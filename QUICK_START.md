# Legal AI Agent - Quick Start Guide

## 🚀 Getting Started

### Step 1: Verify Installation

Check if all packages are installed:
```bash
.\venv\Scripts\Activate.ps1
python -c "import crewai; print('CrewAI installed successfully!')"
```

### Step 2: Test the Agent

Run a simple query:
```bash
python src/project2_legal_agent/main.py "What is Article 21?"
```

Or use interactive mode:
```bash
python src/project2_legal_agent/main.py
```

### Step 3: Understand the Output

The agents will work in sequence:
1. **Legal Researcher** - Researches the query
2. **Constitutional Expert** - Analyzes constitutional aspects
3. **Legal Analyst** - Provides detailed analysis
4. **Legal Advisor** - Gives final comprehensive advisory

## 📝 Example Queries

Try these queries to see the system in action:

```bash
# Constitutional queries
python src/project2_legal_agent/main.py "Explain Article 19 of the Constitution"
python src/project2_legal_agent/main.py "What are fundamental rights?"

# Legal concepts
python src/project2_legal_agent/main.py "What is the doctrine of basic structure?"
python src/project2_legal_agent/main.py "Explain the right to privacy in India"

# Specific laws
python src/project2_legal_agent/main.py "What is Section 498A IPC?"
python src/project2_legal_agent/main.py "Difference between cognizable and non-cognizable offense"
```

## 🔧 Configuration

### Modify Agent Behavior

Edit `src/project2_legal_agent/config/agents.yaml`:
- Change roles
- Adjust goals
- Customize backstories

### Customize Tasks

Edit `src/project2_legal_agent/config/tasks.yaml`:
- Add new tasks
- Modify descriptions
- Change expected outputs

### Add Knowledge

Place documents in `knowledge/` folder:
```
knowledge/
├── constitution/
│   └── articles.txt
├── laws/
│   └── ipc_sections.txt
└── cases/
    └── landmark_cases.txt
```

## 🎯 Advanced Usage

### 1. Integrate with RAG

Enhance tools in `src/project2_legal_agent/tools/` to:
- Load documents from knowledge folder
- Create embeddings
- Implement semantic search

### 2. Connect to Databases

Modify tools to connect to:
- Indian Kanoon API
- SCC Online
- Government law websites

### 3. Add More Agents

Create specialized agents for:
- Criminal law
- Corporate law
- Family law
- Tax law

### 4. Build Web Interface

Integrate with Flask app in `main.py`:
```python
from src.project2_legal_agent.crew import LegalAgentCrew

@app.route("/legal_query", methods=["POST"])
def legal_query():
    query = request.json.get("query")
    crew = LegalAgentCrew()
    result = crew.crew().kickoff(inputs={'query': query})
    return jsonify({"response": str(result)})
```

## 💡 Tips

1. **Start Simple**: Test with basic queries first
2. **Add Knowledge**: Populate the knowledge folder with legal documents
3. **Monitor Costs**: Watch API usage (Gemini has rate limits)
4. **Iterate**: Improve agent prompts based on results
5. **Validate**: Always verify legal information from authoritative sources

## ⚠️ Important Notes

- This is an AI system for educational and research purposes
- Not a substitute for professional legal advice
- Always verify important legal information
- Respect API rate limits
- Keep sensitive data secure

## 🐛 Troubleshooting

**"ModuleNotFoundError: No module named 'crewai'"**
```bash
.\venv\Scripts\Activate.ps1
pip install crewai crewai-tools langchain langchain-google-genai
```

**"API key not found"**
- Check `.env` file has `GEMINI_API_KEY=your-key`
- Reload environment variables

**"Rate limit exceeded"**
- Wait for quota to reset
- Get a new API key
- Monitor usage at https://ai.dev/usage

**Agents not producing good results**
- Add more documents to knowledge folder
- Refine agent prompts in YAML files
- Improve tool implementations

## 📚 Next Steps

1. Read `LEGAL_AI_README.md` for detailed documentation
2. Explore `config/agents.yaml` and `config/tasks.yaml`
3. Add legal documents to `knowledge/` folder
4. Test different queries
5. Customize agents for your use case

## 🤝 Getting Help

- Check agent output for errors
- Review YAML configuration files
- Test tools individually
- Consult CrewAI documentation: https://docs.crewai.com

Happy Legal Research! ⚖️
