import streamlit as st
from core.ai_engine import get_ai_response

# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(
    page_title="OMNI AI",
    page_icon="🤖",
    layout="wide"
)

# -------------------------------
# Session State
# -------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# -------------------------------
# Custom CSS
# -------------------------------
st.markdown("""
<style>
    .main-title {
        font-size: 42px;
        font-weight: bold;
        text-align: center;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        color: #777;
        font-size: 18px;
        margin-bottom: 30px;
    }

    .feature-card {
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #ddd;
        margin-bottom: 15px;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# -------------------------------
# Sidebar
# -------------------------------
with st.sidebar:
    st.title("🤖 OMNI AI")

    st.write("Your Intelligent AI Assistant")

    st.divider()

    menu = st.radio(
        "Navigation",
        [
            "🏠 Home",
            "💬 AI Chat",
            "📄 Document AI",
            "📝 Summarizer",
            "🌐 Translator",
            "💻 Code Assistant"
        ]
    )

    st.divider()

    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# -------------------------------
# Home
# -------------------------------
if menu == "🏠 Home":

    st.markdown(
        '<div class="main-title">🤖 OMNI AI</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">Your Intelligent AI Assistant</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="feature-card">
            <h2>💬</h2>
            <h3>AI Chat</h3>
            <p>Ask questions and get intelligent answers.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="feature-card">
            <h2>📄</h2>
            <h3>Document AI</h3>
            <p>Upload documents and ask questions.</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="feature-card">
            <h2>💻</h2>
            <h3>Code Assistant</h3>
            <p>Debug, explain and improve your code.</p>
        </div>
        """, unsafe_allow_html=True)

    st.info("Select a feature from the sidebar to get started.")

# -------------------------------
# AI CHAT
# -------------------------------
elif menu == "💬 AI Chat":

    st.title("💬 AI Chat")

    st.write("Ask OMNI AI anything.")

    # Display previous messages
    for message in st.session_state.messages:

        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Chat input
    user_input = st.chat_input("Ask OMNI AI anything...")

    if user_input:

        # Display user message
        st.session_state.messages.append({
            "role": "user",
            "content": user_input
        })

        with st.chat_message("user"):
            st.markdown(user_input)

        # Generate response
        with st.chat_message("assistant"):

            with st.spinner("OMNI AI is thinking..."):

                response = get_ai_response(
                    user_input,
                    st.session_state.messages
                )

                st.markdown(response)

        # Save AI response
        st.session_state.messages.append({
            "role": "assistant",
            "content": response
        })

# -------------------------------
# Other Modules
# -------------------------------
elif menu == "📄 Document AI":

    st.title("📄 Document AI")

    st.info(
        "Document AI module will be added next. "
        "You will be able to upload PDF, DOCX and TXT files."
    )

elif menu == "📝 Summarizer":

    st.title("📝 AI Summarizer")

    st.info("Summarizer module will be added next.")

elif menu == "🌐 Translator":

    st.title("🌐 AI Translator")

    st.info("Translator module will be added next.")

elif menu == "💻 Code Assistant":

    st.title("💻 Code Assistant")

    st.info(
        "Code Assistant will help you explain, debug and "
        "optimize Python, C, Java and other code."
    )