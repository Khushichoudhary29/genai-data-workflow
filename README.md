# GenAI Data Workflow – Amazon Review Insight Generator

## 📌 Project Overview

This project implements an **end-to-end GenAI-powered data workflow** that transforms raw Amazon product reviews into meaningful business insights using a **local Large Language Model (LLM)**.

Unlike traditional sentiment analysis projects that rely on keyword matching or numerical scores, this system leverages **semantic reasoning** via a Generative AI model to extract:

* Common positive themes
* Frequent customer complaints
* Overall qualitative sentiment

The entire pipeline runs **locally and offline**, avoiding paid APIs and ensuring full control over data and inference.

---

## 🧠 Why This Project Matters

Modern data workflows increasingly combine **structured data processing** with **unstructured GenAI reasoning**. This project demonstrates:

* Practical GenAI integration (not just theory)
* Real-world dataset handling (Amazon reviews)
* Cost-free, production-inspired architecture using local models

This mirrors how GenAI is applied in **product analytics, customer feedback mining, and decision intelligence systems**.

---

## 🏗️ System Architecture

```
Amazon Reviews CSV
        │
        ▼
Data Ingestion (ingest.py)
        │
        ▼
Text Preprocessing (preprocess.py)
        │
        ▼
Prompt Construction
        │
        ▼
Local GenAI Model (LLaMA3 via Ollama)
        │
        ▼
Insight Generation (genai.py)
```

---

## 📂 Project Structure

```
genai-data-workflow/
│
├── data/
│   └── amazon_reviews.csv
│
├── src/
│   ├── ingest.py        # Load and validate dataset
│   ├── preprocess.py   # Clean and prepare review text
│   └── genai.py         # Generate insights using local LLM
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Technologies Used

* **Python 3.10+**
* **Pandas** – data manipulation and preprocessing
* **Ollama** – local LLM runtime
* **LLaMA3** – Generative AI model for semantic analysis

---

## 🚀 How to Run the Project

### 1️⃣ Create and activate virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Ensure Ollama is running and LLaMA3 is installed

```bash
ollama pull llama3
```

### 4️⃣ Run the GenAI pipeline

```bash
python src/genai.py
```

---

## 🧪 Sample Output

The model produces human-readable analytical insights such as:

* **Common Positive Themes** (e.g., battery life, performance)
* **Common Complaints** (e.g., overheating, camera quality)
* **Overall Sentiment** (Positive / Mixed / Negative)

This output can be directly consumed by product teams, analysts, or decision-makers.

---

## 🧩 How the Project Works (Step-by-Step)

1. Amazon product reviews are loaded from a CSV dataset.
2. Review text is cleaned, validated, and prepared for GenAI processing.
3. Cleaned text is injected into a structured prompt.
4. A local LLaMA3 model analyzes the text semantically.
5. High-level insights are generated instead of raw sentiment scores.

---

## 🔒 Why Local GenAI (No APIs)

* No API key management issues
* No rate limits
* No data privacy risks
* Zero cost
* Fully reproducible

This approach reflects **enterprise-friendly GenAI experimentation**.

---

## 📈 Future Enhancements

* Batch processing for large datasets
* Persist insights to files or databases
* Product-wise comparison dashboards
* Topic clustering using embeddings
* CLI arguments for dynamic inputs

---

## ⭐ Final Note

This project is designed to showcase **applied GenAI engineering**, not just API usage. It bridges traditional data pipelines with modern AI reasoning — a skill set increasingly demanded in industry.
