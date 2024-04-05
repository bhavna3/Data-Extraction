import requests
import json
import time

url = "https://api.induced.ai/api/v1/extract"

payload = {
    "url": "https://github.com/trending",
    "query": "list of all trending repositories",
    "columns": "name, author, stars, repository_url"
}

headers = {
    "x-api-key": "6601af6c3a4f1e12fc59ebe5",
    "Content-Type": "application/json"
}

# Send the initial extraction request
response = requests.request("POST", url, json=payload, headers=headers)

# Check if the request was successful
if response.status_code != 200:
    print("Error:", response.status_code)
    print("Response:", response.text)
    exit()

# Extract the ID from the response
response_data = response.json()
extract_id = response_data['data']['id']
print("Extracting with browser agent..")

# Poll the API until the extraction process is completed
poll_url = f"https://api.induced.ai/api/v1/extract/{extract_id}"
while True:
    poll_response = requests.request("GET", poll_url, headers=headers)
    try:
        poll_data = poll_response.json()
        
        if 'data' in poll_data and 'run' in poll_data['data'] and 'status' in poll_data['data']['run']:
            status = poll_data['data']['run']['status']
            print("Extraction status:", status)
        else:
            print("Error: Unable to find status in JSON response")
            print("Response:", poll_response.text)
            exit()
    except json.JSONDecodeError as e:
        print("Error: Unable to parse JSON response")
        print("Response:", poll_response.text)
        exit()
    
    if status == "COMPLETED":
        break
    elif status == "FAILED":
        print("Extraction failed.")
        exit()
    time.sleep(5)

# Once completed, print the JSON response
print(json.dumps(poll_data, indent=4))

