import streamlit as st
import pickle
import numpy as np
model = pickle.load(open('trained_modeloo', 'rb'))
st.title('iris Prediction Project')
sepal_l = st.number_input('Sepal Length')
sepal_w = st.number_input('Sepal Width')
petal_l = st.number_input('Petal Length')
petal_w = st.number_input('Petal Width')
input_data = np.asarray([[sepal_l, sepal_w, petal_l , petal_w]])
result = ''
if st.button('Result'):
    result = model.predict(input_data)[0]

st.success(result)
