import os
from dotenv import load_dotenv

from flask import Flask, jsonify, render_template, request
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

# Example agent class
class ExampleAgent:
    def __init__(self, name):
        self.name = name

    def do_work(self, data):
        time.sleep(1)  # Simulate work
        return f"Agent {self.name} processed {data}"

def run_multiagent_tasks():
    agents = [ExampleAgent(f"A{i}") for i in range(5)]
    tasks = [(agent.do_work, (f"task-{i}",), {}) for i, agent in enumerate(agents)]
    results = []
    with ThreadPoolExecutor(max_workers=5) as executor:
        future_to_task = {
            executor.submit(func, *args, **kwargs): (func, args, kwargs)
            for func, args, kwargs in tasks
        }
        for future in as_completed(future_to_task):
            func, args, kwargs = future_to_task[future]
            try:
                result = future.result()
                results.append(result)
            except Exception as exc:
                results.append(f"Task {func.__name__} generated an exception: {exc}")
    for res in results:
        print(res)

if __name__ == "__main__":
    run_multiagent_tasks()
import google.generativeai as genai
from src.project2_legal_agent.crew import LegalAgentCrew

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-2.5-flash')


def ai_bot_response(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        print(f"Error generating response: {e}")
        return f"Sorry, I encountered an error: {str(e)}"


def legal_agent_response(query):
    """Get response from Legal AI Agent system"""
    try:
        legal_crew = LegalAgentCrew()
        legal_crew.create_agents()
        legal_crew.create_tasks(query)
        crew = legal_crew.create_crew()
        result = crew.kickoff()

        # Always try to collect both advisory and media source outputs
        main_answer = None
        references = ""
        # If result is a dict, try to extract both
        if isinstance(result, dict):
            advisory = None
            media = None
            for k, v in result.items():
                if k.lower().startswith("advisory") or k.lower().startswith("legal_advisor"):
                    advisory = v
                if isinstance(v, dict) and ("videos" in v or "articles" in v):
                    media = v
            main_answer = advisory if advisory else str(result)
            if media:
                references += "\n\nReferences and Further Learning:\n"
                if media.get("videos"):
                    references += "\nVideos:\n" + "\n".join(f"- {link}" for link in media["videos"])
                if media.get("articles"):
                    references += "\nArticles:\n" + "\n".join(f"- {link}" for link in media["articles"])
        else:
            # If result is not a dict, try to get both outputs from the crew's tasks
            # (CrewAI may store outputs in crew.tasks or similar)
            try:
                # Try to access all task results if available
                all_results = getattr(crew, "results", None) or getattr(crew, "_results", None)
                if all_results and isinstance(all_results, dict):
                    advisory = None
                    media = None
                    for k, v in all_results.items():
                        if k.lower().startswith("advisory") or k.lower().startswith("legal_advisor"):
                            advisory = v
                        if isinstance(v, dict) and ("videos" in v or "articles" in v):
                            media = v
                    main_answer = advisory if advisory else str(result)
                    if media:
                        references += "\n\nReferences and Further Learning:\n"
                        if media.get("videos"):
                            references += "\nVideos:\n" + "\n".join(f"- {link}" for link in media["videos"])
                        if media.get("articles"):
                            references += "\nArticles:\n" + "\n".join(f"- {link}" for link in media["articles"])
                else:
                    main_answer = str(result)
            except Exception:
                main_answer = str(result)
        return main_answer + references
    except Exception as e:
        print(f"Error in legal agent: {e}")
        return f"Sorry, the legal AI agent encountered an error: {str(e)}"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get_response", methods=["POST"])
def get_response():
    try:
        data = request.json
        user_input = data.get("user_input")
        if not user_input:
            return jsonify({"response": "Please provide a message."}), 400
        bot_response = ai_bot_response(user_input)
        return jsonify({"response": bot_response})
    except Exception as e:
        print(f"Error in get_response: {e}")
        return jsonify({"response": f"Error: {str(e)}"}), 500


@app.route("/legal_query", methods=["POST"])
def legal_query():
    """Endpoint for Legal AI Agent queries"""
    try:
        data = request.json
        user_query = data.get("user_query")
        if not user_query:
            return jsonify({"response": "Please provide a legal query."}), 400
        
        print(f"\n{'='*80}\nProcessing Legal Query: {user_query}\n{'='*80}\n")
        legal_response = legal_agent_response(user_query)
        return jsonify({"response": legal_response})
    except Exception as e:
        print(f"Error in legal_query: {e}")
        return jsonify({"response": f"Error: {str(e)}"}), 500



if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
