import streamlit as st
import json

def history_page():

    st.title("Prediction History")


    # Initialize session state to store history if not already done
    if "single_prediction_history" not in st.session_state:
        st.session_state.single_prediction_history = []

    if "bulk_prediction_history" not in st.session_state:
        st.session_state.bulk_prediction_history = []

    # Display Single Predictions History
    st.subheader("Single Predictions")
    if st.session_state.single_prediction_history:
        for i, entry in enumerate(st.session_state.single_prediction_history):
            st.write(f"**{i + 1}. Input Data:** {entry['input_data']} | **Prediction:** {entry['prediction']} | **Probability:** {entry['probability']:.2f}%")
    else:
        st.write("No single predictions yet.")

    # Display Bulk Predictions History
    st.subheader("Bulk Predictions")
    if st.session_state.bulk_prediction_history:
        for i, bulk in enumerate(st.session_state.bulk_prediction_history):
            st.write(f"**Batch {i + 1}:** {bulk['file_name']} with {len(bulk['results'])} records.")
            st.dataframe(bulk['results'])
    else:
        st.write("No bulk predictions yet.")

    # Option to clear history
    if st.button("Clear All History"):
        st.session_state.single_prediction_history = []
        st.session_state.bulk_prediction_history = []
        st.success("Prediction history cleared!")

    
    