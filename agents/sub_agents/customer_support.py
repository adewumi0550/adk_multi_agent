from google.adk import Agent
from google.adk.models import Gemini
import os
from dotenv import load_dotenv

load_dotenv()

# Define the Customer Support Agent
customer_support_agent = Agent(
    name="customer_support",
    description="Handles general customer inquiries and initial interaction.",
    instruction="""You are a professional and helpful customer support assistant. 
    Acknowledge the user's query and provide a polite, helpful response. 
    If you cannot answer the query, ask for more details or suggest contacting a human representative.""",
    model=Gemini(model_id="gemini-2.0-pro-exp-02-05")
)
