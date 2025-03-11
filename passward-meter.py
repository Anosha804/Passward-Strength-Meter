import streamlit as st
import random
import string
import re

def set_background():
    page_bg = """
    <style>
    .stApp {
        background-color: #E6E6FA;
    }
    .stButton>button {
        background-color: #F08080;
        color: white;
        padding: 10px 20px;
        font-size: 16px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
    }
    .stButton>button:hover {
        background-color: #FFDAB9;
    }
      input[type="password"] {
        border: 2px solid #F08080;
        border-radius: 5px;
        padding: 8px;
        width: 100%;
        font-size: 16px;
    }
    </style>
    """
    st.markdown(page_bg, unsafe_allow_html=True)

def check_password_strength(password):
    score = 0
    feedback = []
    
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")
    
    if re.search(r"[a-z]", password) and re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Include both uppercase and lowercase letters.")
    
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Include at least one number (0-9).")
    
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("Include at least one special character (!@#$%^&*).")
    
    common_passwords = ["password", "123456", "password123", "qwerty", "abc123"]
    if password in common_passwords:
        score = 1
        feedback = ["This password is too common. Please choose a stronger one."]
    
    return score, feedback

def generate_strong_password():
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(characters) for _ in range(12))

set_background()
st.title("🔐 Password Strength Meter")
password = st.text_input("Enter a password", type="password")

if password:
    score, feedback = check_password_strength(password)
    strength_labels = {1: "Weak 🔴", 2: "Weak 🔴", 3: "Moderate 🟡", 4: "Strong 🟢"}
    
    st.subheader(f"Strength: {strength_labels.get(score, 'Very Weak 🔴')}")
    
    if score < 5:
        st.write("💡 Suggestions:")
        for tip in feedback:
            st.write(f"- {tip}")
    else:
        st.success("✅ Great! Your password is strong.")

if st.button("Generate Strong Password"):
    strong_password = generate_strong_password()
    st.write("🔑 Suggested Strong Password:", strong_password)
