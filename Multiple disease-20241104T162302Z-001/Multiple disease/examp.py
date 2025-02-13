import pickle
import gradio as gr

# Load the heart disease prediction model
heart_disease_model = pickle.load(open(r'E:\sathvik projects\ml projects\Multiple disease-20241104T162302Z-001\Multiple disease\heart_disease_model.sav', 'rb'))

def predict_heart_disease(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal):
    """Predict whether a person has heart disease."""
    sex_numeric = 0 if sex == 'female' else 1
    input_data = [[age, sex_numeric, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]]
    prediction = heart_disease_model.predict(input_data)[0]
    return 'The person has heart disease' if prediction == 1 else 'The person does not have heart disease'


with gr.Blocks() as demo:
    # Title
    gr.Markdown("# Heart Disease Prediction")

    # Input fields
    age = gr.Number(label="Age")
    sex = gr.Dropdown(choices=['female', 'male'], label="Sex")
    cp = gr.Number(label="Chest Pain Type (0-3)")
    trestbps = gr.Number(label="Resting Blood Pressure")
    chol = gr.Number(label="Serum Cholesterol in mg/dl")
    fbs = gr.Number(label="Fasting Blood Sugar > 120 mg/dl (1 = true, 0 = false)")
    restecg = gr.Number(label="Resting Electrocardiographic Results (0-2)")
    thalach = gr.Number(label="Maximum Heart Rate Achieved")
    exang = gr.Number(label="Exercise Induced Angina (1 = yes, 0 = no)")
    oldpeak = gr.Number(label="ST depression induced by exercise relative to rest")
    slope = gr.Number(label="Slope of the peak exercise ST segment (0-2)")
    ca = gr.Number(label="Number of major vessels (0-3) colored by fluoroscopy")
    thal = gr.Number(label="Thalassemia (3 = normal, 6 = fixed defect, 7 = reversible defect)")

   
    submit_button = gr.Button("Submit")
    output = gr.Textbox(label="Prediction Result")

    
    submit_button.click(predict_heart_disease,
                        inputs=[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal],
                        outputs=output)


demo.launch()
