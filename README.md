# Flask Chat Application with WebSocket Integration

This is a Flask-based chat application that utilizes WebSocket communication for real-time messaging. It allows users to exchange messages and receive responses in a chat interface powered by Flask-SocketIO and OpenAI API.

## Features
* **Real-time messaging**: Users can send and receive messages in real-time without the need to refresh the page.
* **Integration with OpenAI API**: Messages sent by users are processed by the OpenAI API to generate responses, creating an interactive chat experience.
* **Simple and intuitive interface**: The chat interface is designed to be user-friendly, with easy-to-use controls for sending messages and viewing responses.

## Technologies Used
- **Flask**: A lightweight web framework for Python used to build the backend server.
- **Flask-SocketIO**: A Flask extension that adds WebSocket support to the application for real-time communication.
- **Socket.io**: A JavaScript library for enabling real-time, bidirectional, and event-based communication between the client and server.
- **OpenAI API**: An API for accessing OpenAI's language models and generating natural language responses.
- **HTML, CSS, JavaScript**: Frontend technologies used to create the user interface and handle client-side interactions.
- **dotenv**: A Python library used for loading environment variables from a .env file.
- **Bootstrap**: A frontend framework used for styling and layout.

## OpenAI API Key

This project uses the OpenAI API for generating responses in the chat application. In order to use the API, you'll need to obtain an API key from OpenAI.

### Obtaining an API Key

1. Sign up for an account on the [OpenAI website](https://openai.com/).
2. Once logged in, navigate to the API section of your account dashboard.
3. Follow the instructions to generate an API key.
4. Copy the generated API key and securely store it.

### Usage Costs

Using the OpenAI API may involve charges based on usage. Please review the pricing information on the [OpenAI website](https://openai.com/pricing) to understand the pricing model and associated costs.

## Prerequisites

* Python 3.x

## Setup

1. Clone the repository:

```bash
  git clone https://github.com/Irene1c/CodeAlpha_ChatGPT_Integration.git
```

2. Go to the project directory:

```bash
  cd CodeAlpha_ChatGPT_Integration
```

3. Create a virtual environment (optional but recommended):

```bash
  python -m venv venv
  source venv/bin/activate  # On Windows, use `source venv/Scripts/activate`
```

4. Install dependencies:

```bash
  pip install -r requirements.txt
```

5. Set up environment variables:

Create a `.env` file in the project root directory.

Add your `OpenAI API key` and `SECRET_KEY` to the .env file:

```
  OPENAI_API_KEY='your_openai_api_key_here'
  SECRET_KEY='your_secret_key_here'
```

7. Run the application:

```bash
  python app.py
```

8. Access the application in your web browser:

```
  http://localhost:5000
```

## Usage

* Enter your message in the input field at the bottom of the chat interface.
* Press the `Send` button to send your message.
* Wait for the response from the chatbot, which will appear in the chat interface.
* Continue the conversation by sending more messages.

## Contributing
Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

* Fork the repository.
* Create a new branch.
* Make your changes.
* Commit your changes.
* Push to the branch.
* Create a new pull request.

## Internship

* This project is part of the tasks for my internship at CodeAlpha.

## License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file for details.
