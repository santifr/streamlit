import streamlit as st 
import pandas as pd 
import numpy as np
import matplotlib as pt


def main(): 
    # Your Code
    st.markdown('# Dashboard Streamlit') 

    st.markdown('Streamlit is **_really_ cool**.')


    # Generate fake data
    #x = np.random.normal(size=1000)
    #y = x * 3 + np.random.normal(size=1000)
    chart_data = pd.DataFrame(np.random.randn(20, 3),columns=['a', 'b', 'c'])
    st.line_chart(chart_data)

 

# Add a slider to the sidebar:
    #add_slider = st.sidebar.slider('Select a range of values', 0.0, 100.0, (25.0, 75.0)
    st.sidebar.markdown('# Titulo izquierdo')

if __name__ == "__main__": 
    main()



