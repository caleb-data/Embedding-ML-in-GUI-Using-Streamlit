import streamlit as st
import pandas as pd
import os
import json

    
print("Current Working Directory: ", os.getcwd())
file_path = os.path.join(os.getcwd(), "Data", "trainset.csv")
data = pd.read_csv(file_path)

def data_page():
   # Title for the data page
    st.title("Customer Churn Data")

    # Sidebar filters
    st.sidebar.title("Data Filters")
    gender_filter = st.sidebar.multiselect("Gender", options=data["gender"].unique(), default=data["gender"].unique())
    internet_service_filter = st.sidebar.multiselect("Internet Service", options=data["InternetService"].unique(), default=data["InternetService"].unique())
    contract_filter = st.sidebar.multiselect("Contract Type", options=data["Contract"].unique(), default=data["Contract"].unique())

    # Filter data based on sidebar selections
    filtered_data = data[
        (data["gender"].isin(gender_filter)) &
        (data["InternetService"].isin(internet_service_filter)) &
        (data["Contract"].isin(contract_filter))
    ]

    # Display data overview section
    st.markdown("<div class='section-title'>Filtered Data Summary</div>", unsafe_allow_html=True)
    st.write("Showing a summary of the data based on your selected filters.")
    st.write(filtered_data.describe())

    # Display full filtered data
    st.markdown("<div class='section-title'>Full Filtered Data</div>", unsafe_allow_html=True)
    st.write("You can scroll through the filtered data below.")
    st.write(filtered_data.style.set_properties(**{'background-color': '#f5f5f5', 'color': '#333', 'border-color': 'black'}))

    # Download button
    st.markdown("<div class='section-title'>Download Filtered Data</div>", unsafe_allow_html=True)
    csv = filtered_data.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download CSV",
        data=csv,
        file_name='filtered_data.csv',
        mime='text/csv',
        help="Download the filtered dataset as a CSV file",
    )

