# Company annual report CLT

This is a command line tool to automatically read companies report related to climate risk disclosure from their annual reports. 
It will store the output in a file with the name company name and the year of the report. E.g. `Apple_2020.json`.
## Requirements

You need to have `python`, `pip`, `poppler-utils` and `tesseract` installed.

```
pip install -r requirements.txt
```

You might need additonal tesseract language packs per your use cases. For example,

```
sudo dnf install tesseract-langpack-chi_sim
```

You need to provide your own OpenAI API with `.env`.

## Usage

```
ResumeCLT.py [-h] --source_dir SOURCE_DIR --output_dir OUTPUT_DIR [--target_list TARGET_LIST]

Options for ResumeCLT

options:
  -h, --help            show this help message and exit
  --source_dir SOURCE_DIR
                        Directory where the report files are stored
  --output_dir OUTPUT_DIR
                        Directory where the output files will be stored
  --target_list TARGET_LIST
                        File containing the list of target schools
```

Run provided test case with:

```
bash run.sh
```

## License
