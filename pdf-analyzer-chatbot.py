import os
import gradio as gr
import google.generativeai as genai
import PyPDF2

# Configure Google API
GOOGLE_API_KEY = os.getenv('GEMINI_KEY')
genai.configure(api_key=GOOGLE_API_KEY)

# Initialize Gemini model
model = genai.GenerativeModel('gemini-1.5-flash', 
                            generation_config=genai.types.GenerationConfig(
                                temperature=0.7,
                                top_p=0.9,
                                top_k=40
                            ))

# System prompt
SYSTEM_PROMPT = """You are an expert PDF document analyzer with the following guidelines:

1. CONTEXT:
- Analyze ONLY the content provided in the PDF document
- Do not make assumptions or add external knowledge
- If information is not found in the document, explain this and suggest 2-3 relevant questions that could be answered based on the document's actual content
2. RESPONSE FORMAT:
- Provide clear, concise answers
- Use bullet points for complex explanations
- Quote relevant text segments when appropriate
- Structure responses logically

3. ACCURACY:
- Maintain factual accuracy based solely on the document
- Highlight any ambiguities in the source text
- Express certainty levels in your responses

4. COMPREHENSION:
- Consider the full context of the document
- Make connections between related information
- Identify key themes and main points

When information is not found:
- Clearly state that the specific information is not in the document
- Provide 2-3 alternative questions that ARE answerable from the document content
- Base suggested questions on related themes or topics that are present
Remember: Your role is to help users understand the specific PDF content through accurate analysis and clear communication while guiding them toward questions that can be answered from the available content."""

pdf_content = ""
def extract_text_from_pdf(pdf_file):
    text = ""
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

def process_pdf(pdf_file):
    global pdf_content
    try:
        pdf_content = extract_text_from_pdf(pdf_file.name)
        return "PDF successfully loaded. You can now ask questions about its content."
    except Exception as e:
        return f"Error processing PDF: {str(e)}"

def chat_with_pdf(message, history):
    if not pdf_content:
        return "Please upload a PDF file first."
    
    # Construct the prompt with context
    full_prompt = f"""Context: {pdf_content}

{SYSTEM_PROMPT}

User Question: {message}"""

    # Start chat and get response
    chat = model.start_chat(history=[])
    response = chat.send_message(full_prompt)
    return response.text
# Create Gradio interface
with gr.Blocks() as iface:
    gr.Markdown("# PDF Question Answering System")
    
    with gr.Row():
        pdf_input = gr.File(label="Upload PDF", file_types=[".pdf"])
        pdf_status = gr.Textbox(label="Status")
    
    pdf_input.upload(
        fn=process_pdf,
        inputs=[pdf_input],
        outputs=[pdf_status]
    )

    chatbot = gr.ChatInterface(
        fn=chat_with_pdf,
        title="Ask questions about the PDF", 
        description="Upload a PDF first, then ask questions about its content.",

    )
# Launch the interface
if __name__ == "__main__":
    iface.launch()

