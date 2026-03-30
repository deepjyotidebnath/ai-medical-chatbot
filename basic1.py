import os
from groq import Groq
from dotenv import load_dotenv

# Load API key
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def get_ai_response(user_input, chat_history):

    # Add user input
    chat_history.append({
        "role": "user",
        "content": user_input
    })

    # API call
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=chat_history,
        temperature=0.7
    )

    reply = response.choices[0].message.content

    # Add bot reply
    chat_history.append({
        "role": "assistant",
        "content": reply
    })

    return reply, chat_history