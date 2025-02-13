import pickle
import gradio as gr

# Load the saved models
heart_disease_model = pickle.load(open(r'E:\sathvik projects\ml projects\Multiple disease-20241104T162302Z-001\Multiple disease\heart_disease_model.sav', 'rb'))
parkinsons_model = pickle.load(open(r'E:\sathvik projects\ml projects\Multiple disease-20241104T162302Z-001\Multiple disease\parkinsons_model.sav', 'rb'))

# Define the prediction functions
def predict_heart_disease(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal):
    # Convert `sex` to numeric (0 for female, 1 for male)
    sex_numeric = 0 if sex == 'female' else 1
    input_data = [[age, sex_numeric, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]]
    prediction = heart_disease_model.predict(input_data)[0]
    return 'The person has heart disease' if prediction == 1 else 'The person does not have heart disease'

def predict_parkinsons(fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE):
    input_data = [[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]]
    prediction = parkinsons_model.predict(input_data)[0]
    return "The person has Parkinson's disease" if prediction == 1 else "The person does not have Parkinson's disease"

# Display form based on disease selection
def update_inputs(disease):
    if disease == "Heart Disease":
        return gr.update(visible=True), gr.update(visible=False)
    elif disease == "Parkinson's":
        return gr.update(visible=False), gr.update(visible=True)

# Create form for each disease
with gr.Blocks() as demo:
    # Title
    gr.Markdown("# Multiple Disease Prediction")

    # Disease dropdown
    disease_dropdown = gr.Dropdown(choices=["Heart Disease", "Parkinson's"], label="Select Disease", value="Heart Disease")

    # Heart Disease form
    with gr.Group(visible=True) as heart_disease_form:
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
        heart_disease_button = gr.Button("Submit")
        heart_disease_output = gr.Textbox(label="Heart Disease Prediction Result")

    # Parkinson's form
    with gr.Group(visible=False) as parkinsons_form:
        fo = gr.Number(label="MDVP:Fo(Hz)")
        fhi = gr.Number(label="MDVP:Fhi(Hz)")
        flo = gr.Number(label="MDVP:Flo(Hz)")
        jitter_percent = gr.Number(label="MDVP:Jitter(%)")
        jitter_abs = gr.Number(label="MDVP:Jitter(Abs)")
        rap = gr.Number(label="MDVP:RAP")
        ppq = gr.Number(label="MDVP:PPQ")
        ddp = gr.Number(label="Jitter:DDP")
        shimmer = gr.Number(label="MDVP:Shimmer")
        shimmer_db = gr.Number(label="MDVP:Shimmer(dB)")
        apq3 = gr.Number(label="Shimmer:APQ3")
        apq5 = gr.Number(label="Shimmer:APQ5")
        apq = gr.Number(label="MDVP:APQ")
        dda = gr.Number(label="Shimmer:DDA")
        nhr = gr.Number(label="NHR")
        hnr = gr.Number(label="HNR")
        rpde = gr.Number(label="RPDE")
        dfa = gr.Number(label="DFA")
        spread1 = gr.Number(label="Spread1")
        spread2 = gr.Number(label="Spread2")
        d2 = gr.Number(label="D2")
        ppe = gr.Number(label="PPE")
        parkinsons_button = gr.Button("Submit")
        parkinsons_output = gr.Textbox(label="Parkinson's Prediction Result")

    # Event handling
    heart_disease_button.click(predict_heart_disease,
                               inputs=[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal],
                               outputs=heart_disease_output)

    parkinsons_button.click(predict_parkinsons,
                            inputs=[fo, fhi, flo, jitter_percent, jitter_abs, rap, ppq, ddp, shimmer, shimmer_db, apq3, apq5, apq, dda, nhr, hnr, rpde, dfa, spread1, spread2, d2, ppe],
                            outputs=parkinsons_output)

    # Update input visibility based on disease selection
    disease_dropdown.change(update_inputs, inputs=disease_dropdown,
                            outputs=[heart_disease_form, parkinsons_form])

# Launch the interface
demo.launch()
