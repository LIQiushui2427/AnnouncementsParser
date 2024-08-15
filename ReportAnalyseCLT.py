# Supported file format: PDF
# This program will parse all Climare-related report presented in source_dir and
# parse out the following information:
# - Company name
# - Region
# - Report year
# - All the variables in the variables dictionary
# - The parsed information will be saved in a json file in the output_dir with name-format: {company_name}_{report_year}.json

from options import parse_args
from utils import *
import os
import json



def process_file(file, args):
    print(f'Reading Prompt file: {args.prompt_file}...')
    json_file = open(args.prompt_file)
    print(f'Processing file: {file}...')

    text_content = extract_text_from_file(file)
    print('Waiting for response from OpenAI...')
    
    parsed_info = parse_content(text_content, json_file.read())

    print('Response received.')
    print('Saving parsed information...', parsed_info.keys())
    keys = list(parsed_info.keys())
    print(keys)
    # The first key is the company name
    company_name = parsed_info[keys[0]]
    report_type = parsed_info[keys[1]]
    report_year = parsed_info[keys[2]]
    
    filename = f'{company_name}_{report_type}_{report_year}.json'
    
    # Rename the file
    
    # Save all the parsed information in a JSON file with the filename format: {company_name}_{report_year}.json
    
    with open(os.path.join(args.output_dir, filename), 'w') as f:
        json.dump(parsed_info, f)
        
    print(f'Parsed information saved in {filename}.')
    
    print(parsed_info)


def main():
    args = parse_args()
    # Check if args are valid
    if not os.path.exists(args.source_dir):
        print(f"Error: Source directory {args.source_dir} does not exist.")
        return
    if not os.path.exists(args.output_dir):
        print(f"Error: Output directory {args.output_dir} does not exist.")
        return
    # if args.target_list and not os.path.exists(args.target_list):
    #     print(f"Error: Target list file {args.target_list} does not exist.")
    #     return
    # Get all files with the following extensions: PDF, DOCX, DOC
    files = os.listdir(args.source_dir)
    files = [file for file in files if file.endswith((".pdf", ".docx", ".doc"))]
    # Process each file
    for file in files:
        file_path = os.path.join(args.source_dir, file)
        process_file(file_path, args)
    print("All files processed.")
    

if __name__ == "__main__":
    main()