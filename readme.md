# Company Announcement CLT (Climate-Related Tool)

## Introduction

This command line tool is designed to automate the extraction of climate risk disclosure information from annual Announcements of U.S. manufacturing companies classified under SIC Codes 2000-3999. The tool processes PDF Announcements, extracts relevant data using advanced OCR and NLP techniques, and outputs the information in a structured JSON format. This README provides detailed instructions on setting up and using the tool effectively.

## Project Structure

The project is organized as follows:

- `Data/`: Default directory for storing input PDFs and output JSON files.
- `requirements.txt`: Lists all Python dependencies.

## Requirements

### Software Requirements

- **Python 3.8+**: The primary programming language used.
- **pip**: Python's package installer.
- **Poppler-utils**: Provides utilities to work with PDF files.
- **Tesseract-OCR**: Converts images in PDFs to text.

### Installation Instructions

#### Python and pip

Ensure Python and pip are installed. You can download Python from the official website and it typically comes with pip.

### Poppler-utils

For Debian-based systems, install using:

```bash
sudo apt-get install poppler-utils
```

For Red Hat-based systems, use:

```bash
sudo yum install poppler-utils
```

Tesseract-OCR
To install Tesseract on Ubuntu:

```bash
sudo apt install tesseract-ocr
```

To install additional language packs such as for Simplified Chinese:

```bash
sudo apt install tesseract-ocr-chi-sim
```

### Installing Python Dependencies

Navigate to the project directory and run:

```bash
pip install -r requirements.txt
```

## Configuration

API Keys
Store your OpenAI API key in a .env file within the project's root directory to ensure the tool can access ChatGPT services for text analysis. The file should look like this:

```bash
OPENAI_API_KEY='your-api-key-here'
```

## Usage Instructions

### Running the Tool

To use the tool, execute the following command from the root of your project directory:

```bash
python src/ReportAnalyseCLT.py --source_dir path/to/input --output_dir path/to/output
```

## Command Line Arguments

--source_dir: Specifies the directory containing the PDF Announcements.
--output_dir: Specifies where the JSON output files should be saved.
--target_list (optional): A file containing a list of specific companies to process.

## Example Usage

```bash
python src/ReportAnalyseCLT.py --source_dir data/Announcements --output_dir data/output
```

## Output Format

The output JSON files will be named in the format CompanyName_Year.json and will contain structured data extracted from the Announcements, including financial figures and disclosure details.

## Troubleshooting

### Common Issues

**Dependency Errors:** Ensure all dependencies are correctly installed as per the instructions.
**OCR Accuracy:** Poor quality PDFs may result in inaccurate text extraction. Consider manually verifying critical data.
**Help:** For additional help, use the -h option with the command to display detailed usage instructions:

```bash
python src/ReportAnalyseCLT.py -h
```

## License

This tool is released under the MIT License.



