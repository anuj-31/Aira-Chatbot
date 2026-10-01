# 🤖 AIRA — Local Chatbot

<p align="center">
  <img src="aira-chatbot.png" alt="AIRA Chatbot" width="900"/>
</p>

<p align="center">
  <b>Your Local AI Assistant powered by Gemma 3:4B, LangChain & Ollama</b>
</p>

<p align="center">
  🔒 100% Local &nbsp; • &nbsp; 🤖 Gemma 3:4B &nbsp; • &nbsp; 🦜 LangChain &nbsp; • &nbsp; 🦙 Ollama
</p>

---

## 📌 About the Project

**AIRA** is a locally running AI chatbot built using **Gemma 3:4B**, **LangChain**, **Ollama**, and **Streamlit**.

The goal of this project is to create a simple AI assistant that can run on a user's own laptop without requiring a paid cloud API.

AIRA uses **Ollama** to run the Gemma 3:4B model locally and **LangChain** to connect the application with the language model.

### ✨ Key Highlights

- 🤖 Powered by **Gemma 3:4B**
- 🦜 Built using **LangChain**
- 🦙 Uses **Ollama** for local LLM inference
- 🖥️ Streamlit-based user interface
- 🔒 Runs completely locally
- 🔑 No OpenAI API key required
- 💰 No paid API required
- 💬 Interactive chatbot interface
- ⚡ Easy to install and customize

---

## 🖥️ Application Preview

<p align="center">
  <img src="aira-chatbot.png" alt="AIRA Chatbot Interface" width="900"/>
</p>

---

## 🧰 Tech Stack

| Technology | Purpose |
|------------|---------|
| 🐍 Python | Core programming language |
| 🤖 Gemma 3:4B | Large Language Model |
| 🦙 Ollama | Local LLM runtime |
| 🦜 LangChain | LLM application framework |
| 🎨 Streamlit | Web-based user interface |

---

## 🏗️ Architecture

```text
                    ┌──────────────────┐
                    │      User        │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │    Streamlit     │
                    │       UI         │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │    LangChain     │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │      Ollama      │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │    Gemma 3:4B    │
                    │     Local LLM    │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │   AI Response    │
                    └──────────────────┘
```

---

# 🚀 Getting Started

Follow the steps below to run AIRA on your own laptop.

## 📋 Prerequisites

Before installing AIRA, make sure you have:

- Python **3.10 or higher**
- Git
- Ollama
- At least **8 GB RAM** recommended
- Several GB of free disk space

A GPU is optional, but a supported GPU can provide faster model inference.

---

## 1️⃣ Clone the Repository

Open your terminal or command prompt:

```bash
git clone https://github.com/aira-chatbot/AIRA.git
cd AIRA
```

---

## 2️⃣ Create a Virtual Environment

Creating a virtual environment is recommended to keep the project dependencies isolated.

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3️⃣ Install Python Dependencies

Install all required Python packages:

```bash
pip install -r requirements.txt
```

If you do not have a `requirements.txt` file, install the main dependencies manually:

```bash
pip install streamlit langchain langchain-ollama
```

---

## 4️⃣ Install Ollama

AIRA uses **Ollama** to run Gemma 3:4B locally.

Download and install Ollama:

**https://ollama.com/**

After installation, verify it:

```bash
ollama --version
```

---

## 5️⃣ Download Gemma 3:4B

Pull the model:

```bash
ollama pull gemma3:4b
```

Check the installed models:

```bash
ollama list
```

You should see:

```text
NAME
gemma3:4b
```

---

## 6️⃣ Test Gemma 3:4B

Before running AIRA, test the model directly:

```bash
ollama run gemma3:4b
```

Try:

```text
What is machine learning?
```

If Gemma responds correctly, your Ollama setup is ready.

To exit:

```text
/bye
```

---

## 7️⃣ Run AIRA

Start the Streamlit application:

```bash
streamlit run app.py
```

Open the local URL shown in the terminal, usually:

**http://localhost:8501**

🎉 **AIRA is now running locally on your laptop!**

---

## 📁 Project Structure

```text
AIRA/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
└── aira-chatbot.png
```

