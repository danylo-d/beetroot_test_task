from configparser import ConfigParser

from parser import parse_blocks
from exporter import CsvExporter


if __name__ == "__main__":
    config = ConfigParser()
    config.read("config.ini")

    pdf_path = config.get("Settings", "pdf_path")
    start_page = config.get("Settings", "start_page")
    csv_file = config.get("Settings", "csv_file")

    parsed_results = parse_blocks(pdf_path, int(start_page))
    exporter = CsvExporter(parsed_results, csv_file)
    exporter.export_to_csv()
