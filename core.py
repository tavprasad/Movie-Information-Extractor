#Prompt Templates
from dotenv import load_dotenv
load_dotenv()

from langchain.chat_models import init_chat_model
model = init_chat_model(
    "groq:openai/gpt-oss-20b",
    temperature=0.8
)    




from langchain_core.prompts import PromptTemplate

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

para=input("Give your Paragraph: ")

final_prompt = prompt.invoke({
    "movie_text": para
})

response=model.invoke(final_prompt)

print(response.content)