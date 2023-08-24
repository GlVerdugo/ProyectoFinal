# PROJECT: HEART DIASEASE PREDICTION

## Produced by
Student: Guadalupe López Verdugo
ID:A01688491

## Introduction of the Project

In this project, you will learn about the basics of ML, how to apply it automatically, best practices, and the fundamental tools for developing software in the field of MLOps.

MLOps is a set of practices that combines software development, operations, and data science to automate and manage the entire lifecycle of machine learning models. This can save time and resources, and allow ML teams to focus on more strategic tasks.

## About the Project
The overall goal of this project is to create a robust and reproducible MLOps workflow for developing, training, and deploying machine learning models. In particular, we will build a KNN classification model to predict heart disease. KNN is a simple but powerful machine learning algorithm that can be used to classify data points into two or more categories. In this project, we will use KNN to classify patients with or without heart disease based on their medical characteristics..

## Explanation of the variables of the dataset
1. HeartDisease : Respondents that have ever reported having coronary heart disease (CHD) or myocardial infarction (MI).
2. BMI : Body Mass Index (BMI).
3. Smoking : Have you smoked at least 100 cigarettes in your entire life? ( The answer Yes or No ).
4. AlcoholDrinking : Heavy drinkers (adult men having more than 14 drinks per week and adult women having more than 7 drinks per week).
5. Stroke : (Ever told) (you had) a stroke?
6. PhysicalHealth : Now thinking about your physical health, which includes physical illness and injury, for how many days during the past 30 days was your physical health not good? (0-30 days).
7. MentalHealth : Thinking about your mental health, for how many days during the past 30 days was your mental health not good? (0-30 days).
8. DiffWalking : Do you have serious difficulty walking or climbing stairs?
9. Sex : Are you male or female?
10. AgeCategory: Fourteen-level age category.
11. Race : Imputed race/ethnicity value.
12. Diabetic : (Ever told) (you had) diabetes?
13. PhysicalActivity : Adults who reported doing physical activity or exercise during the past 30 days other than their regular job.
14. GenHealth : Would you say that in general your health is...
15. SleepTime : On average, how many hours of sleep do you get in a 24-hour period?
16. Asthma : (Ever told) (you had) asthma?
17. KidneyDisease : Not including kidney stones, bladder infection or incontinence, were you ever told you had kidney disease?
18. SkinCancer : (Ever told) (you had) skin cancer?

T
### Baseline

This MLOps project focuses on demonstrating the implementation of a complete workflow ranging from data preparation to exposing a local web service to making predictions using a linear regression model. The chosen data set is heart disease, which contains information on heart disease, health variables are included to predict whether or not the patient might have heart disease.

The project includes: software development, good practices, REST API and deployment of models using tools such as Docker and Docker Compose, which are essential to be able to bring a machine learning model into a productive environment. The project has focused on implementing the best practices of Continuous Integration, which allows to be able to evolve the code quickly, efficiently and with excellent guidelines.


### Links to experiments like notebooks


In the following link you will find the analysis and exploration of the data:

* [ Exploring-data-heartdisease.ipynb](docs/notebooks/heart-disease-prediction.ipynb)


## Setup

### Python version and packages to install

* Change the directory to the root folder.

* Create a virtual environment with Python 3.10:

Windows
 1.Run the following command to install the virtual environment: 
    py3.10 -m venv venv310

 2.Activate the virtual environment: Go to the SCRIPT folder and run the file .\activate:

 3.Once the virtual environment is activated, you can install the packages necessary for machine learning by running the following command (you need a requierement.txt file):
    pip install -r requirements.txt


## Model training from a main file

To train the Logistic Model:

KPIS: ![KPIS](docs/imgs/kpis_results.png)
Results: ![Results](docs/imgs/docs/imgs/kpis_results.png)
Model saved in ./models/KNeighbors_Classifier_output.pkl

## Usage

### Individual Fastapi and Use Deployment

* Run the next command to start the Titanic API locally

    ```bash
    uvicorn itesm_mlops_project.api.main:app --reload
    ```

#### Checking endpoints

