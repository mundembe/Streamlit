import streamlit as st
from streamlit_lottie import st_lottie
import requests

st.set_page_config(page_title="My Webpage", page_icon=":heart:", layout="wide")

def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style.css")

#-----------Load Assets-----------
lottie_animation = load_lottie_url("https://assets8.lottiefiles.com/packages/lf20_we4yddwi.json")

# ----------Header Section------------

with st.container():
    st.subheader("HI Welcome to my webpage")
    st.title("Insert title here")
    st.write("---")

with st.container():
    left_column, right_column = st.columns(2)

    with left_column:
        st.header("Header")
        st.write("##")
        st.write(
            """
            Say \n
            Something\n
            Sweat\n
            """
        )

    with right_column:
        st_lottie(lottie_animation, height=300, key="coding")
    
#-----------Contact me-----------
with st.container():
    st.write("---")
    st.header("Get in touch with me")
    st.write("##")

    contact_form = """
    <form action="https://formsubmit.co/1488e08f91862990255ded1dd0e415e8" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """

    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
    
