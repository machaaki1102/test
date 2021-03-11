import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('1st 超入門')

st.write('Interactive Widgets')

option = st.text_input('あなたの趣味を教えて下さい')

'あなたの好きな趣味は',option,'です。'

condition = st.slider('あなたの今の調子は',0,100,50)
'コンディション',condition
#IF st.checkbox('Show Image'):
#    Imege.open('sample.jpg')
#    st.Image(img,caption='Kohei Imanishi', use_columns_width=True)