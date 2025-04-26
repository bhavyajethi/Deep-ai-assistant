import streamlit as st
from lang_graph import build_graph

st.title("Deep Research AI Assistant")

query = st.text_input("Enter your question here")

if st.button("Run Research"):
    if not query:
        st.warning("Please enter a question first")
    else:
        lang_graph = build_graph()
        with st.spinner("Researching and drafting your ans..."):
            result = lang_graph.invoke({"query": query})


        final_ans = result.get("final_answer", "No answer generated")
        st.subheader("Final answer")
        st.markdown(
            f"""
            <div style='
                padding: 20px;
                background-color: #f5f5f5;
                border-left: 5px solid #4CAF50;
                border-radius: 5px;
                font-size: 16px;
                line-height: 1.5;
            '>
                {final_ans}
            </div>
            """,
            unsafe_allow_html=True,
        )