import streamlit as st
import types
import tensorflow as tf
from tensorflow import keras

model = keras.models.load_model('model.h5')

@st.cache(hash_funcs={types.FunctionType: lambda _: None})
def load_model():
    model = keras.models.load_model('model_fashion_mnist.hdf5')
    return model

# Call the function
loaded_model = load_model()

st.write("""
#Fashion MNSIT Detection System"""
)
file=st.file_uploader("Choose plant photo from computer",type=["jpg","png"])
A