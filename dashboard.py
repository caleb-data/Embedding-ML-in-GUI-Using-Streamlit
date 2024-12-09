import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st


def dashboard_page():
    st.title("Customer Churn Dashboard")

    # Load data
    data_file = os.path.join(os.getcwd(), "data", "train_data.csv")
    data = pd.read_csv(data_file)

    # Sidebar filters
     
 
    st.sidebar.title("Filters")

    filters = {

        "gender": st.sidebar.multiselect("Gender", options=data["gender"].unique(), default=data["gender"].unique()),

        "InternetService": st.sidebar.multiselect("Internet Service", options=data["InternetService"].unique(), default=data["InternetService"].unique()),

        "Contract": st.sidebar.multiselect("Contract Type", options=data["Contract"].unique(), default=data["Contract"].unique()),

        "PaymentMethod": st.sidebar.multiselect("Payment Method", options=data["PaymentMethod"].unique(), default=data["PaymentMethod"].unique()),

    }
    
    # Filter data based on user selections

    def apply_filters(data, filters):

        for column, selected_values in filters.items():

            data = data[data[column].isin(selected_values)]

        return data
    
    # Filtered data

    filtered_data = apply_filters(data, filters)
    
    # Display summary

    st.write("### Summary of Filtered Data")

    st.write(filtered_data.describe())
    
    # Churn distribution as a Donut Chart

    st.write("### Churn Distribution")

    churn_counts = filtered_data["Churn"].value_counts()

    fig, ax = plt.subplots(figsize=(7, 7))

    ax.pie(

        churn_counts,

        labels=churn_counts.index,

        autopct="%1.1f%%",

        startangle=90,

        colors=sns.color_palette("pastel"),

        wedgeprops={"edgecolor": "black", "linewidth": 1.5},

        pctdistance=0.85,

    )

    # Add circle for the donut hole

    centre_circle = plt.Circle((0, 0), 0.70, fc="white")

    plt.gca().add_artist(centre_circle)

    ax.axis("equal")

    st.pyplot(fig)
    
    # Monthly Charges as a Box Plot

    st.write("### Monthly Charges Distribution")

    fig, ax = plt.subplots(figsize=(8, 5))

    sns.boxplot(

        x="MonthlyCharges",

        data=filtered_data,

        palette="coolwarm",

        linewidth=1.5,

        ax=ax,

    )

    ax.set_title("Monthly Charges Distribution", fontsize=14)

    ax.set_xlabel("Monthly Charges", fontsize=12)

    st.pyplot(fig)
    
    # Total Charges vs Tenure as a Bubble Chart

    st.write("### Total Charges vs Tenure (Bubble Chart)")

    fig, ax = plt.subplots(figsize=(8, 5))

    bubble_sizes = filtered_data["MonthlyCharges"] * 2  # Adjust bubble sizes

    sns.scatterplot(

        data=filtered_data,

        x="tenure",

        y="TotalCharges",

        size=bubble_sizes,

        sizes=(20, 200),

        hue="Churn",

        palette="Set2",

        edgecolor="black",

        linewidth=0.5,

        ax=ax,

    )

    ax.set_title("Total Charges vs Tenure", fontsize=14)

    ax.set_xlabel("Tenure (Months)", fontsize=12)

    ax.set_ylabel("Total Charges", fontsize=12)

    ax.legend(title="Churn")

    st.pyplot(fig)
    
    # Horizontal Bar Charts for Churn by Contract Type

    st.write("### Churn Rate by Contract Type (Horizontal Bar Chart)")

    contract_counts = filtered_data.groupby(["Contract", "Churn"]).size().unstack(fill_value=0)

    fig, ax = plt.subplots(figsize=(8, 5))

    contract_counts.plot(

        kind="barh",

        stacked=True,

        color=["#66b3ff", "#ff9999"],

        ax=ax,

        edgecolor="black",

    )

    ax.set_title("Churn Rate by Contract Type", fontsize=14)

    ax.set_xlabel("Count", fontsize=12)

    ax.set_ylabel("Contract Type", fontsize=12)

    ax.legend(title="Churn")

    st.pyplot(fig)
    
    # Horizontal Bar Charts for Churn by Payment Method

    st.write("### Churn Rate by Payment Method (Horizontal Bar Chart)")

    payment_counts = filtered_data.groupby(["PaymentMethod", "Churn"]).size().unstack(fill_value=0)

    fig, ax = plt.subplots(figsize=(8, 5))

    payment_counts.plot(

        kind="barh",

        stacked=True,

        color=["#99ff99", "#ffcc99"],

        ax=ax,

        edgecolor="black",

    )

    ax.set_title("Churn Rate by Payment Method", fontsize=14)

    ax.set_xlabel("Count", fontsize=12)

    ax.set_ylabel("Payment Method", fontsize=12)

    ax.legend(title="Churn")

    st.pyplot(fig)
    
    # Horizontal Bar Charts for Churn by Internet Service

    st.write("### Churn Rate by Internet Service (Horizontal Bar Chart)")

    internet_counts = filtered_data.groupby(["InternetService", "Churn"]).size().unstack(fill_value=0)

    fig, ax = plt.subplots(figsize=(8, 5))

    internet_counts.plot(

        kind="barh",

        stacked=True,

        color=["#c2c2f0", "#ffb3e6"],

        ax=ax,

        edgecolor="black",

    )

    ax.set_title("Churn Rate by Internet Service", fontsize=14)

    ax.set_xlabel("Count", fontsize=12)

    ax.set_ylabel("Internet Service", fontsize=12)

    ax.legend(title="Churn")

    st.pyplot(fig)

 
