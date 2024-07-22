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
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"), base_url="https://api.chatanywhere.tech/v1")
    print("API Key: ", os.environ.get("OPENAI_API_KEY"))
    
    prompts = json.loads(prompts)
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
          messages=[
            {
            "role": "system",
            "content": [
                {
                "type": "text",
                "text": "You are a professional grade company report parser and will be provided with text content extracted from a annual report file. Your task is to return nothing else but clean, accurate JSON formatted data with: # - Company Name\n# - Report Year \n# - Region\n# - All the variables in the variables dictionary\n# \
                - The parsed information will be saved in a json file in the output_dir with name-format: {company_name}_{report_year}.json \
                for the variables questions, please refer to the variables dictionary in the prompts.py file. Your answer regarding every variable should be either 0 for no or 1 for yes. "
                }
            ]
            },
            {
            "role": "user",
            "content": [
                {
                "type": "text",
                "text": text_content + str(prompts)
                }
            ]
            }
        ],
        response_format= { "type":"json_object" }
    )

    return json.loads(completion.choices[0].message.content)

def generate_filename(parsed_info, args):
    # If the school is in the target list, prepend "Matched-" to the filename

    company_name = parsed_info['company_name']
    report_year = parsed_info['report_year']
    
    filename = f'{company_name}_{report_year}'
            
    return filename