import json
import pytest
import requests

BASE_URL = "http://localhost:8000"


# Function to get a bearer token
def get_bearer_token():
    login_url = f"{BASE_URL}/auth/login"
    
    login_data = {
        "username": "gymhero@mail.com",  # replace with actual username
        "password": "gymhero",  # replace with actual password
    }
    
    response = requests.post(login_url, data=login_data)
    
    # Check if the request was successful
    assert response.status_code == 200, f"Login failed with status code {response.status_code}"

    # Extract token from response
    token = response.json().get("access_token")
    assert token, "No token found in the login response"
    return token

# Fixture to retrieve and provide the bearer token
@pytest.fixture(scope="session")
def bearer_token():
    token = get_bearer_token()
    return token

# Function to parse user data, capturing both value and weight_id
def parse_user_data(file_path):
    user_data = {}
    weights = {}

    # Read the text file
    with open(file_path, "r") as file:
        for line in file:
            # Split the line by ": " into 3 parts (key, weight_id, value)
            parts = line.strip().split(": ", 2)  
            if len(parts) != 3:
                continue  # Skip malformed lines

            key, weight_id, value = parts
            
            # Handle special cases for boolean or None
            if value.lower() == "true":
                value = True
            elif value.lower() == "false":
                value = False
            elif value == " ":
                value = None  # Assuming empty fields should be None
            
            # Store the value in the user_data dictionary
            user_data[key] = value

            # Store the weight_id in the weights dictionary
            if key not in weights:
                weights[key] = {}
            weights[key] = weight_id

    return user_data, weights

def load_weights_from_file(file_path="weights.json"):
    try:
        with open(file_path, "r") as json_file:
            data = json.load(json_file)
        return data
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")
        return None

def save_updated_weights_to_file(updated_weights, file_path="weights.json"):
    with open(file_path, 'w') as json_file:
        json.dump(updated_weights, json_file, indent=4)
    print(f"Updated weights saved to {file_path}")
    
    
def update_weights_based_on_feedback(response, used_weights, file_path="/home/mononoke/Desktop/gymhero/grammarinator/weights.json"):
    current_weights = load_weights_from_file(file_path)
    if not current_weights:
        return
    
    for field, value in used_weights.items():
        if response.status_code == 201:
            current_weights[field]["0"][value] += 1

        elif response.status_code == 409:
            
            current_weights[field]["0"][value] += 0.5

        else:
            if current_weights[field]["0"][value] > 1:
                current_weights[field]["0"][value] -= 1
            
    save_updated_weights_to_file(current_weights, file_path)

@pytest.fixture
def user_data():
    file_path = "/home/mononoke/Desktop/gymhero/grammarinator/tests/create_user/create_user_0.txt"
    user_data, weights = parse_user_data(file_path)
    return user_data, weights

# Test function to create a user
def test_create_user(user_data, bearer_token):
    create_user_url = f"{BASE_URL}/users"

    headers = {
        "Authorization": f"Bearer {bearer_token}"  # Add bearer token for authentication
    }
    
    clean_user_data = {key: value for key, value in user_data[0].items() if key != "procedure"}
    print(clean_user_data)
    response = requests.post(create_user_url, json=clean_user_data, headers=headers)
    update_weights_based_on_feedback(response, user_data[1])
    print(response.content)

    print('weights updated')