### `app.py`

Contains the main Streamlit application and LangChain + Ollama integration.

### `requirements.txt`

Contains the Python dependencies required to run AIRA.

### `assets/`

Contains screenshots and other project assets.

---

## 🔐 Privacy

AIRA is designed to run **locally on your own machine**.

The basic workflow is:

```text
User Message
     │
     ▼
Streamlit
     │
     ▼
LangChain
     │
     ▼
Ollama
     │
     ▼
Gemma 3:4B
     │
     ▼
AI Response
```

No OpenAI API key or other paid LLM API is required.

---

## 💡 Example Prompts

Try asking AIRA:

```text
Explain machine learning in simple terms.
```

```text
Write a Python binary search function.
```

```text
What is Retrieval Augmented Generation?
```

```text
Explain OOP concepts in Python.
```

```text
Help me debug this Python code.
```

```text
Explain the difference between supervised and unsupervised learning.
```

---

## 🔄 Changing the Model

Ollama supports multiple local models.

For example:

```bash
ollama pull llama3.2
```

Then change the model name in your Python code:

```python
model = "llama3.2"
```

The exact code may vary depending on how the LangChain model is initialized.

---

## 🛠️ Troubleshooting

### ❌ Model Not Found

If you see:

```text
model 'gemma3:4b' not found
```

Run:

```bash
ollama pull gemma3:4b
```

Then verify:

```bash
ollama list
```

Make sure `gemma3:4b` appears in the list.

### ❌ Ollama Connection Error

Make sure Ollama is running.

Test it:

```bash
ollama run gemma3:4b
```

If required, start the Ollama server:

```bash
ollama serve
```

Then restart the Streamlit application:

```bash
streamlit run app.py
```

### ❌ `OllamaEndpointNotFoundError: 404`

This usually occurs when the application tries to use a model that is not available in Ollama.

Check:

```bash
ollama list
```

If `gemma3:4b` is missing:

```bash
ollama pull gemma3:4b
```

Make sure the model name in your Python code exactly matches:

```text
gemma3:4b
```

### 🐌 Slow Responses

Local LLM performance depends on your hardware.

If responses are slow:

- Make sure enough RAM is available
- Close unnecessary applications
- Use a supported GPU if available
- Check that Ollama is configured correctly
- Consider using a smaller model

---

## 💻 Hardware

The exact requirements depend on the operating system and Ollama configuration.

A practical setup for Gemma 3:4B is:

| Component | Recommendation |
|-----------|----------------|
| RAM | 8 GB+ |
| CPU | Modern multi-core processor |
| GPU | Optional |
| Storage | Several GB available |
| OS | Windows / Linux / macOS |

> Performance can vary depending on your CPU, GPU, RAM, and system configuration.

---

## 🔮 Future Improvements

- [ ] Conversation memory
- [ ] Persistent chat history
- [ ] Streaming responses
- [ ] RAG implementation
- [ ] PDF document Q&A
- [ ] Multiple model selection
- [ ] Voice input
- [ ] Voice output
- [ ] Improved UI/UX
- [ ] Docker support
- [ ] Additional deployment options

---

## 🤝 Contributing

Contributions are welcome!

### 1. Fork the repository

### 2. Create a new branch

```bash
git checkout -b feature/new-feature
```

### 3. Make your changes

### 4. Commit your changes

```bash
git add .
git commit -m "Add new feature"
```

### 5. Push your branch

```bash
git push origin feature/new-feature
```

### 6. Open a Pull Request

---

## 👨‍💻 Author

### Randhir Kumar

**B.Tech — Metallurgical & Materials Engineering**  
**NIT Jamshedpur**

### Areas of Interest

- Artificial Intelligence
- Machine Learning
- Deep Learning
- Generative AI
- Computer Vision
- Data Science
- Data Structures & Algorithms

---

## ⭐ Support

If you found **AIRA** useful, consider giving the repository a ⭐ on GitHub.

```text
⭐ Star the repository
🍴 Fork the repository
🛠️ Modify the project
🚀 Build something cool
```

---

## 📜 License

This project is licensed under the **MIT License**.
