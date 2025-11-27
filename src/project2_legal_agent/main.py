#!/usr/bin/env python
"""
Legal AI Agent - Main Entry Point
Run this script to interact with the legal AI system
"""

import os
import sys
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Add the project root to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from src.project2_legal_agent.crew import LegalAgentCrew


def run_legal_analysis(query: str):
    """
    Run legal analysis on a query
    
    Args:
        query: The legal question or topic to analyze
    """
    print(f"\n{'='*80}")
    print(f"Legal AI Agent System")
    print(f"{'='*80}")
    print(f"\nQuery: {query}\n")
    print(f"{'='*80}\n")
    
    try:
        # Initialize the crew
        legal_crew = LegalAgentCrew()
        legal_crew.create_agents()
        legal_crew.create_tasks(query)
        crew = legal_crew.create_crew()
        
        # Run the analysis
        result = crew.kickoff()
        
        print(f"\n{'='*80}")
        print(f"FINAL LEGAL ADVISORY")
        print(f"{'='*80}\n")
        print(result)
        print(f"\n{'='*80}\n")
        
        return result
        
    except Exception as e:
        print(f"\nError: {str(e)}")
        print("\nMake sure you have:")
        print("1. Set GEMINI_API_KEY in your .env file")
        print("2. Installed all required packages: pip install -r requirements.txt")
        print("3. Set SERPER_API_KEY if using web search (optional)")
        return None


def interactive_mode():
    """Run the legal AI agent in interactive mode"""
    print("\n" + "="*80)
    print("Legal AI Agent - Interactive Mode")
    print("="*80)
    print("\nAsk questions about laws, constitution, or legal matters.")
    print("Type 'exit' or 'quit' to stop.\n")
    
    while True:
        try:
            query = input("\nYour legal query: ").strip()
            
            if query.lower() in ['exit', 'quit', 'q']:
                print("\nThank you for using Legal AI Agent!")
                break
            
            if not query:
                print("Please enter a valid query.")
                continue
            
            run_legal_analysis(query)
            
        except KeyboardInterrupt:
            print("\n\nThank you for using Legal AI Agent!")
            break
        except Exception as e:
            print(f"\nError: {str(e)}")


def main():
    """Main function"""
    # Check if API key is set
    if not os.getenv("GEMINI_API_KEY"):
        print("\n" + "="*80)
        print("ERROR: GEMINI_API_KEY not found!")
        print("="*80)
        print("\nPlease set your Gemini API key in the .env file:")
        print("GEMINI_API_KEY=your-api-key-here")
        print("\n" + "="*80 + "\n")
        return
    
    # Check for command line arguments
    if len(sys.argv) > 1:
        query = " ".join(sys.argv[1:])
        run_legal_analysis(query)
    else:
        # Run in interactive mode
        interactive_mode()


if __name__ == "__main__":
    main()
