import requests
import feedparser
import streamlit as st

NEWS_API_KEY = st.secrets.get("NEWSAPI_KEY", "")
GNEWS_API_KEY = st.secrets.get("GNEWS_API_KEY", "")

def fetch_newsapi(segment, date):
    if not NEWS_API_KEY:
        return []
    try:
        url = "https://newsapi.org/v2/everything"
        params = {
            "q": segment,
            "from": date,
            "to": date,
            "language": "en",
            "sortBy": "relevancy",
            "apiKey": NEWS_API_KEY,
        }
        res = requests.get(url, params=params, timeout=5)
        return res.json().get("articles", [])
    except:
        return []

def fetch_gnews(segment, date):
    if not GNEWS_API_KEY:
        return []
    try:
        url = "https://gnews.io/api/v4/search"
        params = {
            "q": segment,
            "from": date,
            "to": date,
            "lang": "en",
            "token": GNEWS_API_KEY,
        }
        res = requests.get(url, params=params, timeout=5)
        return res.json().get("articles", [])
    except:
        return []

def fetch_rss(segment):
    rss_map = {
        "Technology": "https://feeds.bbci.co.uk/news/technology/rss.xml",
        "Business": "https://feeds.bbci.co.uk/news/business/rss.xml",
        "Sports": "https://feeds.bbci.co.uk/sport/rss.xml",
        "Health": "https://feeds.bbci.co.uk/news/health/rss.xml",
        "Entertainment": "https://feeds.bbci.co.uk/news/entertainment_and_arts/rss.xml",
        "Politics": "https://feeds.bbci.co.uk/news/politics/rss.xml",
    }

    feed = feedparser.parse(rss_map.get(segment, ""))
    articles = []
    for e in feed.entries:
        articles.append({
            "title": e.title,
            "description": e.get("summary", ""),
            "source": "BBC (RSS)"
        })
    return articles

@st.cache_data(show_spinner=False)
def collect_news(segment, date):
    articles = []
    articles += fetch_newsapi(segment, date)
    articles += fetch_gnews(segment, date)

    # Fallback if APIs fail or hit limits
    if len(articles) < 5:
        articles += fetch_rss(segment)

    return articles
