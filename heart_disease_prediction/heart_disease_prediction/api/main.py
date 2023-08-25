import logging
import os
import sys

# Add the parent directory to sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(parent_dir)

from fastapi import FastAPI
from starlette.responses import JSONResponse

from predictor.predict import ModelPredictor
from api.models.models import Heartdisease

logger = logging.getLogger(__name__) # Indicamos que tome el nombre del modulo
logger.setLevel(logging.DEBUG) # Configuramos el nivel de logging

formatter = logging.Formatter('%(asctime)s:%(name)s:%(module)s:%(levelname)s:%(message)s') # Creamos el formato

file_handler = logging.FileHandler('/Users/glverdugo/Documents/Maestria/MLops/ProyectoFinal/heart_disease_prediction/heart_disease_prediction/api/main_api.log') # Indicamos el nombre del archivo

file_handler.setFormatter(formatter) # Configuramos el formato

logger.addHandler(file_handler) # Agregamos el archivo

app = FastAPI()

@app.get('/', status_code=200)
async def healthcheck():
    logger.info("Heart Diasease classifier is all ready to go!")
    return 'Heart Diasease classifier is all ready to go!'

@app.post('/predict')
def extract_name(heartdisease_features: Heartdisease):
    predictor = ModelPredictor("/Users/glverdugo/Documents/Maestria/MLops/ProyectoFinal/heart_disease_prediction/heart_disease_prediction/models/KNeighbors_Classifier_output.pkl")
    X = [heartdisease_features.BMI ,
        heartdisease_features.Smoking,
        heartdisease_features.AlcoholDrinking,
        heartdisease_features.Stroke,
        heartdisease_features.PhysicalHealth,
        heartdisease_features.MentalHealth,
        heartdisease_features.DiffWalking,
        heartdisease_features.Sex,
        heartdisease_features.Race_Asian,
        heartdisease_features.Race_Black,
        heartdisease_features.Race_Hispanic,
        heartdisease_features.Race_Other,
        heartdisease_features.Race_White,
        heartdisease_features.GenHealth_Fair,
        heartdisease_features.GenHealth_Good,
        heartdisease_features.GenHealth_Poor,
        heartdisease_features.GenHealth_Very_good,
        heartdisease_features.Diabetic,
        heartdisease_features.PhysicalActivity,
        heartdisease_features.SleepTime,
        heartdisease_features.Asthma,
        heartdisease_features.KidneyDisease,
        heartdisease_features.SkinCancer]
    print(f"Input values: {[X]}")
    logger.info(f"Input values: {[X]}")
    prediction = predictor.predict([X])
    logger.info(f"Resultado predicción: {prediction}")
    return JSONResponse(f"Resultado predicción: {prediction}")
