# Data Extraction via API Integration

This project focuses on leveraging Induced AI API for extracting data from GitHub. By sending a URL and a natural language query, users can retrieve structured data without the need for custom scraping scripts. 

## Key Features

- **Utilizes Requests Library**: Interacts seamlessly with the Induced AI API for efficient data extraction.
  
- **Streamlined Data Retrieval**: Enables users to acquire structured data by simply submitting a URL and a natural language query, bypassing the necessity for bespoke scraping scripts.
  
- **Polling Mechanism Implementation**: Incorporates a robust polling mechanism to monitor the extraction status, guaranteeing the completion of data retrieval.
  
- **Robust Error Handling**: Proactively manages various issues such as unsuccessful requests or JSON parsing errors, ensuring smooth script execution.
  
- **Output in JSON Format**: Upon successful completion, presents extracted data encompassing repository names, authors, stars, and URLs in a standardized JSON format for easy consumption and analysis.


## Usage

To utilize the Data Extraction repository for extracting data from GitHub:

1. **Clone the Repository**: Clone the Data Extraction repository to your local machine using the following command:
   ```
   git clone https://github.com/your-username/Data-Extraction.git
   ```

2. **Install Dependencies**: Navigate to the cloned repository directory and install the required dependencies using pip:
   ```
   cd Data-Extraction
   pip install -r requirements.txt
   ```

3. **Set Up API Key**: Obtain an API key from Induced AI and replace `YOUR_API_KEY` in the script with your actual API key.

4. **Run the Script**: Execute the Python script `extract_trending_repos.py` to start the data extraction process:
   ```
   python extract_trending_repos.py
   ```

5. **Monitor Progress**: The script will interact with the Induced AI API to extract trending repositories from GitHub. Monitor the extraction progress and wait for the process to complete.

6. **Retrieve Extracted Data**: Upon completion, the script will print the extracted data including repository names, authors, stars, and URLs in JSON format.

7. **Explore Data**: Explore the extracted data for analysis or further processing as per your requirements.

This usage guide provides step-by-step instructions for setting up and running your GitHub Web Scraper script. Adjustments can be made based on specific requirements or preferences.

##  Example output

{
    "repositories": [
        {
            "name": "awesome-python",
            "author": "vinta",
            "stars": 101893,
            "repository_url": "[https://github.com/vinta/awesome-python](https://github.com/vinta/awesome-python)"
        },
        {
            "name": "system-design-primer",
            "author": "donnemartin",
            "stars": 101800,
            "repository_url": "[https://github.com/donnemartin/system-design-primer](https://github.com/donnemartin/system-design-primer)"
        },
        {
            "name": "public-apis",
            "author": "public-apis",
            "stars": 99410,
            "repository_url": "[https://github.com/public-apis/public-apis](https://github.com/public-apis/public-apis)"
        },
        {
            "name": "Python",
            "author": "TheAlgorithms",
            "stars": 96110,
            "repository_url": "[https://github.com/TheAlgorithms/Python](https://github.com/TheAlgorithms/Python)"
        },
        {
            "name": "thefuck",
            "author": "nvbn",
            "stars": 86164,
            "repository_url": "[https://github.com/nvbn/thefuck](https://github.com/nvbn/thefuck)"
        }
    ]
}

## Contributing

🤝 Contributions are welcome! If you encounter any issues or have suggestions for improvement, feel free to open an issue or submit a pull request.

⚠️ **Disclaimer:** This tool is intended for educational and research purposes. Use responsibly and in compliance with GitHub's terms of service.

📄 **License:** This project is licensed under the MIT License.
