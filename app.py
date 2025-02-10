from flask import Flask, render_template, request, jsonify
import re
import requests
from flask_cors import CORS  # Import CORS

app = Flask(__name__, static_folder='static')  # Configure static folder
CORS(app) # Enable CORS for all routes

# Mira API endpoint and your API key
MIRA_API_URL = "https://api.mira.com/v1/chat"  # Replace with the actual Mira API endpoint
MIRA_API_KEY = "sb-d1da1684b815b93eb68400e986c39022"  # Replace with your actual key

def get_answer(message):
    message = message.lower()
    message = re.sub(r'[^\w\s]', '', message)

    payload = {"text": message} # Mira expects "text" key

    try:
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {MIRA_API_KEY}"  # Use Bearer token in header
        }
        response = requests.post(MIRA_API_URL, json=payload, headers=headers)
        response.raise_for_status()

        mira_data = response.json() # Parse JSON response
        bot_response = mira_data.get("response", "I'm sorry, I couldn't understand that.")

    except requests.exceptions.RequestException as e:
        print(f"Error communicating with Mira API: {e}")
        if response: # Print response details for debugging
            print(f"Response text: {response.text}")
            print(f"Response status code: {response.status_code}")
        bot_response = "Sorry, I'm having trouble connecting to the server. Please try again later."
    except (KeyError, TypeError) as e:  # Handle JSON parsing errors
        print(f"Error parsing Mira response: {e}")
        bot_response = "Error processing the response from Mira."
        if mira_data:
            print(f"Mira Data: {mira_data}")

    return bot_response

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data['message']
    bot_response = get_answer(user_message)
    return jsonify({'response': bot_response})

@app.route('/')
def index():
    return render_template('index.html')  # Use render_template

if __name__ == '__main__':
    app.run(debug=True)

    from mira_sdk import MiraClient, Flow

# Initialize the client
client = MiraClient(config={"API_KEY": "YOUR_API_KEY"})

version = "1.0.0"
input_data = {}

# If no version is provided, latest version is used by default
if version:
    flow_name = f"@aayushalways/compound/{version}"
else:
    flow_name = "@aayushalways/compound"

result = client.flow.execute(flow_name, input_data)
print(result)

from mira_sdk import MiraClient, Flow

# Initialize the client
client = MiraClient(config={"API_KEY": "YOUR_API_KEY"})

version = "1.0.0"
input_data = {}

# If no version is provided, latest version is used by default
if version:
    flow_name = f"@aayushalways/intent-recognition-flow/{version}"
else:
    flow_name = "@aayushalways/intent-recognition-flow"

result = client.flow.execute(flow_name, input_data)
print(result)

from mira_sdk import MiraClient, Flow

# Initialize the client
client = MiraClient(config={"API_KEY": "YOUR_API_KEY"})

version = "1.0.0"
input_data = {}

# If no version is provided, latest version is used by default
if version:
    flow_name = f"@aayushalways/entity/{version}"
else:
    flow_name = "@aayushalways/entity"

result = client.flow.execute(flow_name, input_data)
print(result)
from mira_sdk import MiraClient, Flow

# Initialize the client
client = MiraClient(config={"API_KEY": "YOUR_API_KEY"})

version = "1.0.0"
input_data = {}

# If no version is provided, latest version is used by default
if version:
    flow_name = f"@aayushalways/response/{version}"
else:
    flow_name = "@aayushalways/response"

result = client.flow.execute(flow_name, input_data)
print(result)

from mira_sdk import MiraClient, Flow

# Initialize the client
client = MiraClient(config={"API_KEY": "YOUR_API_KEY"})

version = "1.0.0"
input_data = {}

# If no version is provided, latest version is used by default
if version:
    flow_name = f"@aayushalways/data-r-f/{version}"
else:
    flow_name = "@aayushalways/data-r-f"

result = client.flow.execute(flow_name, input_data)
print(result)

from mira_sdk import MiraClient, Flow

# Initialize the client
client = MiraClient(config={"API_KEY": "YOUR_API_KEY"})

version = "1.0.0"
input_data = {}

# If no version is provided, latest version is used by default
if version:
    flow_name = f"@aayushalways/fallback/{version}"
else:
    flow_name = "@aayushalways/fallback"

result = client.flow.execute(flow_name, input_data)
print(result)
