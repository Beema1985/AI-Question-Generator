# AI Question Generator

A Streamlit-based AI Question Generator interface for **CBSE Class XII Computer Science**.

## Features

- Dashboard-style sidebar navigation
- Topic selection
- Dynamic subtopic selection
- Select All / Clear Selection
- Generate Questions action
- Python, Database Concepts, Computer Networks and Societal Impacts
- UI closely based on the supplied design reference
- GitHub-ready project structure
- Streamlit deployment compatible

## Project Structure

```text
AI_Question_Generator/
├── app.py
├── requirements.txt
├── .gitignore
├── .streamlit/
│   └── config.toml
└── README.md
```

## Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/AI_Question_Generator.git
cd AI_Question_Generator
```

### 2. Create a virtual environment

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the application

```bash
streamlit run app.py
```

The application will open in your browser.

## Deploy on Streamlit Community Cloud

1. Create a new GitHub repository.
2. Upload all files from this project.
3. Open Streamlit Community Cloud.
4. Connect your GitHub repository.
5. Select `app.py` as the main file.
6. Deploy.

No API keys are required for this UI version.

## Important

The current version implements the **interface and selection workflow**. The Generate button currently validates the selected topic/subtopics. The actual AI question-generation engine can be connected later using an API or a local question-generation model.

## License

For educational and project-development use.
