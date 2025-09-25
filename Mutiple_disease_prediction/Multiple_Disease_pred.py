import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# =================== Load Models =====================
diabetes_model = pickle.load(open(
    r'C:/Users/shivu/OneDrive/Desktop/Mutiple_disease_prediction/save_Models/diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open(
    r'C:/Users/shivu/OneDrive/Desktop/Mutiple_disease_prediction/save_Models/heart_disease_model.sav', 'rb'))

parkinsons_model = pickle.load(open(
    r'C:/Users/shivu/OneDrive/Desktop/Mutiple_disease_prediction/save_Models/parkinson_model.sav', 'rb'))

# =================== Sidebar Menu =====================
with st.sidebar:
    selected = option_menu(
        'Multiple Disease Prediction System',
        ['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinsons Prediction'],
        icons=['activity', 'heart', 'person'],
        default_index=0
    )

# =================== Diabetes Prediction Page =====================
if selected == 'Diabetes Prediction':
    st.title('🩸 Diabetes Prediction using ML')
    
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        SkinThickness = st.text_input('SkinThickness value')
        DiabetesPedigreeFunction = st.text_input('DiabetesPedigreeFunction value')
    with col2:
        Glucose = st.text_input('Glucose Level')
        Insulin = st.text_input('Insulin Level')
        Age = st.text_input('Age of the Person')
    with col3:
        BloodPressure = st.text_input('BloodPressure Level')
        BMI = st.text_input('BMI value')

    diab_diagnosis = ''
    
    if st.button('Diabetes Test Result'):
        try:
            input_data = [float(Pregnancies), float(Glucose), float(BloodPressure), float(SkinThickness),
                          float(Insulin), float(BMI), float(DiabetesPedigreeFunction), float(Age)]
            
            diab_prediction = diabetes_model.predict([input_data])

            if diab_prediction[0] == 1:
                diab_diagnosis = '⚠️ The person is Diabetic'
            else:
                diab_diagnosis = '✅ The person is NOT Diabetic'

            st.success(diab_diagnosis)
        except ValueError:
            st.error("⚠️ Please enter valid numeric values for all fields.")


# =================== Heart Disease Prediction Page =====================
elif selected == 'Heart Disease Prediction':
    st.title('❤️ Heart Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')
        trestbps = st.text_input('Resting Blood Pressure')
        restecg = st.text_input('Resting ECG results (0-2)')
        slope = st.text_input('Slope of ST segment (0-2)')
    with col2:
        sex = st.text_input('Sex (1 = Male, 0 = Female)')
        chol = st.text_input('Serum Cholestoral (mg/dl)')
        thalach = st.text_input('Max Heart Rate Achieved')
        ca = st.text_input('Number of major vessels (0-3)')
    with col3:
        cp = st.text_input('Chest Pain Type (0-3)')
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl (1=True,0=False)')
        exang = st.text_input('Exercise Induced Angina (1=Yes,0=No)')
        thal = st.text_input('Thalassemia (0=normal,1=fixed defect,2=reversible)')

    heart_diagnosis = ''

    if st.button('Heart Disease Test Result'):
        try:
            input_data = [float(age), float(sex), float(cp), float(trestbps), float(chol), float(fbs),
                          float(restecg), float(thalach), float(exang), float(slope), float(ca), float(thal)]
            
            heart_prediction = heart_disease_model.predict([input_data])

            if heart_prediction[0] == 1:
                heart_diagnosis = '⚠️ The person has Heart Disease'
            else:
                heart_diagnosis = '✅ The person does NOT have Heart Disease'

            st.success(heart_diagnosis)
        except ValueError:
            st.error("⚠️ Please enter valid numeric values for all fields.")


# =================== Parkinsons Prediction Page =====================
elif selected == 'Parkinsons Prediction':
    st.title('🧠 Parkinson’s Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
        jitter_percent = st.text_input('MDVP:Jitter(%)')
        rap = st.text_input('MDVP:RAP')
        shimmer = st.text_input('MDVP:Shimmer')
        apq3 = st.text_input('Shimmer:APQ3')
        apq = st.text_input('MDVP:APQ')
        nhr = st.text_input('NHR')
        rpde = st.text_input('RPDE')
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')
        jitter_abs = st.text_input('MDVP:Jitter(Abs)')
        ppq = st.text_input('MDVP:PPQ')
        shimmer_db = st.text_input('MDVP:Shimmer(dB)')
        apq5 = st.text_input('Shimmer:APQ5')
        dda = st.text_input('Shimmer:DDA')
        hnr = st.text_input('HNR')
        dfa = st.text_input('DFA')
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')
        ddp = st.text_input('Jitter:DDP')
        spread1 = st.text_input('spread1')
        spread2 = st.text_input('spread2')
        d2 = st.text_input('D2')
        ppe = st.text_input('PPE')

    parkinsons_diagnosis = ''

    if st.button('Parkinson’s Test Result'):
        try:
            input_data = [float(fo), float(fhi), float(flo), float(jitter_percent), float(jitter_abs),
                          float(rap), float(ppq), float(ddp), float(shimmer), float(shimmer_db),
                          float(apq3), float(apq5), float(apq), float(dda), float(nhr), float(hnr),
                          float(rpde), float(dfa), float(spread1), float(spread2), float(d2), float(ppe)]
            
            parkinsons_prediction = parkinsons_model.predict([input_data])

            if parkinsons_prediction[0] == 1:
                parkinsons_diagnosis = '⚠️ The person has Parkinson’s Disease'
            else:
                parkinsons_diagnosis = '✅ The person does NOT have Parkinson’s Disease'

            st.success(parkinsons_diagnosis)
        except ValueError:
            st.error("⚠️ Please enter valid numeric values for all fields.")
