import joblib
from pathlib import Path
import pandas as pd

class PredictController:

    def __init__(self):
        try:
            model_path = Path(__file__).parent.parent.joinpath('models').joinpath('ml_gbm_datajud2.pkl')
            print(model_path)
            self.model = joblib.load(model_path)
        except Exception as error:
            print(f"An error occurred during prediction: {error}")
            raise error
        

    def predict(self, process_params):
        process_params = {
                "grau": float(process_params["grau"]),
                "codigo_classe": int(process_params["codigo_classe"]),
                "orgao_codigo": int(process_params["orgao_codigo"]),
                "codigo_assunto": int(process_params["codigo_assunto"]),
                "assunto_nivel1": int(process_params["assunto_nivel1"]),
                "assunto_nivel2": float(process_params["assunto_nivel2"]),
                "assunto_nivel3": float(process_params["assunto_nivel3"]),
                "assunto_nivel4": float(process_params["assunto_nivel4"]),
                "assunto_nivel5": float(process_params["assunto_nivel5"]),
                "classe_nivel1": int(process_params["classe_nivel1"]),
                "classe_nivel2": float(process_params["classe_nivel2"]),
                "classe_nivel3": float(process_params["classe_nivel3"]),
                "classe_nivel4": float(process_params["classe_nivel4"]),
                "classe_nivel5": float(process_params["classe_nivel5"]),
            }
        try:
            predict_df = pd.DataFrame([process_params])
            print(predict_df)
            prediction = self.model.predict(predict_df)
        except Exception as error:
            print(f"An error occurred during prediction: {error}")
            raise error
        
        return prediction[0]
