import requests
import json
import random
import time
import threading

# ANSI escape codes for color formatting
GREEN = "\033[92m"    # Warna hijau untuk respons sukses
RED = "\033[91m"      # Warna merah untuk error
YELLOW = "\033[93m"   # Warna kuning untuk peringatan atau retry
RESET = "\033[0m"     # Reset warna ke default

# Read API key and URL from file
with open('account.txt', 'r') as file:
    api_key = file.readline().strip()
    api_url = file.readline().strip()

# Read messages from file
with open('message.txt', 'r') as file:
    user_messages = file.readlines()

user_messages = [msg.strip() for msg in user_messages]

def send_request(message):
    headers = {
        'Authorization': f'Bearer {api_key}',
        'accept': 'application/json',
        'Content-Type': 'application/json'
    }

    data = {
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": message}
        ]
    }

    while True:
        try:
            response = requests.post(api_url, headers=headers, data=json.dumps(data))

            if response.status_code == 200:
                try:
                    response_json = response.json()
                    print(f"{GREEN}Response for message: '{message}'{RESET}")
                    print(f"{GREEN}{json.dumps(response_json, indent=2)}{RESET}")  # Pretty print JSON response
                    break
                except json.JSONDecodeError:
                    print(f"{RED}Error: Received invalid JSON response for message: '{message}'{RESET}")
                    print(f"{RED}Response Text: {response.text}{RESET}")
            else:
                print(f"{YELLOW}Error: {response.status_code}, {response.text}. Retrying...{RESET}")
                time.sleep(5)
        except requests.exceptions.RequestException as e:
            print(f"{RED}Request failed with error: {e}. Retrying...{RESET}")
            time.sleep(5)

def start_thread():
    while True:
        random_message = random.choice(user_messages)
        send_request(random_message)

# Get number of threads from user
try:
    num_threads = int(input("Enter the number of threads you want to use: "))
    if num_threads < 1:
        print(f"{RED}Please enter a number greater than 0.{RESET}")
        exit()
except ValueError:
    print(f"{RED}Invalid input. Please enter an integer.{RESET}")
    exit()

# Start threads
threads = []
for _ in range(num_threads):
    thread = threading.Thread(target=start_thread)
    threads.append(thread)
    thread.start()

# Wait for threads to finish
for thread in threads:
    thread.join()

print(f"{GREEN}All requests have been processed.{RESET}")
