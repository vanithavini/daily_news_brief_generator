# 🗞️ Daily News Brief Generator

In today’s information-heavy digital world, users often struggle with information overload when consuming news from multiple platforms.
This project presents an AI-based Daily News Brief Generator that aggregates news from multiple sources, summarizes it using NLP models, and delivers personalized, concise daily briefs to users via a clean Streamlit interface.

The system focuses on:
- Personalization
- Clarity
- Multi-source aggregation
- AI-powered summarization
- Ease of use

## 🚀 Features

- 🔐 User login with saved preferences
- 📰 News from multiple sources:
  - NewsAPI
  - GNews
  - BBC RSS (fallback)
- 🤖 AI summarization using T5 Transformer
- 🎛️ Short or detailed summaries
- ⚡ Cached data for fast performance
- 📂 Simple JSON-based user storage


## 🛠️ Tech Stack

Layer	       Technology
*****          **********
Backend	        Python
Frontend	    Streamlit
AI / NLP	    HuggingFace Transformers
Model	        T5-small
News Sources	NewsAPI, GNews, RSS feeds
Storage	        JSON (user preferences)
Deployment	    Streamlit Cloud

## 📁 Project Structure

daily_news_brief_generator/
│
├── .streamlit/secrets.toml      # APIs Tokens(Keys) setup
├── app.py                       # Streamlit frontend
├── news_fetcher.py              # Fetch news from APIs & RSS
├── summarizer.py                # AI summarization logic
├── utils.py                     # Helper utilities
├── users.json                   # User preferences storage
├── requirements.txt
└── README.md


## 🔐 API Keys & Secrets
Supported Keys 
- NEWSAPI_KEY
- GNEWS_API_KEY
- HF_TOKEN 

## 🔄 Application Flow
- User opens the app
- User logs in
- First-time users select preferred segments
- Home page shows personalized daily brief
- User can:
    Change category
    Change date
    Change summary length
- AI regenerates the news brief instantly

## 📦Installation
git clone 
cd daily-news-brief-generator
pip install -r requirements.txt

## ▶️ Run the App locally
streamlit run app.py

## 🌍 Deployment
Deployed using Streamlit Cloud
Publicly accessible URL
No local setup required for judges

## 📎 Future Enhancements
Multi-language briefs
Topic-level personalization
Email delivery of daily briefs
Lightweight summarization fallback model 


