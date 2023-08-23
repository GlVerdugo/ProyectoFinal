"""Main module."""
import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(parent_dir)

from load.load_data import DataRetriever
from train.train_data import HeartDiseasePipeline
import pandas as pd
from sklearn.model_selection import train_test_split
import joblib
import os
from sklearn.metrics import accuracy_score, roc_auc_score

from utilities import custom_logging

logger = custom_logging.CustomLogging(__name__)


DATASETS_DIR = './data/'
URL = 'C:/Users/glverdugo/Documents/Maestria/MLops/Proyecto/heart_disease_prediction/heart_disease_prediction/data/heart_2020_cleanedd.csv'

RETRIEVED_DATA = 'heart_2020_cleanedd.csv'


SEED_SPLIT = 404
TRAIN_DATA_FILE = DATASETS_DIR + 'train.csv'
TEST_DATA_FILE  = DATASETS_DIR + 'test.csv'


TARGET = 'HeartDisease'
FEATURES = ['BMI','Smoking','AlcoholDrinking','Stroke','PhysicalHealth','MentalHealth','DiffWalking','Sex','Race',
             'Diabetic','PhysicalActivity','GenHealth','SleepTime','Asthma',
            'KidneyDisease','SkinCancer' ]

CATEGORICAL_VARS = ['Race','GenHealth']

NUMERICAL_VARS = ['BMI','Smoking','AlcoholDrinking','Stroke','PhysicalHealth','MentalHealth','DiffWalking','Sex',
             'Diabetic','PhysicalActivity','SleepTime','Asthma',
            'KidneyDisease','SkinCancer' ]



SEED_MODEL = 404

SELECTED_FEATURES = ['BMI','Smoking','AlcoholDrinking','Stroke','PhysicalHealth','MentalHealth','DiffWalking','Sex',
                     'Race','Race_Asian','Race_Black','Race_Hispanic','Race_Other','Race_White','GenHealth','GenHealth_Fair',
                    'GenHealth_Good','GenHealth_Poor','GenHealth_Very good','Diabetic','PhysicalActivity','SleepTime',
                    'Asthma','KidneyDisease','SkinCancer']

TRAINED_MODEL_DIR = './models/'
PIPELINE_NAME = 'KNeighbors_Classifier'
PIPELINE_SAVE_FILE = f'{PIPELINE_NAME}_output.pkl'


if __name__ == "__main__":
    
    print(os.getcwd())
    os.chdir('C:/Users/glverdugo/Documents/Maestria/MLops/Proyecto/heart_disease_prediction/heart_disease_prediction')
    # Retrieve data
    data_retriever = DataRetriever(URL, DATASETS_DIR)
    result = data_retriever.retrieve_data()
    #print(result)
    
    # Instantiate the HeartDiseasePipeline class
    HeartDisease_data_pipeline = HeartDiseasePipeline(seed_model=SEED_MODEL,
                                                numerical_vars=NUMERICAL_VARS,
                                                categorical_vars=CATEGORICAL_VARS, 
                                                selected_features=SELECTED_FEATURES)
    logger.info("Pipeline Transformations")

    # Read data
    df = pd.read_csv(DATASETS_DIR + RETRIEVED_DATA)
    logger.info("Loading data")

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
                                                        df.drop(TARGET, axis=1),
                                                        df[TARGET],
                                                        test_size=0.2,
                                                        random_state=404
                                                   )
    
    logger.info("Split data")
    KNeighborsClassifier_model = HeartDisease_data_pipeline.fit_KNeighborsClassifier(X_train, y_train)
    
    X_test = HeartDisease_data_pipeline.PIPELINE.fit_transform(X_test)
    y_pred = KNeighborsClassifier_model.predict(X_test)
    
    class_pred = KNeighborsClassifier_model.predict(X_test)
    proba_pred = KNeighborsClassifier_model.predict_proba(X_test)[:,1]
    print(f'test roc-auc : {roc_auc_score(y_test, proba_pred)}')
    print(f'test accuracy: {accuracy_score(y_test, class_pred)}')
    logger.info("Split training and test data")

    # # Save the model using joblib
    save_path = TRAINED_MODEL_DIR + PIPELINE_SAVE_FILE
    joblib.dump(KNeighborsClassifier_model, save_path)
    print(f"Model saved in {save_path}")
    logger.info(f"Model saved in {save_path}")
    