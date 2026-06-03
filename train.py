import pandas as pd
import joblib
from sklearn.ensemble import RandomForestRegressor

df = pd.read_csv("data.csv")

X=df[["Age","Gender","Weight","Height","Activity","Goal"]]
y=df[["Calories","Protein","Carbs","Fat"]]

model=RandomForestRegressor(n_estimators=300,random_state=42)
model.fit(X,y)

joblib.dump(model,"model.pkl")
print("Model saved as model.pkl")
