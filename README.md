# PDF Analyzer Chatbot

This project is a PDF Analyzer Chatbot that allows users to upload PDF documents and ask questions about their content. The chatbot provides concise and accurate answers based solely on the PDF content.

## Features

- Analyze PDF content and answer user questions
- Maintain factual accuracy and clarity
- Suggest alternative questions if information is not found

## Requirements

- Python 3.7+
- `gradio`
- `google-generativeai`
- `PyPDF2`

## Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/do420/pdf-analyzer-chatbot.git
   cd pdf-analyzer-chatbot

2. **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    Configure the Google API Key:

3. **Set your Google API key as an environment variable:**
    ```bash

    export GEMINI_KEY='your_google_api_key'

4. **Run the application:**
    ```bash
    python gemini-pdf-analyzer.py

## Usage
- Upload a PDF document using the interface.
- Ask questions about the uploaded PDF content in the chat interface.
- Receive responses based on the PDF content.

## License
This project is licensed under the MIT License.



