import streamlit as st 
import pandas as pd 
import numpy as np 



## Title of the application 
st.title("Hello World ")

## Display a simple text there 
st.write("Hi  there i am navneet there ")


## Display the dataframe 
df = pd.DataFrame({
    'fistNames' : ['navneet' , 'rahul', 'rajat' ], 
    'numbers' : [1, 2, 3 ]
})
st.write( "Here is my daaframe ")
st.write(df)


# create a line chart 
chart_data = pd.DataFrame(
    np.random.randn(20, 3), 
    columns= ['a', 'b', 'c']
)
st.line_chart(chart_data)



