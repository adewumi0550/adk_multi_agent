# Multi-Agent ADK System

A sophisticated multi-agent system built with the **Google Agent Development Kit (ADK)** and powered by **Gemini 2.0 Pro** via Vertex AI.

## Features

- **Lead Orchestrator**: Automatically routes user queries to the most relevant sub-agent.
- **Booking Assistant**: Handles appointment scheduling and logic.
- **Location Assistant**: Provides information about physical office locations.
- **Customer Support**: Handles general inquiries and greetings.

## Prerequisites

- Python 3.9+ (Tested on 3.14.3)
- A Google Cloud Project with Vertex AI API enabled.
- Google Cloud CLI authenticated.

## Local Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/adewumi0550/adk_multi_agent.git
   cd adk_multi_agent
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install google-adk google-cloud-aiplatform python-dotenv
   ```

4. **Configure Environment Variables**:
   Copy the example environment file and fill in your details:
   ```bash
   cp .env.example .env
   ```
   Edit `.env` and set your `GOOGLE_CLOUD_PROJECT` (e.g., `campuscook-8e47c`).

## Running the Agents

### 1. Interactive CLI
Chat with the agents directly in your terminal:
```bash
adk run agents --session_service_uri memory://
```

### 2. Web UI
Start a local web interface to interact with the agents:
```bash
adk web agents --session_service_uri memory://
```
Access the UI at `http://127.0.0.1:8000`.

### 3. Standalone Script
Run the sample interaction script:
```bash
python3 main.py
```

## Project Structure

- `agents/`: Contains the agent definitions and sub-agents.
- `app.py`: Entry point for the ADK CLI.
- `main.py`: Standalone orchestration script.
- `.env`: Local configuration.
