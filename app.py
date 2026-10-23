import streamlit as st
from dotenv import load_dotenv

from langchain.chat_models import init_chat_model
from langchain_core.prompts import PromptTemplate


# --------------------------------------------------
# Configuration
# --------------------------------------------------

load_dotenv()

st.set_page_config(
    page_title="Movie Information Extractor",
    page_icon="🎬",
    layout="wide"
)


# --------------------------------------------------
# Custom CSS
# --------------------------------------------------

st.markdown("""
<style>

    /* Main container */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1100px;
    }

    /* Main title */
    .main-title {
        text-align: center;
        font-size: 42px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        font-size: 17px;
        margin-bottom: 35px;
    }

    /* Section headings */
    .section-title {
        font-size: 22px;
        font-weight: 600;
        margin-top: 10px;
        margin-bottom: 10px;
    }

    /* Info cards */
    .info-card {
        padding: 18px;
        border-radius: 12px;
        border: 1px solid rgba(128, 128, 128, 0.25);
        margin-bottom: 12px;
    }

    .info-label {
        font-size: 13px;
        font-weight: 600;
        opacity: 0.7;
        margin-bottom: 4px;
    }

    .info-value {
        font-size: 17px;
        font-weight: 500;
    }

    /* Summary box */
    .summary-box {
        padding: 20px;
        border-radius: 12px;
        border: 1px solid rgba(128, 128, 128, 0.25);
        line-height: 1.7;
        margin-bottom: 15px;
    }

    /* Footer */
    .footer {
        text-align: center;
        margin-top: 40px;
        opacity: 0.6;
        font-size: 14px;
    }

</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# Model
# --------------------------------------------------

@st.cache_resource
def load_model():

    return init_chat_model(
        "groq:openai/gpt-oss-20b",
        temperature=0.8
    )


model = load_model()


# --------------------------------------------------
# Prompt Template
# --------------------------------------------------

template = """
You are an expert movie information extraction assistant.

Extract useful and important information about the movie from the given text.

Return the information in the following format:

Movie Name:
Release Year:
Release Date:
Genre:
Director:
Writers:
Main Cast:
Producer(s):
Production Companies:
Cinematographer:
Filming Locations:
Language:
Country:
Plot Summary:
Quick Summary:

Rules:
1. Extract information only from the provided text.
2. Do not make up or assume information that is not present.
3. If a field is not available, write "Not mentioned".
4. For Main Cast, list the important actors and their character names only if the character names are mentioned.
5. For Genre, include all genres explicitly mentioned.
6. For Quick Summary, give a concise 2-3 sentence summary of the movie's story and premise.
7. Keep the extracted information clear and concise.

Movie Text:
{movie_text}
"""

prompt = PromptTemplate(
    template=template,
    input_variables=["movie_text"]
)


# --------------------------------------------------
# UI
# --------------------------------------------------

st.markdown(
    '<div class="main-title">🎬 Movie Information Extractor</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Extract structured movie information from any paragraph using LangChain + Groq'
    '</div>',
    unsafe_allow_html=True
)


# --------------------------------------------------
# Input
# --------------------------------------------------

st.markdown(
    '<div class="section-title">📄 Movie Paragraph</div>',
    unsafe_allow_html=True
)

movie_text = st.text_area(
    "Paste your movie paragraph below",
    height=280,
    placeholder=(
        "Example:\n\n"
        "Interstellar is a 2014 science fiction drama film directed by "
        "Christopher Nolan..."
    ),
    label_visibility="collapsed"
)


# --------------------------------------------------
# Buttons
# --------------------------------------------------

col1, col2, col3 = st.columns([1, 1, 3])

with col1:
    extract_button = st.button(
        "🔍 Extract Information",
        use_container_width=True,
        type="primary"
    )

with col2:
    clear_button = st.button(
        "🗑️ Clear",
        use_container_width=True
    )


# --------------------------------------------------
# Clear
# --------------------------------------------------

if clear_button:
    st.rerun()


# --------------------------------------------------
# Extraction
# --------------------------------------------------

if extract_button:

    if not movie_text.strip():

        st.warning("⚠️ Please enter a movie paragraph first.")

    else:

        with st.spinner("🎬 Extracting movie information..."):

            try:

                final_prompt = prompt.invoke({
                    "movie_text": movie_text
                })

                response = model.invoke(final_prompt)

                result = response.content

                st.session_state["movie_result"] = result

            except Exception as e:

                st.error(
                    f"❌ Something went wrong while processing the movie:\n\n{e}"
                )


# --------------------------------------------------
# Display Result
# --------------------------------------------------

if "movie_result" in st.session_state:

    st.divider()

    st.markdown(
        '<div class="section-title">🎥 Extracted Movie Information</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="summary-box">',
        unsafe_allow_html=True
    )

    st.markdown(st.session_state["movie_result"])

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )


# --------------------------------------------------
# Footer
# --------------------------------------------------

st.markdown(
    '<div class="footer">'
    'Built with LangChain • Groq • Streamlit'
    '</div>',
    unsafe_allow_html=True
)
