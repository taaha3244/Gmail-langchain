# Gmail Automation with LangChain and OpenAI

This project leverages the capabilities of LangChain and OpenAI to automate interactions within Gmail, enhancing productivity and efficiency in managing email communications.

## Prerequisites

Before you begin, ensure you have the following:
- Python 3.8 or higher
- Access to Google Cloud Platform (GCP)
- An OpenAI API key

## Setup

### Clone the Repository

Start by cloning this repository to your local machine:

```bash
git clone https://github.com/taaha3244/Gmail-langchain.git
```

### Environment Variables

Create a .env file in the root directory of your project and add the following environment variables:
```bash
OPENAI_API_KEY='your_openai_api_key_here'
```
### Credentials.json

Using GCP get your gmail API credentials and save them to a 'credentials.json' file in the root folder

how to get credentials? : https://developers.google.com/gmail/api/quickstart/python#authorize_credentials_for_a_desktop_application

### Requirements
Install requirements with
```bash
pip install -r requirements.txt
```
### Usage
To run the project, execute the following commands in the root directory:

```bash
python -m your_script_name
```
