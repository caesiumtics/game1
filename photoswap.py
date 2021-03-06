from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import numpy as np

# load and display an image with Matplotlib
# from matplotlib import image
# from matplotlib import pyplot
import matplotlib.pyplot as plt

"""
# Simple Streamlit app by KS
"""

with st.echo(code_location = 'below'):
    total_points = st.slider("Show image?", 0, 100, 50)
        
    fig = plt.figure()

    x = np.linspace(0, 1, 10)
    y = x
    
    plt(x, y)

    st.plotly_chart(fig)
