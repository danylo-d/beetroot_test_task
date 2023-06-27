# PDF Parser and CSV Exporter

This project provides a Python script to parse a PDF document and extract specific information from it. The extracted data is then exported to a CSV file for further analysis or usage.

## Requirements

- Python 3.x
- `fitz` library (PyMuPDF): To parse the PDF document.
- `pandas` library: To export the extracted data to a CSV file.

## Installation

1. Clone the repository to your local machine or download the source code files.
   ```
   git clone https://github.com/danylo-d/beetroot_test_task.git
   ```
2. Install the required dependencies by running the following command:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Place the PDF document you want to parse in the same directory as the project files.
2. Modify the `config.ini` file according to your requirements:

   - Set the `pdf_path` option to the filename of the PDF document.
   - Set the `start_page` option to the page number from which you want to start parsing.
   - Set the `csv_file` option to the desired filename for the exported CSV file.

3. Run the `main.py` script using the following command:
   ```
   python main.py
   ```

4. The script will parse the PDF document starting from the specified page and extract the relevant information.
5. Once the parsing is complete, the extracted data will be exported to the specified CSV file.
6. The CSV file will contain the following columns:

   - `Name (incl. titles if any mentioned)`: Name of the person including any titles mentioned.
   - `Affiliation(s) Name(s)`: Name(s) of the affiliation(s).
   - `Person's Location`: Location of the person.
   - `Session Name`: Name of the session.
   - `Topic Title`: Title of the topic.
   - `Presentation Abstract`: Abstract of the presentation.

## Example

For example, let's assume we have a PDF document named "Abstract Book from the 5th World Psoriasis and Psoriatic Arthritis Conference 2018.pdf" with 100 pages. We want to parse the document starting from page 43 and export the extracted data to a CSV file named "data.csv".

We would modify the `config.ini` file as follows:

```ini
[Settings]
pdf_path = Abstract Book from the 5th World Psoriasis and Psoriatic Arthritis Conference 2018.pdf
start_page = 43
csv_file = data.csv
```

Then, we would run the `main.py` script:

```
python main.py
```

The script will parse the PDF document starting from page 43 and export the extracted data to the "data.csv" file.
