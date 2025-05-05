import requests
from bs4 import BeautifulSoup
import json
import time

BASE_URL = "https://matchtv.ru"
NEWS_URL = f"{BASE_URL}/news"


def get_news_list(num_news=500):
    news_items = []
    page = 1
    while len(news_items) < num_news:
        response = requests.get(f"{NEWS_URL}?page={page}")
        if response.status_code != 200:
            print(f"Ошибка при загрузке страницы {page}")
            break

        soup = BeautifulSoup(response.text, "html.parser")
        articles = soup.find_all("a", class_="node-news-list__item")
        for article in articles:
            href = article.get("href")
            full_url = BASE_URL + href
            title_elem = article.find("div", class_="node-news-list__title")
            title = title_elem.get_text(strip=True) if title_elem else "Нет заголовка"
            topic_elem = article.find_all("li", class_="credits__item")
            topic = topic_elem[1].get_text(strip=True) if topic_elem else "Нет темы"
            news_items.append({
                "url": full_url,
                "title": title,
                "topic": topic
            })
            if len(news_items) >= num_news:
                break

        time.sleep(0.5)
    return news_items


def get_article_text(url):
    response = requests.get(url)
    if response.status_code != 200:
        return "Ошибка загрузки текста"
    soup = BeautifulSoup(response.text, "html.parser")
    content_div = soup.find("div", class_="article__content")
    if not content_div:
        return "Нет основного текста"
    paragraphs = content_div.find_all("p")
    text = "\n".join(p.get_text(strip=True) for p in paragraphs)
    return text


def collect_full_news(num_news=500):
    news_list = get_news_list(num_news)
    for i, news in enumerate(news_list):
        news["text"] = get_article_text(news["url"])
        time.sleep(0.5)
    return news_list


all_news = collect_full_news(num_news=500)
with open("matchtv_news_details.json", "w", encoding="utf-8") as f:
    json.dump(all_news, f, ensure_ascii=False, indent=4)
