#!/usr/bin/env python3
"""
MIT AI Studio - Crew AI Example Agent
A simple example of a Crew AI agent system that represents an AI Studio student.

This example demonstrates:
- Creating multiple specialized agents
- Defining tasks for each agent
- Orchestrating agents in a crew
- Running the crew from the terminal

Author: MIT AI Studio
"""

import os
from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool, FileWriterTool, FileReadTool


# Set up environment variables (you would need to set these with your actual API keys)
# For this example, we'll use placeholder values
# os.environ["SERPER_API_KEY"] = "your-serper-api-key-here"  # Optional: for web search






def create_twin_agent():
    return Agent(
        role='The little me of myself',
        goal='Provide short paragraph about the question asked on Johnson behalf given his information',
        backstory="""You are Johnson Wang, a Harvard masters student in Computational Biology and Data Science, 
        with a strong background in mathematics, biochemistry, and computer science. 
        You have hands-on experience with large language models (LoRA, RAG) and multimodal learning (VLM + Adapter for short-video tagging). 
        You are driven to apply AI methods to real-world biomedical and multimodal problems, and you value clear, rigorous, 
        yet approachable communication in your answers.""",
        verbose=True,
        allow_delegation=False,
        tools=[FileReadTool(file_path='./information.txt')]  # Tool to read files
    )


def create_writer_agent():
    return Agent(
        role='Formal Response Writer',
        goal='Take a draft first-person response and produce a concise, formal, and polished reply suitable for sending',
        backstory="""You are a professional writer who helps Johnson Wang communicate. 
        Make sure the final response sounds polished but still personal, with Johnson's own voice: 
        curious, analytical, but approachable. Keep it clear, avoid excessive jargon, 
        and highlight Johnson's unique AI+biology background when possible.""",

        verbose=True,
        allow_delegation=False,
        tools=[FileWriterTool()]  # Tool to write files
    )



def create_johnson_response_task(agent, question):
    """Create a research task for the research agent."""
    return Task(
        description=f"""Question: {question}

        Your task (on behalf of Johnson Wang):
        1. Read `information.txt` to learn Johnson's background and perspective.
        2. The answer must explicitly reference Johnson's background (Harvard master's in AI + biology, math/CS training).
        3. Where relevant, connect to Johnson's projects and experiences.
        4. Provide a short supporting paragraph (3-4 sentences) that explains the reasoning or details.

        Keep the reply honest, try not to invent ideas that is out of the scope of Johnson's knowledge (PhD level knowledge).
        """,

        expected_output="""A short structured text containing the the answer to the question
        """,
        agent=agent
    )


def create_writing_task(agent):
    """Create a writing task for the writer agent using the twin agent's draft output.

    draft_output is expected to be a small structured object or text containing at least
    an 'answer' (2-3 sentences) and optional 'support' notes.
    """

    return Task(
        description=f"""You are given a short draft response (from Johnson's twin agent).
        
        1. Convert the draft into a concise, formal, first-person reply (2-4 sentences).
        2. Preserve the factual content and citations from the draft; do not invent facts.
        3. Optionally provide a single short formal context paragraph if needed.
        4. Save the final reply as 'johnson_reply.md' and return a short confirmation.""",

        expected_output= "A formal first-person reply saved to 'johnson_reply.md' and a short status message.",
        agent=agent
    )



def main():
    """Main runner: collect a question, create agents/tasks, run the crew, and report results."""
    print("🚀 Welcome to Chat use Johnson - a master student at Harvard studying AI and biology")
    print("=" * 50)
    
    # Get topic from user input
    question = input("Enter a question you'd like Johnson to answer: ")
    if not question.strip():
        question = "Explain my background in 3 sentences"
        print(f"Using default question: {question}")
    
    print(f"\n📚 Question: {question}")
    print("=" * 50)
    
    # Create agents
    print("\n🤖 Creating AI agents...")
    researcher = create_twin_agent()
    writer = create_writer_agent()
    
    # Create tasks
    # Create tasks
    print("📋 Setting up tasks...")
    research_task = create_johnson_response_task(researcher, question)
    writing_task = create_writing_task(writer)

    
    # Create crew
    print("👥 Assembling the crew...")
    crew = Crew(
        agents=[researcher, writer],
        tasks=[research_task, writing_task],
        process=Process.sequential,  # Tasks will be executed in sequence
        verbose=True
    )
    
    # Execute the crew
    print("\n🎯 Starting crew execution...")
    print("=" * 50)
    
    try:
        result = crew.kickoff()

        print("\n✅ Crew execution completed!")
        print("=" * 50)
        print("📄 Final Result:")
        print(result)

        # Check if the article or reply file was created
        if os.path.exists('johnson_reply.md'):
            print("\n📝 Reply successfully saved to 'johnson_reply.md'")
            with open('johnson_reply.md', 'r') as f:
                content = f.read()
                print(f"📊 Reply length: {len(content)} characters")
        else:
            print("\n⚠️  No output file found. The agents may not have used the file tools.")

    except Exception as e:
        print(f"\n❌ An error occurred: {str(e)}")
        print("\n💡 Note: This example requires valid API keys to function properly.")
        print("Please set your OPENAI_API_KEY environment variable.")


if __name__ == "__main__":
    main()


