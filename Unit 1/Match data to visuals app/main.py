
import streamlit as st
from utils import get_sample_datasets, plot_visualization, get_instruction_text

st.set_page_config(page_title="Match Data Types to Visuals", layout="centered")

st.title("📊 Match Data Types to Visualizations")
st.markdown("Explore how different data types require different visualization techniques.")

datasets = get_sample_datasets()
data_type = st.selectbox("Choose a Data Type", list(datasets.keys()))

df = datasets[data_type]

st.write("### Sample Data")
st.dataframe(df)

st.info(get_instruction_text(data_type))

plot_visualization(data_type, df)
