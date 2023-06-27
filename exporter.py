import pandas as pd


class CsvExporter:
    def __init__(self, data, csv_path):
        self.data = data
        self.csv_path = csv_path

    def export_to_csv(self):
        df = pd.DataFrame(
            [(k, *v.values()) for c_r in self.data for k, v in c_r.items()],
            columns=[
                "Name (incl. titles if any mentioned)",
                "Affiliation(s) Name(s)",
                "Person's Location",
                "Session Name",
                "Topic Title",
                "Presentation Abstract",
            ],
        )
        df.to_csv(self.csv_path, index=False)
