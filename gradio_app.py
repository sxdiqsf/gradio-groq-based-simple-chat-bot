import gradio as gr
from chatbot import chat

def gradio_chat(user_input):
    return chat(user_input)

app = gr.Interface(
    fn=gradio_chat,
    inputs=gr.Textbox(
        lines=12,
        placeholder="Ask me anything...",
        label="Your Question"
    ),
    outputs=gr.Textbox(
        lines=12,
        label="AI Response"
    ),
    title="🤖 Smart AI Prompt Engineer",
    description="An AI chatbot built using Groq LLM with memory and role-based prompting."
)

if __name__ == "__main__":
    app.launch()
