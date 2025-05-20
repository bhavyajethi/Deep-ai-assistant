import streamlit as st
from agents.research_agent import research_node
from voice_mode import listen_and_transcribe, speak_output
from utils import save_to_pdf, translate_answer

# Session init
if "history" not in st.session_state:
    st.session_state["history"] = []

st.set_page_config(page_title="Deep Research AI", page_icon="🧠")
st.title("🧠 Deep Research AI Assistant (Gemini)")

query = st.session_state.get("query", "")
query = st.text_input("Enter your question here", value=query)

if st.button("🎙️ Use Voice"):
    with st.spinner("🎧 Listening..."):
        query = listen_and_transcribe()
        st.session_state["query"] = query
        st.success(f"You said: {query}")

if st.button("🔍 Run Research"):
    if not query:
        st.warning("⚠️ Please enter a question or use voice")
    else:
        with st.spinner("🧠 Researching using Gemini..."):
            result = research_node(query)

        final_ans = result.get("gemini_answer", "No answer generated")
        sources = result.get("sources", [])

        st.session_state["final_ans"] = final_ans
        st.session_state["history"].append({"q": query, "a": final_ans})

        st.subheader("📌 Gemini Answer")
        st.markdown(
            f"""
            <div style='padding: 20px; background-color: #f5f5f5; border-left: 5px solid #4CAF50; border-radius: 5px; font-size: 16px;'>
            {final_ans}
            </div>
            """,
            unsafe_allow_html=True,
        )

        if sources:
            st.subheader("🔗 Sources")
            for url in sources:
                st.markdown(f"- [{url}]({url})")
        else:
            st.info("No sources found.")

        speak_output(final_ans)

if st.button("📤 Export to PDF"):
    save_to_pdf(query, st.session_state.get("final_ans", ""), st.session_state.get("sources", []))
    st.success("PDF saved as 'output.pdf'")

if st.button("🌐 Translate Answer to Hindi"):
    translated = translate_answer(st.session_state.get("final_ans", ""), "hi")
    st.markdown(f"**Translated Answer (Hindi):** {translated}")

if st.button("📜 Show Chat History"):
    st.subheader("Chat History")
    for item in st.session_state["history"]:
        st.markdown(f"**Q:** {item['q']}\n\n**A:** {item['a']}")
