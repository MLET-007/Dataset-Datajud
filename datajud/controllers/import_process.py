from fastapi import FastAPI

import pandas as pd
from pathlib import Path
from datajud.utils.carga_dados import load_data_from_datajud_api

class ImportProcessController:
    def __init__(self, engine):
        self.engine = engine

    def import_process_csv(self):
        try: 
            df = pd.read_csv(Path(__file__).parent.parent.parent / "data.csv")
            df.to_sql("processo", con=self.engine, if_exists="replace", index=False)
            print("Data imported successfully")
        except Exception as e:
            print(f"Error during data import: {e}")        

    def import_process_api(self, data):
        try:
            load_data_from_datajud_api(data['tribunal'], data['numero_processo']).to_sql("processo", con=self.engine, if_exists="replace", index=False)
            print("Data imported successfully")
        except Exception as e:
            print(f"Error during data import: {e}")
        
