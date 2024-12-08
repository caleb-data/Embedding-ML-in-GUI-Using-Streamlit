# import streamlit as st
# from home import home_page
# from data import data_page
# from predict import predict_page
# from dashboard import dashboard_page
# from history import history_page


# # Authentication and login logic
# def authentication():
#     if 'authentication_status' not in st.session_state:
#         st.session_state['authentication_status'] = False

#     if not st.session_state['authentication_status']:
#         login_form()
#     else:
#         show_authentication_page()

# def login_form():
#     st.title("Login")
#     username = st.text_input("Username")
#     password = st.text_input("Password", type="password")

#     if st.button("Login"):
#         if username == "admin" and password == "password":
#             st.session_state['authentication_status'] = True
#             st.rerun()
#         else:
#             st.error("Username/password is incorrect")

# def show_authentication_page():
#     st.title("Welcome")
    
    
#     if st.button("Logout"):
#         logout()

# def logout():
#     st.session_state.clear()
#     #st.session_state['show_balloons'] = False
#     st.rerun()

# # Main function for handling navigation
# def main():
#     st.set_page_config(page_title="Streamlit App", page_icon=":rocket:", layout="centered", initial_sidebar_state="auto") #menu_items=None)
#     # Call authentication function
#     authentication()

#     # Only display navigation if authenticated
#     if st.session_state.get('authentication_status'):
#         # Sidebar navigation
#         st.sidebar.title("Navigator")
#         st.sidebar.write("Select a page to view:")
        
#         # Sidebar navigation options
#         page = st.sidebar.selectbox(
#             ":book:", 
#             ["Home", "Data", "Predict", "Dashboard",]
#         )

#         # Display the selected page content
#         if page == "Home":
#             Home_page()
#         elif page == "Data":
#             data_page()
#         elif page == "Predict":
#             predict_page()
#         elif page == "Dashboard":
#             dashboard_page()
#         elif page == "History":
#             history_page

# # Run the main function
# if __name__ == "__main__":
#     main()


import streamlit as st
#import os
#import json
from home import home_page
from data import data_page
from predict import predict_page
from dashboard import dashboard_page
from auth import authenticate



# Assigning to the appropriate pages
def main():
    authenticate()
    if st.session_state.authenticated: 
    # Creating a sidebar
        st.sidebar.title("Navigator")
        st.sidebar.write("Use this to select between pages")
        page = st.sidebar.selectbox("Navigate", ["Home", "Data", "Predict", "Dashboard"])

        if page == "Home":
            home_page()
        elif page == "Data":
            data_page()
        elif page == "Predict":
            predict_page()
        elif page == "Dashboard":
            dashboard_page()

if __name__ == "__main__":
    main()