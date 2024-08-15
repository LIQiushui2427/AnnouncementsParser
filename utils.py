import os
import json
from PyPDF2 import PdfReader
from pdf2image import convert_from_path
import pytesseract
from openai import OpenAI

from dotenv import load_dotenv
load_dotenv()


def _build_system_message():
    pass

def extract_text_from_file(file):
    # Determine the file extension
    file_extension = os.path.splitext(file)[1]

    # Initialize the text content
    text_content = ""
    # Read the file content based on the file type
    if file_extension == ".pdf":
        with open(file, "rb") as fileobj:
            reader = PdfReader(fileobj)
            for page in reader.pages:
                text_content += page.extract_text()

        # if the text_content is small, that means we need to use OCR
        if len(text_content) < 20:
            images = convert_from_path(file)
            for image in images:
                text_content += pytesseract.image_to_string(image)
    
    elif file_extension == ".docx":
        # Use python-docx library to read the content
        pass

    return text_content

def parse_content(text_content, prompts):
    print("Parsing content...")
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
    
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
          messages=[
            {
            "role": "system",
            "content": [
                {
                "type": "text",
                "text": "You are a professional company report parser and will be provided with text content extracted from a annual report file. Your task is to return nothing else but clean, accurate JSON formatted data with: # - Company Name\n# - Report Year \n# - Region\n# , and all variables and questions in the prompts. The parsed information will be saved in a json file in the output_dir with name-format: {company_name}_{report_type}_{report_year}.json."
                }
            ]
            },
            {
            "role": "user",
            "content": [
                {
                "type": "text",
                "text": "Hi, please parse the following text content and provide the requested information in your answer. \
                please finish remaining questions/task after reading the report, whose specification is all in the prompts.json files. \
                Your answer should strictly follow the instructions in the prompt, if there is no choice, please give 1 if the answer is yes and 0 if the answer is no. \
                The parsed information will be saved in a json file in the output_dir with name-format: {company_name}_{report_type}_{report_year}.json. " + "\n\n Texts: " + text_content + "\n\n Prompts: " + prompts
                }
            ]
            }
        ],
        response_format= { "type":"json_object" }
    )

    return json.loads(completion.choices[0].message.content)