1. Access `http://127.0.0.1:8000/`, you will see a message like this `"Titanic is all ready to go!"`
2. Access `http://127.0.0.1:8000/docs`, the browser will display something like this:
![FastAPI Docs](docs/imgs/fast-api-docs.png)
3. Try running the following predictions with the endpoint by writing the following values:
    * **Prediction 1**  
        Request body

        ```bash
        {
        "pclass_nan": 0,
        "age_nan": 0,
        "sibsp_nan": 0,
        "parch_nan": 0,
        "fare_nan": 0,
        "sex_male": 1,
        "cabin_Missing": 1,
        "cabin_rare": 0,
        "embarked_Q": 1,
        "embarked_S": 0,
        "title_Mr": 1,
        "title_Mrs": 0,
        "title_rar": 0
        }
        ```

        Response body
        The output will be:

        ```bash
        "Resultado predicción: [0]"
        ```

    * **Prediction 2**  
        Request body

        ```bash
         {
            "pclass_nan": 0,
            "age_nan": 0,
            "sibsp_nan": 1,
            "parch_nan": 0,
            "fare_nan": 0,
            "sex_male": 0,
            "cabin_Missing": 0,
            "cabin_rare": 0,
            "embarked_Q": 1,
            "embarked_S": 0,
            "title_Mr": 1,
            "title_Mrs": 0,
            "title_rar": 0
        }
        ```

        Response body
        The output will be:

        ```bash
        "Resultado predicción: [1]"
        ```

### Individual deployment of the API with Docker and usage

#### Build the image

* Ensure you are in the `itesm-mlops-project/` directory (root folder).
* Run the following code to build the image:

    ```bash
    docker build -t titanic-image ./itesm_mlops_project/app/
    ```

* Inspect the image created by running this command:

    ```bash
    docker images
    ```

    Output:

    ```bash
    REPOSITORY      TAG       IMAGE ID       CREATED       SIZE
    titanic-image   latest    bb48551cf542   2 hours ago   500MB
    ```

#### Run Titanic REST API

1. Run the next command to start the `titanic-image` image in a container.

    ```bash
    docker run -d --rm --name titanic-c -p 8000:8000 titanic-image
    ```

2. Check the container running.

    ```bash
    docker ps -a
    ```

    Output:

    ```bash
    CONTAINER ID   IMAGE           COMMAND                  CREATED          STATUS          PORTS                    NAMES
    53d78fb5223f   titanic-image   "uvicorn main:app --…"   19 seconds ago   Up 18 seconds   0.0.0.0:8000->8000/tcp   titanic-c
    ```

#### Checking endpoints for app

1. Access `http://127.0.0.1:8000/`, and you will see a message like this `"Titanic classifier is all ready to go!"`
2. A file called `main_api.log` will be created automatically inside the container. We will inspect it below.
3. Access `http://127.0.0.1:8000/docs`, the browser will display something like this:
    ![FastAPI Docs](docs/imgs/fast-api-docs.png)

4. Try running the following predictions with the endpoint by writing the following values:
    * **Prediction 1**  
        Request body

        ```bash
        {
        "pclass_nan": 0,
        "age_nan": 0,
        "sibsp_nan": 0,
        "parch_nan": 0,
        "fare_nan": 0,
        "sex_male": 1,
        "cabin_Missing": 1,
        "cabin_rare": 0,
        "embarked_Q": 1,
        "embarked_S": 0,
        "title_Mr": 1,
        "title_Mrs": 0,
        "title_rar": 0
        }
        ```

        Response body
        The output will be:

        ```bash
        "Resultado predicción: [0]"
        ```

        ![Prediction 1](docs/imgs/prediction-1.png)

    * **Prediction 2**  
        Request body

        ```bash
         {
            "pclass_nan": 0,
            "age_nan": 0,
            "sibsp_nan": 1,
            "parch_nan": 0,
            "fare_nan": 0,
            "sex_male": 0,
            "cabin_Missing": 0,
            "cabin_rare": 0,
            "embarked_Q": 1,
            "embarked_S": 0,
            "title_Mr": 1,
            "title_Mrs": 0,
            "title_rar": 0
        }
        ```

        Response body
        The output will be:

        ```bash
        "Resultado predicción: [1]"
        ```

        ![Prediction 2](docs/imgs/prediction-2.png)

#### Opening the logs

1. Run the command

    ```bash
    docker exec -it titanic-c bash
    ```

    Output:

    ```bash
    root@53d78fb5223f:/# 
    ```

2. Check the existing files:

    ```bash
    ls
    ```

    Output:

    ```bash
    Dockerfile   bin   etc   main.py       ml_models  opt        requirements.txt  sbin  tmp README.md    boot  home  main_api.log  mnt    predictor  root   srv   usr __pycache__  dev   lib   media         models     proc       run     sys   var
    ```

