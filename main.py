import asyncio
import os
from dotenv import load_dotenv
from google.adk import Agent, Runner
from google.adk.models import Gemini
from google.adk.sessions import InMemorySessionService
from google.genai import types
from agents.agent import root_agent as orchestrator_agent

load_dotenv()

    description="Orchestrates requests between specialized sub-agents.",
    instruction="""You are the lead orchestrator. 
    Analyze the user's request and delegate to the most appropriate sub-agent:
    - customer_support: for general help, greetings, and miscellaneous questions.
    - booking_assistant: for scheduling, appointments, and bookings.
    - location_assistant: for addresses, office hours, and physical locations.
    
    If you are unsure, default to customer_support.""",
    sub_agents=[customer_support_agent, booking_agent, location_agent],
    model=Gemini(model_id="gemini-2.0-pro-exp-02-05")
)

async def run_system():
    # Initialize the Runner with the orchestrator agent and auto-session creation
    runner = Runner(
        app_name="MultiAgentApp",
        agent=orchestrator_agent,
        session_service=InMemorySessionService(),
        auto_create_session=True
    )
    
    print("Multi-Agent System Ready.")
    print(f"Project ID: {os.getenv('GOOGLE_CLOUD_PROJECT')}")
    
    queries = [
        "I'd like to book an appointment for next Tuesday.",
        "Where is your office address?",
        "Hello, how can you help me today?"
    ]
    
    for query in queries:
        print(f"\nUser Query: {query}")
        print("Routing...")
        
        try:
            # InMemoryRunner.run_async returns an AsyncGenerator[Event, None]
            # 'new_message' must be a types.Content object
            async for event in runner.run_async(
                user_id="test_user", 
                session_id="session_1", 
                new_message=types.Content(
                    role="user",
                    parts=[types.Part(text=query)]
                )
            ):
                # Print relevant text content from the model
                if hasattr(event, 'content') and event.content:
                    for part in event.content.parts:
                        if part.text:
                            print(f"Agent Response: {part.text}")
        except Exception as e:
            print(f"Error running system: {e}")
            import traceback
            traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(run_system())
