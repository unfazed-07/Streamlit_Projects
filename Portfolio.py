import streamlit as st
import pandas as pd

st.markdown(
    "<small><i>Built with curiosity and commitment—not polish. I’m learning, and this will grow with me.</i></small>",
    unsafe_allow_html=True
)


st.set_page_config(
    page_title="Divyansh Sharma - Protfolio", 
    layout="centered"
)

#--Title--
st.title(''':red[Divyansh Sharma - Portfolio]''')
#--Introducation--
st.markdown("""
### :orange[Welcome!]
:orange[Hi, I'm **Divyansh Sharma**, a Computer Science Undergraduate Student with a strong interest in **Artificial Intelligence and Machine learning**.]

:orange[Currently, I'm building a strong foundation in **Python**, curently learning Python(OOP), basic Streamlit.This portfolio is a brief and honest summary of what I've learned so far and will be updated regularly as I continue  my learning Journey]
""")

#--Education Section--
st.markdown("---")
st.markdown("### 🎓:orange[Education]")
edu_data = pd.DataFrame({
        "Qualification": [
        " [B.Tech in CSE (GenAI)",
        "Class 12th", 
        "Class 10th"
    ],
    "Institution": [
        "Lovely Professional University",
        " -- ",
        " -- "
    ],
    "Status / Marks": [
        "Ongoing",
        "89%",
        "95%"
    ]
})
st.dataframe(edu_data)

#-----Certifications Section-----

st.markdown("### :orange[📃Certifications]")
cert_data = pd.DataFrame({
    "Certificate Name": [
        "Python for Everybody",
        "AI for Everyone"
    ],
    "Issuing Body": [
        "University of Michigan",
        "DeepLearning.AI"
    ],
    "Link": [
        "https://coursera.org/share/64b6f570d0016f0e52da969aa7397976",
        "https://coursera.org/share/ef4fa4a0c8143dc51c8734201e0d9fe2"
    ]
})
for i, row in cert_data.iterrows():
        st.markdown(f"- **{row['Certificate Name']}** from {row['Issuing Body']} - [View Certificate]({row['Link']})")

#---Project Section---#

st.markdown("### 📽️:orange[Projects]")

st.markdown("""
- [**Stregit amlit Protfolio Website**]() -  A simple interactive web app built using Streamlit library to display my skills, certifications, and learning journey so far. I'm always looking foward to make its interface better as I learn. Check out, clown it for your own if you like. 

- [**PY4E Assignments**](https://github.com/unfazed-07/Python_for_everybody_assignments) - A collection of some of the programming assignments I complete as a part of "Python for Everybody" Specialisation.

-  [**Python Practice**](https://github.com/unfazed-07/python_practice)- A python repo, here i put some of the basic projects I made as Part of Practice
            
""")
st.markdown("""

""")
#---Contact Info
st.markdown("---")
st.markdown("##### 🔗 :orange[Connect with Me]")
st.markdown('''
- [GitHub](https://github.com/unfazed-07)
- [LinkedIn](https://www.linkedin.com/in/divyansh-sharma-5546b3223/)
- [Coursera](https://www.coursera.org/user/f7b4f468562cff9050e26a0a5c1e22dd)
- 📧 Email: divyansh_sharma007@hotmail.com
''')

#--SIDEBAR--
#--SURVEY Button--
#--LET'S MAKE--
