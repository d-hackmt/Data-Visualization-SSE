import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from wordcloud import WordCloud

# Sample datasets grouped by super type
def load_sample_data(super_type, sub_type):
    if super_type == "Numerical":
        if sub_type == "Discrete":
            return pd.DataFrame({'Items Sold': [2, 3, 5, 5, 2, 1, 3, 4, 3, 3]})
        elif sub_type == "Continuous":
            return pd.DataFrame({'Marks': np.random.normal(75, 10, 100)})

    elif super_type == "Categorical":
        if sub_type == "Nominal":
            return pd.DataFrame({'Gender': ['Male', 'Female', 'Other'] * 10})
        elif sub_type == "Ordinal":
            return pd.DataFrame({'Satisfaction': ['Low', 'Medium', 'High', 'Medium', 'Low'] * 10})

    elif super_type == "Time-Series":
        dates = pd.date_range(start='2024-01-01', periods=30)
        return pd.DataFrame({'Date': dates, 'Sales': np.random.randint(50, 150, size=30)})

    elif super_type == "Text":
        tweets = [
            "AI will change the world!", "Data visualization makes insights easier to see.",
            "Python is amazing for data science.", "Streamlit apps are interactive and cool.",
            "Word clouds help visualize text beautifully.", "Education and data go hand in hand.",
            "Transforming ideas into code with AI.", "ChatGPT helps me understand things faster!"
        ]
        return pd.DataFrame({'Tweet': tweets})

    else:
        return pd.DataFrame()

# Match rules for correct visualizations
chart_guidelines = {
    "Numerical-Discrete": ["Bar Chart", "Pie Chart"],
    "Numerical-Continuous": ["Histogram", "Line Chart", "Box Plot"],
    "Categorical-Nominal": ["Bar Chart", "Pie Chart"],
    "Categorical-Ordinal": ["Bar Chart", "Dot Plot"],
    "Time-Series-Continuous": ["Line Chart", "Area Chart"],
    "Text-Text": ["Word Cloud"]
}

# Central plotting function
def plot_chart(df, super_type, sub_type, chart_type):
    key = f"{super_type}-{sub_type}"
    valid_charts = chart_guidelines.get(key, [])

    fig, ax = plt.subplots()

    try:
        # Handle different combinations
        if super_type == "Numerical" and sub_type == "Discrete":
            data = df['Items Sold']
            if chart_type == "Bar Chart":
                data.value_counts().plot(kind='bar', ax=ax)
            elif chart_type == "Pie Chart":
                data.value_counts().plot(kind='pie', autopct='%1.1f%%', ax=ax)
            else:
                raise ValueError("Invalid chart for this data type.")

        elif super_type == "Numerical" and sub_type == "Continuous":
            data = df['Marks']
            if chart_type == "Histogram":
                sns.histplot(data, kde=True, ax=ax)
            elif chart_type == "Line Chart":
                ax.plot(data)
            elif chart_type == "Box Plot":
                sns.boxplot(x=data, ax=ax)
            else:
                raise ValueError("Invalid chart for this data type.")

        elif super_type == "Categorical" and sub_type == "Nominal":
            data = df['Gender']
            if chart_type == "Bar Chart":
                data.value_counts().plot(kind='bar', ax=ax)
            elif chart_type == "Pie Chart":
                data.value_counts().plot(kind='pie', autopct='%1.1f%%', ax=ax)
            else:
                raise ValueError("Invalid chart for this data type.")

        elif super_type == "Categorical" and sub_type == "Ordinal":
            order = ['Low', 'Medium', 'High']
            df['Satisfaction'] = pd.Categorical(df['Satisfaction'], categories=order, ordered=True)
            if chart_type == "Bar Chart":
                df['Satisfaction'].value_counts().loc[order].plot(kind='bar', ax=ax)
            elif chart_type == "Dot Plot":
                sns.stripplot(x='Satisfaction', data=df, order=order, ax=ax)
            else:
                raise ValueError("Invalid chart for this data type.")

        elif super_type == "Time-Series":
            if chart_type == "Line Chart":
                ax.plot(df['Date'], df['Sales'], marker='o')
            elif chart_type == "Area Chart":
                ax.fill_between(df['Date'], df['Sales'], alpha=0.3)
            else:
                raise ValueError("Invalid chart for this data type.")
            ax.set_xlabel("Date")
            ax.set_ylabel("Sales")

        elif super_type == "Text":
            if chart_type == "Word Cloud":
                text = " ".join(df['Tweet'].values)
                wc = WordCloud(width=800, height=400, background_color='white').generate(text)
                plt.imshow(wc, interpolation='bilinear')
                plt.axis("off")
            else:
                raise ValueError("Invalid chart for text data.")

        return fig, chart_type in valid_charts

    except Exception as e:
        raise ValueError(f"❌ Cannot plot '{chart_type}' for {key} data. {str(e)}")
