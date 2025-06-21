import streamlit as st
from utils import load_sample_data, plot_chart, chart_guidelines

st.set_page_config(page_title="🧠 Match Data Types to Visuals", layout="centered")

st.title("📊 Match Data Types to Visualizations")
st.markdown("Select a data type and chart to test which visualizations work best and why.")

# Sidebar selections
super_type = st.sidebar.selectbox("Select Data Type Group", ["Numerical", "Categorical", "Time-Series", "Text"])
sub_type_options = {
    "Numerical": ["Discrete", "Continuous"],
    "Categorical": ["Nominal", "Ordinal"],
    "Time-Series": ["Continuous"],
    "Text": ["Text"]
}
sub_type = st.sidebar.selectbox("Select Specific Type", sub_type_options[super_type])

# Key for chart guidance
key = f"{super_type}-{sub_type}"
chart_choices = [
    "Bar Chart", "Pie Chart", "Line Chart", "Histogram", "Box Plot",
    "Dot Plot", "Area Chart", "Word Cloud"
]
chart_type = st.sidebar.selectbox("Try Chart Type", chart_choices)

# Show hint for correct chart types
st.markdown(f"💡 **Recommended Chart Types for {key}:** `{', '.join(chart_guidelines.get(key, []))}`")

# Load and show data
df = load_sample_data(super_type, sub_type)
st.subheader("🔍 Sample Dataset")
st.dataframe(df)

# Plot
st.subheader("📈 Visualization Output")
try:
    fig, is_correct = plot_chart(df, super_type, sub_type, chart_type)
    st.pyplot(fig)
    if is_correct:
        st.success(f"✅ '{chart_type}' is a good choice for {key} data.")
    else:
        st.warning(f"⚠️ '{chart_type}' can technically be plotted, but it's **not ideal** for this data type.")

except Exception as e:
    st.error(str(e))