3. Open the file `main_api.log` and inspect the logs with this command:

    ```bash
    vim main_api.log
    ```

    Output:

    ```log
    2023-08-21 22:27:33,132:main:main:INFO:Titanic classifier is all ready to go!
    2023-08-21 22:30:18,810:main:main:INFO:Input values: [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 0.0]]
    2023-08-21 22:30:18,811:main:main:INFO:Resultado predicción: [0]
    2023-08-21 22:31:42,424:main:main:INFO:Input values: [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0, 0.0, 0.0]]
    2023-08-21 22:31:42,426:main:main:INFO:Resultado predicción: [1]

    ```

4. Copy the logs to the root folder:

    ```bash
    docker cp titanic-c:/main_api.log .
    ```

    Output:

    ```bash
    Successfully copied 2.05kB to .../itesm-mlops-project/.
    ```

#### Delete container and image

* Stop the container:

    ```bash
    docker stop titanic-c
    ```

* Verify it was deleted

    ```bash
    docker ps -a
    ```

    Output:

    ```bash
    CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
    ```

* Delete the image

    ```bash
    docker rmi titanic-image
    ```

    Output:

    ```bash
    Deleted: sha256:bb48551cf5423bad83617ad54a8194501aebbc8f3ebb767de62862100d4e7fd2
    ```

### Complete deployment of all containers with Docker Compose and usage

#### Create the network

First, create the network AIService by running this command:

```bash
docker network create AIservice
```

#### Run Docker Compose

* Ensure you are in the directory where the docker-compose.yml file is located

* Run the next command to start the App and Frontend APIs

    ```bash
    docker-compose -f itesm_mlops_project/docker-compose.yml up --build
    ```

    You will see something like this:

    ```bash
    Use 'docker scan' to run Snyk tests against images to find vulnerabilities and learn how to fix them
    Creating itesm_mlops_project-app-1 ... done
    Creating itesm_mlops_project-frontend-1 ... done
    itesm_mlops_project-app-1       | INFO:     Will watch for changes in these directories: ['/']
    itesm_mlops_project-app-1       | INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
    itesm_mlops_project-app-1       | INFO:     Started reloader process [1] using StatReload
    itesm_mlops_project-frontend-1  | INFO:     Will watch for changes in these directories: ['/']
    itesm_mlops_project-frontend-1  | INFO:     Uvicorn running on http://0.0.0.0:3000 (Press CTRL+C to quit)
    itesm_mlops_project-frontend-1  | INFO:     Started reloader process [1] using StatReload
    itesm_mlops_project-app-1       | INFO:     Started server process [8]
    itesm_mlops_project-app-1       | INFO:     Waiting for application startup.
    itesm_mlops_project-app-1       | INFO:     Application startup complete.
    itesm_mlops_project-frontend-1  | INFO:     Started server process [9]
    itesm_mlops_project-frontend-1  | INFO:     Waiting for application startup.
    itesm_mlops_project-frontend-1  | INFO:     Application startup complete.
    ```

#### Checking endpoints in Frontend

1. Access `http://127.0.0.1:3000/`, and you will see a message like this `"Front-end is all ready to go!"`
2. A file called `frontend.log` will be created automatically inside the container. We will inspect it below.
3. Access `http://127.0.0.1:3000/docs`, the browser will display something like this:
    ![Frontend Docs](docs/imgs/frontend-1.png)

4. Try running the following predictions with the endpoint `classify` by writing the following values:
    * **Prediction 1**  
        Request body

        ```bash
        {
        "pclass_nan": 0,
        "age_nan": 0,
        "sibsp_nan": 0,
        "parch_nan": 0,
        "fare_nan": 0,
        "sex_male": 1,
        "cabin_Missing": 1,
        "cabin_rare": 0,
        "embarked_Q": 1,
        "embarked_S": 0,
        "title_Mr": 1,
        "title_Mrs": 0,
        "title_rar": 0
        }
        ```

        Response body
        The output will be:

        ```bash
        "Resultado predicción: [0]"
        ```

        ![Frontend Prediction 1](docs/imgs/frontend-prediction-1.png)

    * **Prediction 2**  
        Request body

        ```bash
         {
            "pclass_nan": 0,
            "age_nan": 0,
            "sibsp_nan": 1,
            "parch_nan": 0,
            "fare_nan": 0,
            "sex_male": 0,
            "cabin_Missing": 0,
            "cabin_rare": 0,
            "embarked_Q": 1,
            "embarked_S": 0,
            "title_Mr": 1,
            "title_Mrs": 0,
            "title_rar": 0
        }
        ```

        Response body
        The output will be:

        ```bash
        "Resultado predicción: [1]"
        ```

        ![Frontend Prediction 2](docs/imgs/frontend-prediction-2.png)

