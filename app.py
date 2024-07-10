from flask import Flask, render_template, request, jsonify
import requests
import json
import time

app = Flask(__name__, template_folder='C:/Users/saikeerthana/OneDrive/Desktop/new proj/data_extraction_env/templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/extract', methods=['POST'])
def extract():
    url = "https://api.induced.ai/api/v1/extract"
    payload = {
        "url": request.form['url'],
        "query": request.form['query'],
        "columns": request.form['columns']
    }
    headers = {
        "x-api-key": "6601af6c3a4f1e12fc59ebe5",
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print("Initial request error:", e)
        return jsonify({"error": str(e)}), 500

    response_data = response.json()
    extract_id = response_data.get('data', {}).get('id')
    if not extract_id:
        print("Failed to retrieve extract ID from response")
        return jsonify({"error": "Failed to retrieve extract ID from response"}), 500

    poll_url = f"https://api.induced.ai/api/v1/extract/{extract_id}"
    timeout = time.time() + 60  # 60 seconds from now
    while True:
        if time.time() > timeout:
            print("Polling timed out")
            return jsonify({"error": "Polling timed out"}), 500

        try:
            poll_response = requests.get(poll_url, headers=headers)
            poll_response.raise_for_status()
            poll_data = poll_response.json()
        except requests.exceptions.RequestException as e:
            print("Polling request error:", e)
            return jsonify({"error": str(e)}), 500

        if 'data' in poll_data and 'run' in poll_data['data'] and 'status' in poll_data['data']['run']:
            status = poll_data['data']['run']['status']
            print("Polling status:", status)
        else:
            print("Unable to find status in JSON response")
            return jsonify({"error": "Unable to find status in JSON response", "response": poll_response.text}), 500

        if status == "COMPLETED":
            break
        elif status == "FAILED":
            print("Extraction failed")
            return jsonify({"error": "Extraction failed."}), 500
        time.sleep(5)

    return jsonify(poll_data)

if __name__ == '__main__':
    app.run(debug=True)
