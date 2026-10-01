import os
import streamlit as st
from dotenv import load_dotenv

from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate


# =========================================================
# CONFIGURATION
# =========================================================

load_dotenv()

MODEL_NAME = "gemma3:4b"


# =========================================================
# LANGSMITH
# =========================================================

if os.getenv("LANGCHAIN_API_KEY"):
    os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
    os.environ["LANGCHAIN_TRACING_V2"] = "true"
    os.environ["LANGCHAIN_PROJECT"] = os.getenv(
        "LANGCHAIN_PROJECT",
        "AIRA Chatbot"
    )


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="AIRA - AI Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# CSS (Bi-directional native chat styling)
# =========================================================

st.markdown("""
<style>
.stApp {
    background-color: #0e1117;
}

#MainMenu, footer {
    visibility: hidden;
}

header {
    background: transparent !important;
}

/* ================= SIDEBAR ================= */
section[data-testid="stSidebar"] {
    background-color: #11151c;
    border-right: 1px solid #262b35;
}

.sidebar-title {
    font-size: 25px;
    font-weight: 700;
    color: #ffffff;
}

.sidebar-subtitle {
    color: #8b949e;
    font-size: 14px;
}

/* ================= HEADER ================= */
.header-container {
    padding: 10px 0 20px 0;
    border-bottom: 1px solid #262b35;
    margin-bottom: 25px;
}

.header-title {
    font-size: 36px;
    font-weight: 700;
    color: #ffffff;
}

.header-subtitle {
    font-size: 14px;
    color: #8b949e;
    margin-top: 4px;
}

.online-status {
    display: inline-block;
    margin-top: 12px;
    padding: 5px 11px;
    border-radius: 20px;
    background-color: #16261b;
    color: #4ade80;
    font-size: 12px;
}

.online-dot {
    display: inline-block;
    width: 7px;
    height: 7px;
    background-color: #4ade80;
    border-radius: 50%;
    margin-right: 6px;
}

/* ================= SIDEBAR CARDS ================= */
.model-card {
    background-color: #161b22;
    border: 1px solid #262b35;
    border-radius: 12px;
    padding: 14px;
    margin-bottom: 10px;
}

.model-label {
    font-size: 11px;
    color: #8b949e;
    text-transform: uppercase;
}

.model-value {
    font-size: 14px;
    font-weight: 600;
    color: #ffffff;
    margin-top: 5px;
}

/* ================= WELCOME ================= */
.welcome-container {
    text-align: center;
    padding-top: 60px;
    padding-bottom: 40px;
}

.welcome-icon {
    font-size: 54px;
}

.welcome-title {
    font-size: 28px;
    font-weight: 650;
    color: #ffffff;
    margin-top: 15px;
}

.welcome-description {
    color: #8b949e;
    font-size: 15px;
    margin-top: 8px;
}

/* ================= BI-DIRECTIONAL CHAT MESSAGES ================= */

/* Base container adjustment */
div[data-testid="stChatMessage"] {
    padding: 12px 18px;
    border-radius: 18px;
    margin-bottom: 16px;
    max-width: 80%;
}

/* USER MESSAGE (Right Aligned) */
div[data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarUser"]) {
    margin-left: auto;
    margin-right: 0;
    background-color: #2563eb !important;
    border-bottom-right-radius: 4px;
    flex-direction: row-reverse;
}

div[data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarUser"]) [data-testid="stChatMessageContent"] {
    text-align: right;
    color: #ffffff;
}

div[data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarUser"]) [data-testid="stChatMessageAvatarUser"] {
    margin-left: 12px;
    margin-right: 0;
}

/* ASSISTANT MESSAGE (Left Aligned) */
div[data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarAssistant"]) {
    margin-right: auto;
    margin-left: 0;
    background-color: #161b22 !important;
    border: 1px solid #262b35;
    border-bottom-left-radius: 4px;
}

div[data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarAssistant"]) [data-testid="stChatMessageAvatarAssistant"] {
    margin-right: 12px;
}

/* Code block adjustments inside bubbles */
div[data-testid="stChatMessage"] pre {
    border-radius: 8px;
    border: 1px solid #30363d;
}

/* ================= BUTTONS & INPUT ================= */
div.stButton > button {
    width: 100%;
    border-radius: 10px;
    border: 1px solid #30363d;
    background-color: #161b22;
    color: #c9d1d9;
}

div.stButton > button:hover {
    border-color: #58a6ff;
    color: #ffffff;
}

[data-testid="stChatInput"] {
    border-radius: 14px;
}
</style>
""", unsafe_allow_html=True)


