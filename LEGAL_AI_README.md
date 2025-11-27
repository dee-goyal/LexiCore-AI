# Legal AI Agent System 🏛️⚖️

An intelligent multi-agent system for analyzing laws, constitutional provisions, and legal matters using CrewAI and Google's Gemini AI.

## 🌟 Features

- **Multi-Agent System**: 4 specialized AI agents working together
  - Legal Researcher
  - Constitutional Expert
  - Legal Analyst
  - Legal Advisor

- **Comprehensive Analysis**: 
  - Research laws and statutes
  - Analyze constitutional provisions
  - Understand legal implications
  - Get plain-language explanations

- **Custom Tools**:
  - Legal Search Tool
  - Constitution Analysis Tool
  - Case Law Search Tool

- **Knowledge Base**: Expandable repository for legal documents

## 📁 Project Structure

```
src/
├── project2_legal_agent/
│   ├── __init__.py
│   ├── main.py              # Main entry point
│   ├── crew.py              # Agent crew definition
│   ├── config/
│   │   ├── agents.yaml      # Agent configurations
│   │   └── tasks.yaml       # Task definitions
│   └── tools/
│       ├── legal_search_tool.py
│       ├── constitution_tool.py
│       └── case_law_tool.py
knowledge/                    # Legal documents storage
tests/                       # Unit tests
legal_analysis.md            # Analysis results
legal_result.md              # Latest result
```

## 🚀 Quick Start

### 1. Install Dependencies

```bash
cd C:\Users\HP\Downloads\openai-flask-starter-main\openai-flask-starter-main
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### 2. Set Up Environment Variables

Make sure your `.env` file has:
```env
GEMINI_API_KEY=your-gemini-api-key-here
SERPER_API_KEY=your-serper-key-here  # Optional for web search
```

### 3. Run the Legal AI Agent

**Interactive Mode:**
```bash
python src/project2_legal_agent/main.py
```

**Single Query:**
```bash
python src/project2_legal_agent/main.py "What is Article 21 of the Constitution?"
```

## 📚 How It Works

### The Agents

1. **Legal Researcher** 🔍
   - Searches for relevant laws and statutes
   - Gathers legal information from various sources
   - Provides comprehensive research findings

2. **Constitutional Expert** 📜
   - Analyzes constitutional provisions
   - Explains fundamental rights
   - Provides historical and modern interpretations

3. **Legal Analyst** 📊
   - Examines practical implications
   - Analyzes case law and precedents
   - Provides real-world application examples

4. **Legal Advisor** 💼
   - Synthesizes all findings
   - Provides clear, actionable advice
   - Explains complex legal concepts simply

### The Process

```
Query → Legal Researcher → Constitutional Expert → Legal Analyst → Legal Advisor → Final Report
```

Each agent performs its specialized task and passes insights to the next, resulting in comprehensive legal analysis.

## 🛠️ Customization

### Adding Legal Documents

1. Place documents in the `knowledge/` folder
2. Organize by category (constitution, laws, cases)
3. Agents will reference these documents

### Enhancing Tools

Edit the tool files in `src/project2_legal_agent/tools/`:
- Implement RAG (Retrieval Augmented Generation)
- Connect to legal databases
- Add web scraping capabilities
- Integrate with legal APIs

### Configuring Agents

Modify `config/agents.yaml` to:
- Change agent roles and goals
- Adjust expertise areas
- Customize backstories

Modify `config/tasks.yaml` to:
- Define new tasks
- Change task priorities
- Adjust output formats

## 📖 Example Queries

```
"What does Article 19 of the Constitution say about freedom of speech?"
"Explain the Right to Privacy in India"
"What are the provisions of Section 498A IPC?"
"Difference between cognizable and non-cognizable offenses"
"What is the doctrine of basic structure?"
```

## 🔧 Advanced Usage

### Running Tests

```bash
pytest tests/test_legal_agent.py -v
```

### Integration with Flask App

The legal agent can be integrated with the existing Flask app to provide a web interface for legal queries.

### Adding More Agents

1. Define new agent in `config/agents.yaml`
2. Create agent method in `crew.py`
3. Add corresponding task
4. Update crew initialization

## 📝 Knowledge Base

Add legal documents to enhance agent capabilities:

```
knowledge/
├── constitution/
│   └── constitution_of_india.txt
├── laws/
│   ├── ipc.txt
│   ├── crpc.txt
│   └── evidence_act.txt
└── cases/
    └── landmark_judgments.txt
```

## 🔍 Tools Available

### Legal Search Tool
Searches through legal documents and databases

### Constitution Tool
Analyzes constitutional articles and amendments

### Case Law Tool
Finds relevant precedents and judicial decisions

### Web Tools (Optional)
- SerperDevTool: Web search
- ScrapeWebsiteTool: Extract content from legal websites

## 🤝 Contributing

To improve the legal agent:
1. Add more specialized agents
2. Enhance existing tools
3. Expand the knowledge base
4. Improve task definitions

## ⚠️ Disclaimer

This AI system is for informational and educational purposes only. It does not constitute legal advice. Always consult qualified legal professionals for specific legal matters.

## 📄 License

MIT License - Feel free to use and modify for your needs.

## 🆘 Troubleshooting

**API Key Issues:**
- Ensure GEMINI_API_KEY is set in `.env`
- Check API quota limits

**Import Errors:**
- Run `pip install -r requirements.txt`
- Activate virtual environment

**Agent Not Working:**
- Check agent configuration in YAML files
- Verify LLM initialization
- Review error logs

## 🎯 Next Steps

1. **Populate Knowledge Base**: Add legal documents
2. **Test Agents**: Run example queries
3. **Customize**: Adjust agents and tasks for your needs
4. **Integrate**: Connect with databases or web APIs
5. **Deploy**: Set up web interface or API endpoint

Happy Legal Research! ⚖️
