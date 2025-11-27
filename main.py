import os
from dotenv import load_dotenv

from flask import Flask, jsonify, render_template, request
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
        return str(result)
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


if __name__ == "__main__":
    app.run(debug=True, port=os.getenv("HTTP_PORT", 5000))
