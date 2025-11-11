# Text-Cleaning-And-Analysis
Automated text cleaning and visualization pipeline for generating insights from raw text data, leveraging common NLP techniques

# 🧠 NLP-Text-Pipeline

A scalable and reusable text preprocessing and visualization pipeline for **Natural Language Processing (NLP)** workflows.  
This project automates text cleaning, normalization, and visualization — enabling analysts and data scientists to quickly prepare text data for further NLP tasks.

---

## 🚀 Features

- Comprehensive text preprocessing:
  - Lowercasing
  - Punctuation and number removal
  - Stopword elimination
  - Lemmatization with **TextBlob**
  - Rare word filtering
- Built-in visualization tools:
  - Frequency-based **Barplot**
  - **Word Cloud** generation
- Modular, dataset-agnostic structure
- Ready for integration into larger NLP pipelines

---

## 🗂️ Project Structure

NLP-Text-Pipeline/
┣ 📄 README.md
┣ 📄 requirements.txt
┣ 📄 NLP-Text-Pipeline.py
┣ 📂 data/
┃ ┗ 📄 your_text_data.csv
┗ 📂 outputs/
┗ 📄 visualizations/


---

## 💻 Installation

Clone the repository and install the required dependencies.

git clone https://github.com/yourusername/NLP-Text-Pipeline.git
cd NLP-Text-Pipeline
pip install -r requirements.txt

---

🧩 Usage

Place your dataset in the data/ directory.
Your dataset should contain a column named text with the text entries to be processed.

Then run:

python text_pipeline.py


or within a notebook:

import pandas as pd
from text_pipeline import text_pipeline

df = pd.read_csv("data/your_text_data.csv", index_col=0)
df = text_pipeline(df, Barplot=True, Wordcloud=True)
print(df[['text', 'cleaned_text']].head())

📊 Example Output

Cleaned text sample:

Original Text	Cleaned Text
"The quick brown fox..."	"quick brown fox"

Visualizations:

Term frequency barplot

Word cloud of top terms
