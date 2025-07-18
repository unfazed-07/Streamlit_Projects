import streamlit as st
import pandas as pd
import os

st.caption("🧠 This feedback form was built with help from AI tools. I currently have no knowledge of SQL, and used AI guidance to apply basic Pandas for storing responses locally in a CSV file.")
st.caption("🔒 Your feedback is stored privately and will only be used to improve this portfolio. No personal data is shared.")
with st.form("feedback_form"):
    st.title("Survey Form")
    name=st.text_input("Enter Your Name: (Optional)")
    role=st.selectbox("Are you a:", ["Student", "Mentor", "Other"])
    rating=st.slider("How would you rate my Protfolio", 1, 10)
    comments =st.text_area("Any suggestion or feedback?")
    submit=st.form_submit_button("Submit")
    if submit:
        feedback=pd.DataFrame({
            "Name":[name],
            "Role":[role],
            'Rating':[rating],
            "comments":[comments]
        })

        file_path="feedback.csv"
        if os.path.exists(file_path):
            feedback.to_csv(file_path, mode='a', header=False, index=False)
        else:
            feedback.to_csv(file_path, index=False)
        
        st.success('Thanks for Your Feedback!, it has been saved')

# 🔽 Download button for you (admin)
feedback_df = pd.read_csv("feedback.csv")

# Ask for password
password = st.text_input("Enter admin password to view feedback", type="password")

# Check against Streamlit secret
if password == st.secrets["admin"]["password"]:
    st.download_button("Download All Feedback (Admin)", feedback_df.to_csv(index=False), "feedback.csv")
elif password:
    st.warning("Wrong password. Try again.")


