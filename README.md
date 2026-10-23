# 🎬 Movie Information Extractor

An AI-powered Movie Information Extractor built using **Python, LangChain, Groq, and Streamlit**. It extracts structured movie details from a given paragraph and presents them in a clean, easy-to-read format using a Large Language Model (LLM).

## 🚀 Project Overview

Finding important information about a movie from lengthy text can be time-consuming. This application uses prompt engineering and an LLM to identify relevant movie details and organize them into structured fields.

Simply paste a paragraph about a movie, click **Extract Information**, and get the extracted details within seconds.

## ✨ Features

- 🎥 **Movie Information Extraction** — Extract essential details from movie descriptions.
- 🧠 **LLM-Powered Processing** — Uses Groq-hosted `openai/gpt-oss-20b` through LangChain.
- 📝 **Prompt Engineering** — Uses a structured prompt template to guide the model's response.
- 📊 **Structured Output** — Organizes extracted information into clearly labeled fields.
- 🖥️ **Interactive Streamlit UI** — Provides a simple interface for entering text and viewing results.
- 🔒 **Environment Variable Support** — Loads API credentials securely from a `.env` file.
- ⚠️ **Missing Information Handling** — Instructs the model to return "Not mentioned" when information is unavailable in the input.

## 📋 Information Extracted

The application extracts the following fields:

| Field | Description |
|---|---|
| Movie Name | Title of the movie |
| Release Year | Year of release |
| Release Date | Full release date, if available |
| Genre | Movie genres |
| Director | Director's name |
| Writers | Screenwriters or writers |
| Main Cast | Important actors and mentioned character names |
| Producer(s) | Movie producers |
| Production Companies | Companies involved in production |
| Cinematographer | Cinematography details |
| Filming Locations | Locations mentioned in the text |
| Language | Movie language |
| Country | Country of origin, if mentioned |
| Plot Summary | Overview of the movie's story |
| Quick Summary | Concise 2–3 sentence summary |

## 🛠️ Tech Stack

- **Python** — Core programming language
- **Streamlit** — Web application interface
- **LangChain** — Prompt templates and model integration
- **Groq** — LLM inference platform
- **GPT-OSS-20B** — Language model used for information extraction
- **python-dotenv** — Environment variable management

## 📂 Project Structure

```text
Movie-Information-Extractor/
│
├── app.py              # Streamlit web application
├── core.py             # Standalone command-line extraction script
├── requirements.txt    # Python dependencies
├── .env                # API credentials (not committed to Git)
├── .gitignore          # Excludes sensitive and unnecessary files
└── README.md           # Project documentation
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/movie-information-extractor.git
cd movie-information-extractor
```

Replace `YOUR_USERNAME` with your GitHub username.

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure your API key

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key_here
```

Get an API key from the [Groq Console](https://console.groq.com/).

**Security:** Never commit your `.env` file or expose your API key in public repositories.

### 5. Run the Streamlit application

```bash
streamlit run app.py
```

Open the local URL displayed in your terminal, usually `http://localhost:8501`.

## 💡 How to Use

1. Launch the Streamlit application.
2. Paste a paragraph containing information about a movie.
3. Click **Extract Information**.
4. Wait for the language model to process the text.
5. Review the extracted movie information.
6. Use the **Clear** button to reset the interface and process another movie.

## 🧪 Example Input

```text
Interstellar is a 2014 science fiction film directed by
Christopher Nolan and written by Jonathan Nolan and
Christopher Nolan. The film stars Matthew McConaughey
as Cooper, Anne Hathaway as Amelia Brand, and Jessica
Chastain as Murphy Cooper. It follows a group of
astronauts who travel through a wormhole in search
of a new home for humanity.
```

### Example Output

```text
Movie Name: Interstellar
Release Year: 2014
Release Date: Not mentioned
Genre: Science fiction
Director: Christopher Nolan
Writers: Jonathan Nolan, Christopher Nolan
Main Cast:
- Matthew McConaughey as Cooper
- Anne Hathaway as Amelia Brand
- Jessica Chastain as Murphy Cooper
Producer(s): Not mentioned
Production Companies: Not mentioned
Cinematographer: Not mentioned
Filming Locations: Not mentioned
Language: Not mentioned
Country: Not mentioned

Plot Summary:
A group of astronauts travel through a wormhole
in search of a new home for humanity.

Quick Summary:
Interstellar follows astronauts on a mission through
a wormhole to find a habitable world for humanity.
The story explores space exploration and humanity's
struggle for survival.
```

*Note: The actual model response may vary. The model is instructed to use only information present in the provided text, but LLM outputs are not guaranteed to be perfectly accurate.*

## 🧠 How It Works

1. **User Input:** The user supplies a paragraph about a movie.
2. **Prompt Template:** LangChain's `PromptTemplate` inserts the paragraph into a predefined extraction prompt.
3. **LLM Processing:** The prompt is sent to the Groq-hosted language model.
4. **Information Extraction:** The model generates structured movie details.
5. **Output Display:** Streamlit presents the result to the user.

## 🔑 Environment Variables

The application uses the following environment variable:

| Variable | Purpose |
|---|---|
| `GROQ_API_KEY` | Authenticates requests to the Groq API |

Keep this variable in your local `.env` file. The `.gitignore` file should exclude `.env` from version control.

## ⚠️ Limitations

- The application extracts information from the supplied paragraph; it does not independently search the internet.
- Missing details are marked as "Not mentioned" according to the prompt instructions.
- Output accuracy depends on the quality and completeness of the input text and the language model's response.
- API access, rate limits, and model availability depend on the Groq service and your account.
- The generated plot and quick summaries may omit details from the original text.


## 🎯 Learning Outcomes

This project demonstrates practical experience with:

- Prompt engineering and instruction design
- Large Language Model integration
- LangChain prompt templates
- API-based model inference
- Environment variable management
- Building interactive applications with Streamlit
- Structuring unstructured text into useful information

## 👨‍💻 Author

**Tavprasad Singh**

B.Tech Computer Science and Engineering

Interested in Artificial Intelligence, Machine Learning, Generative AI, and building intelligent applications.

---

⭐ If you find this project useful, consider giving the repository a star!

