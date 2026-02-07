# STEP 1: Import required tools
from dotenv import load_dotenv
import os
from groq import Groq

# STEP 2: Get API key securely
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

# Create Groq client (connection to AI)
client = Groq(api_key=api_key)

# STEP 3: System role prompt

SYSTEM_PROMPT = """
You are a Smart AI Prompt Engineer.
Your job is to help beginners learn concepts clearly.
Explain in simple words.
Use examples when needed.
Be friendly and encouraging.
"""

# STEP 4: Conversation memory

conversation_history = []

# STEP 5: Chat function

def chat(user_message, temperature=1.0):
    # Add user's message to memory
    conversation_history.append({
        "role": "user",
        "content": user_message
    })

    # Messages sent to the model
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        *conversation_history
    ]

    # Call Groq LLM
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=messages,
        temperature=temperature
    )

    # Extract AI reply
    ai_message = response.choices[0].message.content

    # Save AI reply to memory
    conversation_history.append({
        "role": "assistant",
        "content": ai_message
    })

    return ai_message

