# WhatsApp Conversation AI Agent

This project is a WhatsApp conversation AI agent built using FastAPI, OpenAI, Twilio, and AWS S3. The agent is capable of understanding both text and audio inputs and can respond with text or audio. The application is containerized using Docker and orchestrated with Kubernetes. Additionally, a `docker-compose` setup is provided for local development with PostgreSQL.

## Table of Contents

- [Features](#features)
- [Technologies](#technologies)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Deployment](#deployment)
- [API Reference](#api-reference)
- [Contributing](#contributing)
- [License](#license)

## Features

- Understands text messages from WhatsApp
- Processes audio messages and converts them to text
- Generates responses using OpenAI's language model
- Sends responses as text or audio back to WhatsApp
- Stores user data and conversation history in PostgreSQL
- Supports local development with Docker Compose

## Technologies

- **FastAPI**: For building the web API
- **OpenAI**: For natural language processing and response generation
- **Twilio**: For WhatsApp messaging integration
- **AWS S3**: For storing audio files
- **PostgreSQL**: For persistent data storage
- **Docker**: For containerization
- **Kubernetes**: For orchestration in production
- **Docker Compose**: For local development

## Requirements

- Python 3.8+
- Docker
- Docker Compose
- Kubernetes (for deployment)
- AWS account (for S3 access)
- Twilio account (for WhatsApp integration)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/whatsapp-conversation-ai.git
   cd whatsapp-conversation-ai
   ```

2. **Create a `.env` file:**

   Copy the `.env.example` file to `.env` and fill in your Twilio, OpenAI, and AWS credentials.

   ```bash
   cp .env.example .env
   ```

3. **Build the Docker images:**

   ```bash
   docker-compose build
   ```

4. **Run the application locally:**

   ```bash
   docker-compose up
   ```

5. **Migrate the database:**

   After running the application, you may need to initialize the database with the required tables.

   ```bash
   # In a new terminal
   python create_tables.py
   ```

## Usage

1. **WhatsApp Setup:**

   - Configure your Twilio account to connect with your WhatsApp number.
   - Set the webhook URL in your Twilio console to point to your FastAPI endpoint (Use NGROK to generate an URL).

2. **Interacting with the Agent:**

   - Send a message or audio note to your WhatsApp number.
   - The agent will respond based on the input received.

## API Reference

- **POST /webhook**
  - Endpoint for receiving messages from WhatsApp.
  
- **GET /health**
  - Check the health status of the application.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.