# =========================================================
# SESSION STATE
# =========================================================

if "messages" not in st.session_state:
    st.session_state.messages = []

if "pending_prompt" not in st.session_state:
    st.session_state.pending_prompt = None


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:
    st.markdown('<div class="sidebar-title">🤖 AIRA</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-subtitle">Local AI Assistant</div>', unsafe_allow_html=True)
    st.divider()

    if st.button("＋  New Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

    st.divider()
    st.markdown("### ⚙️ Model")

    st.markdown(f"""
        <div class="model-card">
            <div class="model-label">Model</div>
            <div class="model-value">{MODEL_NAME}</div>
        </div>
        <div class="model-card">
            <div class="model-label">Framework</div>
            <div class="model-value">LangChain + Ollama</div>
        </div>
        <div class="model-card">
            <div class="model-label">Mode</div>
            <div class="model-value">100% Local</div>
        </div>
    """, unsafe_allow_html=True)

    st.divider()
    st.markdown("### 💡 Try asking")

    suggestions = [
        "Explain machine learning simply",
        "Write a Python binary search function",
        "What is RAG?",
        "Explain Transformers"
    ]

    for i, suggestion in enumerate(suggestions):
        if st.button(suggestion, key=f"suggestion_{i}", use_container_width=True):
            st.session_state.pending_prompt = suggestion
            st.rerun()

    st.divider()
    st.caption("Powered by LangChain • Ollama")


# =========================================================
# HEADER
# =========================================================

st.markdown("""
    <div class="header-container">
        <div class="header-title">AIRA</div>
        <div class="header-subtitle">Your local AI assistant powered by LangChain and Ollama</div>
        <div class="online-status">
            <span class="online-dot"></span>Local AI Online
        </div>
    </div>
""", unsafe_allow_html=True)


# =========================================================
# PROMPT
# =========================================================

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """You are AIRA, a helpful and intelligent AI assistant.

Guidelines:
- Give accurate and useful answers.
- Explain technical concepts clearly.
- Use examples when useful.
- For programming questions, provide clean, complete, and correct code enclosed in standard markdown code blocks.
- Keep answers concise unless more detail is required."""
        ),
        ("user", "{question}")
    ]
)


# =========================================================
# OLLAMA
# =========================================================

try:
    llm = OllamaLLM(
        model=MODEL_NAME,
        temperature=0.7
    )
except Exception as e:
    st.error("Failed to initialize Ollama.")
    st.code(str(e))
    st.stop()


# =========================================================
# WELCOME SCREEN OR CHAT HISTORY
# =========================================================

if len(st.session_state.messages) == 0:
    st.markdown("""
        <div class="welcome-container">
            <div class="welcome-icon">🤖</div>
            <div class="welcome-title">How can I help you today?</div>
            <div class="welcome-description">
                Ask me anything about AI, Machine Learning, Python, Data Science, coding or general topics.
            </div>
        </div>
    """, unsafe_allow_html=True)
else:
    for message in st.session_state.messages:
        avatar = "🧑" if message["role"] == "user" else "🤖"
        with st.chat_message(message["role"], avatar=avatar):
            st.markdown(message["content"])


# =========================================================
# INPUT
# =========================================================

pending_prompt = st.session_state.pending_prompt
st.session_state.pending_prompt = None

user_input = st.chat_input("Message AIRA...")

if pending_prompt:
    user_input = pending_prompt


# =========================================================
# GENERATE RESPONSE
# =========================================================

if user_input:
    # Append and display user input (right aligned)
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user", avatar="🧑"):
        st.markdown(user_input)

    # Stream assistant response (left aligned)
    with st.chat_message("assistant", avatar="🤖"):
        try:
            formatted_prompt = prompt.format(question=user_input)
            
            def response_generator():
                for chunk in llm.stream(formatted_prompt):
                    yield chunk

            full_response = st.write_stream(response_generator())
            st.session_state.messages.append({"role": "assistant", "content": full_response})

        except Exception as e:
            error_message = (
                f"⚠️ **Ollama Error**\n\n`{str(e)}`\n\n"
                f"Make sure `{MODEL_NAME}` is installed.\n\n"
                f"Run:\n```bash\nollama list\n```\n\n"
                f"If missing:\n```bash\nollama pull {MODEL_NAME}\n```"
            )
            st.markdown(error_message)
            st.session_state.messages.append({"role": "assistant", "content": error_message})