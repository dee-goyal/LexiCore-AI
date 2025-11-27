"""
Legal AI Agent Crew
This module defines the crew of AI agents for legal research and analysis
"""

from crewai import Agent, Crew, Process, Task
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv
import yaml

# Load environment variables
load_dotenv()

# Import custom tools
from .tools import LegalSearchTool, ConstitutionTool, CaseLawTool


class LegalAgentCrew:
    """Legal AI Agent Crew for law and constitution analysis"""
    
    def __init__(self):
        """Initialize the crew with Gemini LLM"""
        # Load configurations
        config_path = os.path.join(os.path.dirname(__file__), 'config')
        
        with open(os.path.join(config_path, 'agents.yaml'), 'r') as f:
            self.agents_config = yaml.safe_load(f)
        
        with open(os.path.join(config_path, 'tasks.yaml'), 'r') as f:
            self.tasks_config = yaml.safe_load(f)
        
        # Initialize LLM  
        self.llm = "gemini/gemini-2.5-flash"
        os.environ["GOOGLE_API_KEY"] = os.getenv("GEMINI_API_KEY")
    
    def create_agents(self):
        """Create all agents"""
        self.legal_researcher_agent = Agent(
            role=self.agents_config['legal_researcher']['role'],
            goal=self.agents_config['legal_researcher']['goal'],
            backstory=self.agents_config['legal_researcher']['backstory'],
            tools=[LegalSearchTool],
            llm=self.llm,
            verbose=True
        )
        
        self.constitution_expert_agent = Agent(
            role=self.agents_config['constitution_expert']['role'],
            goal=self.agents_config['constitution_expert']['goal'],
            backstory=self.agents_config['constitution_expert']['backstory'],
            tools=[ConstitutionTool, LegalSearchTool],
            llm=self.llm,
            verbose=True
        )
        
        self.legal_analyst_agent = Agent(
            role=self.agents_config['legal_analyst']['role'],
            goal=self.agents_config['legal_analyst']['goal'],
            backstory=self.agents_config['legal_analyst']['backstory'],
            tools=[CaseLawTool, LegalSearchTool],
            llm=self.llm,
            verbose=True
        )
        
        self.legal_advisor_agent = Agent(
            role=self.agents_config['legal_advisor']['role'],
            goal=self.agents_config['legal_advisor']['goal'],
            backstory=self.agents_config['legal_advisor']['backstory'],
            llm=self.llm,
            verbose=True
        )
    
    def create_tasks(self, query: str):
        """Create all tasks with the given query"""
        self.research_task = Task(
            description=self.tasks_config['research_law_task']['description'].format(query=query),
            expected_output=self.tasks_config['research_law_task']['expected_output'],
            agent=self.legal_researcher_agent
        )
        
        self.constitution_task = Task(
            description=self.tasks_config['analyze_constitution_task']['description'].format(query=query),
            expected_output=self.tasks_config['analyze_constitution_task']['expected_output'],
            agent=self.constitution_expert_agent
        )
        
        self.analysis_task = Task(
            description=self.tasks_config['legal_analysis_task']['description'].format(query=query),
            expected_output=self.tasks_config['legal_analysis_task']['expected_output'],
            agent=self.legal_analyst_agent
        )
        
        self.advisory_task = Task(
            description=self.tasks_config['advisory_task']['description'].format(query=query),
            expected_output=self.tasks_config['advisory_task']['expected_output'],
            agent=self.legal_advisor_agent,
            context=[self.research_task, self.constitution_task, self.analysis_task]
        )
    
    def create_crew(self) -> Crew:
        """Create and return the crew"""
        return Crew(
            agents=[
                self.legal_researcher_agent,
                self.constitution_expert_agent,
                self.legal_analyst_agent,
                self.legal_advisor_agent
            ],
            tasks=[
                self.research_task,
                self.constitution_task,
                self.analysis_task,
                self.advisory_task
            ],
            process=Process.sequential,
            verbose=True
        )
