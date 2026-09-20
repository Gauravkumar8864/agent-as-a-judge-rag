import streamlit as st

from src.rag_pipeline import ask_question


st.set_page_config(
    page_title="Agent-as-a-Judge RAG",
    page_icon="📄",
    layout="wide"
)


st.title("📄 Agent-as-a-Judge — RAG Chatbot")

st.write(
    "Ask questions about the research paper "
    '"Agent-as-a-Judge: Evaluating Agents with Agents".'
)

st.divider()


question = st.text_input(
    "Ask a question",
    placeholder="e.g., What is the DevAI benchmark?"
)


top_k = st.slider(
    "Number of retrieved chunks",
    min_value=3,
    max_value=8,
    value=5
)


if st.button("Ask Question", type="primary"):

    if not question.strip():

        st.warning("Please enter a question.")

    else:

        with st.spinner("Retrieving evidence and generating answer..."):

            try:

                result = ask_question(
                    question,
                    top_k=top_k
                )

                st.subheader("Answer")

                st.write(result["answer"])


                st.divider()

                st.subheader("Retrieved Evidence")

                for rank, source in enumerate(
                    result["sources"],
                    start=1
                ):

                    with st.expander(
                        f"Source {rank} — "
                        f"Pages {source['start_page']}"
                        f"-{source['end_page']} "
                        f"| Similarity "
                        f"{source['similarity']:.4f}"
                    ):

                        st.write(
                            f"**Chunk:** "
                            f"{source['chunk_id']}"
                        )

                        st.write(
                            f"**Pages:** "
                            f"{source['start_page']}–"
                            f"{source['end_page']}"
                        )

                        st.write(
                            f"**Similarity:** "
                            f"{source['similarity']:.4f}"
                        )

                        st.markdown("**Retrieved text:**")

                        st.write(source["text"])


            except Exception as error:

                st.error(
                    f"An error occurred: {error}"
                )