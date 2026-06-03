from flask import Flask, render_template, request
import joblib

app = Flask(__name__, template_folder="web", static_folder="web")

# Load trained model
model = joblib.load("model.pkl")


@app.route("/", methods=["GET", "POST"])
def home():

    result = None
    bmi = None
    bmi_status = None
    error = None

    if request.method == "POST":

        try:
            age = int(request.form["age"])
            gender = int(request.form["gender"])
            weight = float(request.form["weight"])
            height = float(request.form["height"])
            activity = int(request.form["activity"])
            goal = int(request.form["goal"])

            # Validation
            if age <= 0 or weight <= 0 or height <= 0:
                error = "Please enter valid positive values."
            else:

                # Model prediction
                pred = model.predict([
                    [age, gender, weight, height, activity, goal]
                ])[0]

                # BMI calculation
                bmi = round(weight / ((height / 100) ** 2), 2)

                # BMI status
                if bmi < 18.5:
                    bmi_status = "Underweight"
                elif bmi < 25:
                    bmi_status = "Normal"
                elif bmi < 30:
                    bmi_status = "Overweight"
                else:
                    bmi_status = "Obese"

                # Prediction result
                result = {
                    "calories": round(pred[0]),
                    "protein": round(pred[1]),
                    "carbs": round(pred[2]),
                    "fat": round(pred[3])
                }

        except Exception as e:
            error = f"Error: {str(e)}"

    return render_template(
        "index.html",
        result=result,
        bmi=bmi,
        bmi_status=bmi_status,
        error=error
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)