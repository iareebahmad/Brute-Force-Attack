import streamlit as st
import time
from random import randint

# Character pool
password_chars = [
    'a','b','c','d','e','f','g','h','i','j','k',
    'l','m','n','o','p','q','r','s','t','u','v',
    'w','x','y','z',0,1,2,3,4,5,6,7,8,9,'!','@',
    '#','$','%','&','*','-','_','=','+','/',
    'A','B','C','D','E','F','G','H','I','J',
    'K','L','M','N','O','P','Q','R','S','T',
    'U','V','W','X','Y','Z'
]

st.set_page_config(page_title="Password Cracker Simulator", layout="centered")

st.title("🔐 Password Cracker Simulator")
st.markdown("This is a **brute-force** password guessing demo. Enter a password, and the system will try to guess it randomly.")

# Password input
actualpwd = st.text_input("Enter your password", type="password")

# Button to start
if st.button("Start Cracking"):
    if not actualpwd:
        st.warning("Please enter a password.")
    else:
        placeholder = st.empty()
        guess_display = st.empty()
        result_display = st.empty()

        myguess = ""
        attempt = 0

        while myguess != actualpwd:
            myguess = ""
            for i in range(len(actualpwd)):
                guessletter = password_chars[randint(0, len(password_chars) - 1)]
                myguess = str(guessletter) + myguess
            attempt += 1

            # Live feedback
            placeholder.markdown(f"**Attempt #{attempt}:** `{myguess}`")
            time.sleep(0.05)  # Slow it down for effect

        guess_display.success(f"🎉 Password cracked after {attempt} attempts!")
        result_display.markdown(f"**Your password is:** `{myguess}`")
