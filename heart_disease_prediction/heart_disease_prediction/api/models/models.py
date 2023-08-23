from pydantic import BaseModel


class Heartdisease(BaseModel):
    """
    Represents a passenger on the Heart disease with various attributes.
    
    Attributes:

    BMI (float): Placeholder for missing values in 'BMI' attribute.
    Smoking (int): Placeholder for missing values in 'Smoking' attribute.
    AlcoholDrinking (int): Placeholder for missing values in 'AlcoholDrinking' attribute.
    Stroke (int): Placeholder for missing values in 'Stroke' attribute.
    PhysicalHealth (int): Placeholder for missing values in 'PhysicalHealth' attribute.
    MentalHealth (int): Placeholder for missing values in 'MentalHealth' attribute.
    DiffWalking (int): Placeholder for missing values in 'DiffWalking' attribute.
    Sex (int): Placeholder for missing values in 'Sex' attribute.
    Race_Asian (int): Placeholder for missing values in 'Race_Asian' attribute.
    Race_Black (int): Placeholder for missing values in 'Race_Black' attribute.
    Race_Hispanic (int): Placeholder for missing values in 'Race_Hispanic' attribute.
    Race_Other (int): Placeholder for missing values in 'Race_Other' attribute.
    Race_White (int): Placeholder for missing values in 'Race_White' attribute.
    GenHealth_Fair (int): Placeholder for missing values in 'GenHealth_Fair' attribute.
    GenHealth_Good (int): Placeholder for missing values in 'GenHealth_Good' attribute.
    GenHealth_Poor (int): Placeholder for missing values in 'GenHealth_Poor' attribute.
    GenHealth_Very_good (int): Placeholder for missing values in 'GenHealth_Very_good' attribute.
    Diabetic (int): Placeholder for missing values in 'Diabetic' attribute.
    PhysicalActivity (int): Placeholder for missing values in 'PhysicalActivity' attribute.
    SleepTime (int): Placeholder for missing values in 'SleepTime' attribute.
    Asthma (int): Placeholder for missing values in 'Asthma' attribute.
    KidneyDisease (int): Placeholder for missing values in 'KidneyDisease' attribute.
    SkinCancer (int): Placeholder for missing values in 'SkinCancer' attribute.
       
    """
    BMI : float
    Smoking : int
    AlcoholDrinking : int
    Stroke : int
    PhysicalHealth : int
    MentalHealth : int
    DiffWalking : int
    Sex : int
    Race_Asian : int
    Race_Black : int
    Race_Hispanic : int
    Race_Other : int
    Race_White : int
    GenHealth_Fair : int
    GenHealth_Good : int
    GenHealth_Poor : int
    GenHealth_Very_good : int
    Diabetic : int
    PhysicalActivity : int
    SleepTime : int
    Asthma : int
    KidneyDisease : int
    SkinCancer : int
    