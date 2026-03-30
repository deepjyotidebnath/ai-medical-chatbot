import streamlit as st
from basic1 import get_ai_response

st.set_page_config(page_title="AI Medical Assistant", layout="wide")

st.title("🩺 AI Medical Chatbot ")
st.warning("⚠️ Not a real doctor. Always consult a medical professional.")

# UI chat messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# AI chat history (FIXED ✅)
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        {
            "role": "system",   # ✅ IMPORTANT FIX
            "content": """
You are a medical assistant AI.

Rules:
- Suggest possible conditions based on symptoms
- Recommend only basic OTC medicines (like paracetamol, ORS, antacids)
- Suggest safe home remedies (like hydration, rest, ginger tea, etc.)
- DO NOT prescribe strong medicines or antibiotics
- Mention dosage only if very safe and common
- Always include:
  1. Possible condition
  2. Medicines (if safe)
  3. Home remedies
  4. When to see a doctor
- Keep answers simple and structured
"""
        }
    ]

# Input box
user_input = st.chat_input("Describe your symptoms...")

# Process input
if user_input:
    st.session_state.messages.append(("user", user_input))

    with st.spinner("Analyzing symptoms..."):
        response, st.session_state.chat_history = get_ai_response(
            user_input,
            st.session_state.chat_history
        )

    st.session_state.messages.append(("bot", response))

# Show chat
for sender, msg in st.session_state.messages:
    if sender == "user":
        st.chat_message("user").write(msg)
    else:
        st.chat_message("assistant").write(msg)

# Clear chat
if st.button("🗑️ Clear Chat"):
    st.session_state.messages = []
    st.session_state.chat_history = [
        {
            "role": "system",   # ✅ FIX AGAIN HERE
            "content": """
You are a medical assistant AI.

Rules:
- Suggest possible conditions based on symptoms
- Recommend only basic OTC medicines (like paracetamol, ORS, antacids)
- Suggest safe home remedies (like hydration, rest, ginger tea, etc.)
- DO NOT prescribe strong medicines or antibiotics
- Mention dosage only if very safe and common
- Always include:
  1. Possible condition
  2. Medicines (if safe)
  3. Home remedies
  4. When to see a doctor
- Keep answers simple and structured
"""
        }
    ]