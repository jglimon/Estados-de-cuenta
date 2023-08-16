import streamlit as st

st.title('Estados de Cuentas Banamex')

# Data Source
st.sidebar.subheader("Data Source")
data_source = st.sidebar.selectbox("Select the data source file extension:", [".csv file", ".xlsx file"])

if data_source == ".csv file":
	data_source = "csv"
else:
	data_source = "excel"
	
# Data File Path
st.sidebar.subheader("Input Data File Path")
path = st.sidebar.text_input("Enter the input data file path here:", "Desktop/")
