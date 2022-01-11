import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

df=pd.read_excel('D:\GIT\Combined-Cycle-Power-Plant\Folds5x2_pp.xlsx')
Temprature=np.array(df['AT'].values).reshape(-1,1)
ExhaustVaccum=np.array(df['V'].values).reshape(-1,1)
AmbientPressure=np.array(df['AP'].values).reshape(-1,1)
RelativeHumidity=np.array(df['RH'].values).reshape(-1,1)
PowerOutput=np.array(df['PE'].values).reshape(-1,1)

Attributes=np.concatenate((Temprature, ExhaustVaccum, AmbientPressure, RelativeHumidity), axis=1)

model=LinearRegression()
model.fit(Attributes, PowerOutput)

Score=model.score(Attributes, PowerOutput)
print("Accuracy: ", Score*100, "Percent")

UserTemprature=float(input("Enter The Ambient Temprature (Degrees): "))
UserExhaustVaccum=float(input("Enter The Exhaust Vaccum (cm of Hg): "))
UserAmbientPressure=float(input("Enter The Ambient Pressure (millibar): "))
UserRelativeHumidity=float(input("Enter The Relative Humidity (%): "))

Prediction= model.predict([[UserTemprature, UserExhaustVaccum, UserAmbientPressure, UserRelativeHumidity]])
print("The Expected Power Output Will be:", round(Prediction[0][0],2), "MW")