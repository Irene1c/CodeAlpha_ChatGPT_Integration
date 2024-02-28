from openai import OpenAI, RateLimitError
import os
from flask import Blueprint, request, jsonify


chat = Blueprint('chat', __name__)


client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)


@chat.route('/api', methods=['POST'])
def process_message():
    """ Function to send user message and return response from openai """

    data = request.get_json()
    user_message = data.get('message', '')

    try:
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_message}
            ]
        )

        # Extract the response from the completion
        response = completion.choices[0].message['content']

    # NOTE: The following RateLimitError handling is only for development purposes
    # and should be removed/commented out before deploying to production.
    except RateLimitError as e:
        response = "Rate limit exceeded."

    return jsonify({'response': response})
