# Import necessary modules from Flask and other libraries
from flask import Flask, request, jsonify  # Flask web framework, request parsing, and JSON response
from flask_cors import CORS  # Handles Cross-Origin Resource Sharing (CORS) for AJAX requests
import openai  # OpenAI Python SDK for AI chat

# Initialize Flask app
app = Flask(__name__)
# Enable CORS for all routes (allows frontend JS to call backend API)
CORS(app)

# OpenAI API key (for demo/MVP; in production, use environment variables for security)
OPENAI_API_KEY = "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"
# Create OpenAI client instance
client = openai.OpenAI(api_key=OPENAI_API_KEY)

# Define the chat endpoint for AJAX POST requests from the frontend
@app.route('/api/chat', methods=['POST'])
def chat():
    # Parse JSON data from the request
    data = request.get_json()
    user_message = data.get('message', '')  # Extract user message
    try:
        # Call OpenAI API to generate a chat completion
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # Model to use
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},  # System prompt
                {"role": "user", "content": user_message}  # User's message
            ]
        )
        # Extract the AI's reply from the response
        bot_reply = response.choices[0].message.content
        # Return the reply as JSON
        return jsonify({'reply': bot_reply})
    except Exception as e:
        # Handle errors (e.g., API/network issues) and return error message
        return jsonify({'reply': f"Error: {str(e)}"}), 500

# Run the Flask app if this script is executed directly
if __name__ == '__main__':
    app.run(port=5000, debug=True)  # Start server on port 5000 with debug mode 