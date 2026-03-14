from agents.sub_agents.customer_support import customer_support_agent
from agents.sub_agents.booking import booking_agent
from agents.sub_agents.location import location_agent
from google.adk import Agent
from google.adk.models import Gemini

# Define the Orchestrator as the entry point for ADK
root_agent = Agent(
    name="orchestrator",
    description="Orchestrates requests between specialised sub-agents.",
    instruction="""You are the lead orchestrator. 
    Analyze the user's request and delegate to the most appropriate sub-agent:
    - customer_support: for general help, greetings, and miscellaneous questions.
    - booking_assistant: for scheduling, appointments, and bookings.
    - location_assistant: for addresses, office hours, and physical locations.
    
    If you are unsure, default to customer_support.""",
    sub_agents=[customer_support_agent, booking_agent, location_agent],
    model=Gemini(model_id="gemini-2.0-pro-exp-02-05")
)

if __name__ == "__main__":
    from google.adk.runners import Runner
    from google.adk.sessions import InMemorySessionService
    import asyncio

    async def main():
        runner = Runner(
            app_name="MultiAgentApp",
            agent=root_agent,
            session_service=InMemorySessionService(),
            auto_create_session=True
        )
        print("ADK App initialized and ready.")

    asyncio.run(main())
