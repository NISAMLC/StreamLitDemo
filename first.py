import pandas as pd
import streamlit as st
import numpy as np

st.title('This is my first Streamlit App')

##ways to add text into our application

st.header(" Header")
st.subheader('Sub Header')

st.text("This is my text area here i can write long paragraphs")
st.markdown("""
# Header-1
## Header-2
### Header-3
This is my **third** line
- One
- Two
- Three

## To pass emoji 😍

:sunglasses: <br>
:joy:

""",unsafe_allow_html=True)



st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')


st.latex("""
a^2 + b^2 + 2ab
""")



sales = pd.read_csv('Superstore.csv')
sales = sales[:50]

myList = [1,2,3,4,5,6,7,8,9,10]
arr = np.array(myList)
dim = arr.reshape(2,5)
myDict = {
    'courses':['DS','ML','DL','CV'],
    'Grades':[22,32,42,54],
    'Domain':['Physics','Biology','Finance','Econometrics']
}
st.subheader("-----------------------------------------------------------------------------------")

st.write(
"""
# First Header
## Second header

- Jack
- John
- Jannet

"""
)

st.write(
    'this is my sales data',sales
)

st.write('This is my list',myList)
st.write('this is my array', arr)
st.write('This is with 2x5 dimension', dim)
st.write('This is my dictionary', myDict)

st.write('Data stats description', sales.describe())


