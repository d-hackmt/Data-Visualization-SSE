
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from wordcloud import WordCloud
import streamlit as st
import io

# Suppress warnings
import warnings
warnings.filterwarnings("ignore")

# Sample datasets
def get_sample_datasets():
    datasets = {
        "Numerical - Continuous": pd.DataFrame({
            "Height(cm)": [150, 160, 165, 170, 175, 180, 185, 190, 195, 200]
        }),
        "Numerical - Discrete": pd.DataFrame({
            "Books Owned": [1, 2, 2, 3, 3, 3, 4, 5, 5, 5]
        }),
        "Categorical - Nominal": pd.DataFrame({
            "Gender": ["Male", "Female", "Female", "Male", "Other", "Female"]
        }),
        "Categorical - Ordinal": pd.DataFrame({
            "Satisfaction": ["Low", "Medium", "High", "High", "Low", "Medium"]
        }),
        "Time-Series": pd.DataFrame({
            "Date": pd.date_range(start="2023-01-01", periods=10, freq="M"),
            "Sales": [120, 150, 160, 180, 200, 190, 210, 230, 250, 240]
        }),
        "Text (Unstructured)": pd.DataFrame({
            "Tweets": [
                "I love data visualization!",
                "Python is great for data science.",
                "Visualization makes data come alive.",
                "Streamlit apps are super useful.",
                "Machine learning is amazing.",
                "Data is the new oil.",
                "AI is transforming the world.",
                "This plot looks fantastic!",
                "Bar charts are easy to read.",
                "Let's build something cool."
            ]
        })
    }
    return datasets

# Chart rendering functions
def plot_visualization(data_type, df):
    fig, ax = plt.subplots()
    st.write("### Recommended Chart for:", data_type)

    if data_type == "Numerical - Continuous":
        sns.histplot(df.iloc[:, 0], kde=True, ax=ax)
        st.pyplot(fig)

    elif data_type == "Numerical - Discrete":
        sns.countplot(x=df.iloc[:, 0], ax=ax)
        st.pyplot(fig)

    elif data_type == "Categorical - Nominal":
        sns.countplot(x=df.iloc[:, 0], ax=ax)
        st.pyplot(fig)

    elif data_type == "Categorical - Ordinal":
        order = ["Low", "Medium", "High"]
        sns.countplot(x=df.iloc[:, 0], order=order, ax=ax)
        st.pyplot(fig)

    elif data_type == "Time-Series":
        fig = px.line(df, x="Date", y="Sales", title="Sales Over Time")
        st.plotly_chart(fig)

    elif data_type == "Text (Unstructured)":
        text = " ".join(df["Tweets"])
        wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)
        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis("off")
        st.pyplot(plt)

# Instructional text
def get_instruction_text(data_type):
    hints = {
        "Numerical - Continuous": "✅ Use Histogram or KDE plot to visualize distribution.",
        "Numerical - Discrete": "✅ Use Bar Chart to show counts of each discrete value.",
        "Categorical - Nominal": "✅ Use Bar Chart or Pie Chart to show category frequency.",
        "Categorical - Ordinal": "✅ Use Ordered Bar Chart to show rankings.",
        "Time-Series": "✅ Use Line Chart to track values over time.",
        "Text (Unstructured)": "✅ Use Word Cloud to visualize frequent words."
    }
    return hints.get(data_type, "")