#### Opening the logs in Frontend

Open a new terminal, and execute the following commands:

1. Copy the `frontend` logs to the root folder:

    ```bash
    docker cp itesm_mlops_project-frontend-1:/frontend.log .
    ```

    Output:

    ```bash
    Successfully copied 3.12kB to .../itesm-mlops-project/.
    ```

2. You can inspect the logs and see something similar to this:

    ```bash
    INFO: 2023-08-21 23:42:00,057|main|Front-end is all ready to go!
    INFO: 2023-08-21 23:45:04,575|main|Front-end is all ready to go!
    DEBUG: 2023-08-21 23:45:43,724|main|Incoming input in the front end: {'pclass_nan': 0, 'age_nan': 0, 'sibsp_nan': 0, 'parch_nan': 0, 'fare_nan': 0, 'sex_male': 1, 'cabin_Missing': 1, 'cabin_rare': 0, 'embarked_Q': 1, 'embarked_S': 0, 'title_Mr': 1, 'title_Mrs': 0, 'title_rar': 0}
    DEBUG: 2023-08-21 23:45:43,742|main|Prediction: "Resultado predicción: [0]"
    DEBUG: 2023-08-21 23:46:47,024|main|Incoming input in the front end: {'pclass_nan': 0, 'age_nan': 0, 'sibsp_nan': 1, 'parch_nan': 0, 'fare_nan': 0, 'sex_male': 0, 'cabin_Missing': 0, 'cabin_rare': 0, 'embarked_Q': 1, 'embarked_S': 0, 'title_Mr': 1, 'title_Mrs': 0, 'title_rar': 0}
    DEBUG: 2023-08-21 23:46:47,038|main|Prediction: "Resultado predicción: [1]"
    ```

#### Opening the logs in App

Open a new terminal, and execute the following commands:

1. Copy the `app` logs to the root folder:

    ```bash
    docker cp itesm_mlops_project-app-1:/main_api.log .
    ```

    Output:

    ```bash
    Successfully copied 2.56kB to .../itesm-mlops-project/.
    ```

2. You can inspect the logs and see something similar to this:

    ```bash
    2023-08-21 23:45:43,738:main:main:INFO:Input values: [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 0.0]]
    2023-08-21 23:45:43,740:main:main:INFO:Resultado predicción: [0]
    2023-08-21 23:46:47,034:main:main:INFO:Input values: [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0, 0.0, 0.0]]
    2023-08-21 23:46:47,036:main:main:INFO:Resultado predicción: [1]
    ```

### Delete the containers with Docker Compose

1. Stop the containers that have previously been launched with `docker-compose up`.

    ```bash
    docker-compose -f itesm_mlops_project/docker-compose.yml stop 
    ```

    Output:

    ```bash
    [+] Stopping 2/2
    ✔ Container itesm_mlops_project-frontend-1  Stopped                           0.3s 
    ✔ Container itesm_mlops_project-app-1       Stopped                           0.4s 
    ```

2. Delete the containers stopped from the stage.

    ```bash
    docker-compose -f itesm_mlops_project/docker-compose.yml rm
    ```

    Output:

    ```bash
    ? Going to remove itesm_mlops_project-frontend-1, itesm_mlops_project-app-1 Yes
    [+] Removing 2/0
    ✔ Container itesm_mlops_project-app-1       Removed                           0.0s 
    ✔ Container itesm_mlops_project-frontend-1  Removed                           0.0s 
    ```

## Resources

Here you will find information about this project and more.

### Information sources

* [MNA - Master in Applied Artificial Intelligence](https://learn.maestriasydiplomados.tec.mx/pos-programa-mna-v-)
* [ITESM MLOps Course GitHub Repository](https://github.com/carloslme/itesm-mlops)

## Contact information

* **Credits**

    ------------

  * **Development Lead**

    * Carlos Mejia <carloslmescom@gmail.com>
    * [GitHub Profile](https://github.com/carloslme/)
    * [LinkedIn](https://www.linkedin.com/in/carloslme/)

* **Contributors**

------------

None yet. Why not be the first?
