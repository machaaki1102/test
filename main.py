import streamlit as st
import numpy as np
import pandas as pd
from PIL import Imege

st.title('1st 超入門')

st.write('DataFrame')


Imege.open('sample.jpg')
st.Image(img,caption='Kohei Imanishi', use_columns_width=True)

df = pd.DataFrame(
    np.random.rand(100,2)/[50,50] + [35.69,139.70],
    columns=['lat','lon']
)

st.map(df)
