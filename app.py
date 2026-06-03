from flask import Flask, render_template, request
import joblib

app = Flask(__name__, template_folder="web", static_folder="web")

model = joblib.load("model.pkl")

@app.route("/", methods=["GET","POST"])
def home():
    result=None
    bmi=None

    if request.method=="POST":
        age=int(request.form["age"])
        gender=int(request.form["gender"])
        weight=float(request.form["weight"])
        height=float(request.form["height"])
        activity=int(request.form["activity"])
        goal=int(request.form["goal"])

        pred=model.predict([[age,gender,weight,height,activity,goal]])[0]

        bmi=round(weight/((height/100)**2),2)

        result={
            "calories": round(pred[0]),
            "protein": round(pred[1]),
            "carbs": round(pred[2]),
            "fat": round(pred[3])
        }

    return render_template("index.html", result=result, bmi=bmi)

if __name__=="__main__":
    app.run(host="0.0.0.0", port=5000)
