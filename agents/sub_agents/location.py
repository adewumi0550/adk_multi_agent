from google.adk import Agent
from google.adk.models import Gemini
import os
from dotenv import load_dotenv

load_dotenv()

# Define the Location Agent
location_agent = Agent(
    name="location_assistant",
    description="Provides information about physical locations.",
    instruction="""You are a helpful location assistant. 
    Your goal is to provide accurate information about our physical offices.
    Main Office: 123 Tech Avenue, Silicon Valley.
    London Branch: 45 Chancery Lane, London.
    Tokyo Branch: 1-1 Chiyoda, Tokyo.
    Be polite and provide the address clearly.""",
    model=Gemini(model_id="gemini-2.0-pro-exp-02-05")
)
