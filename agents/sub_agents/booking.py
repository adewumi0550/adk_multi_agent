from google.adk import Agent
from google.adk.models import Gemini
import os
from dotenv import load_dotenv

load_dotenv()

# Define the Booking Agent
booking_agent = Agent(
    name="booking_assistant",
    description="Handles appointment booking and scheduling logic.",
    instruction="""You are an expert booking and scheduling assistant. 
    Your goal is to help users book appointments efficiently. 
    Ask for the date, time, and purpose of the appointment if not provided. 
    Be clear and concise.""",
    model=Gemini(model_id="gemini-2.0-pro-exp-02-05")
)
