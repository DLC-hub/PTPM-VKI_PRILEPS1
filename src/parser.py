import requests
from bs4 import BeautifulSoup
from src.config import DEFAULT_HEADERS, HTML_SELECTORS
from src.exceptions import DuplicateRecordError


class ForumParser:
    def parse_page(self, url):
        response = requests.get(url, headers=DEFAULT_HEADERS)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'lxml')
        posts = soup.select(HTML_SELECTORS["post_container"])
        parsed = []

        for post in posts:
            post_id = post.get(HTML_SELECTORS["post_id_attr"])
            if not post_id:
                continue

            author_tag = post.select_one(HTML_SELECTORS["author"])
            author = author_tag.get_text(strip=True) if author_tag else "Unknown"

            content_tag = post.select_one(HTML_SELECTORS["content"])
            content = str(content_tag) if content_tag else ""

            parsed.append({
                "id": int(post_id),
                "name": author,
                "message": content
            })

        return parsed

    def save_to_db(self, parsed_data, db):
        for item in parsed_data:
            try:
                db.add(item["id"], item["name"], item["message"])
            except DuplicateRecordError:
                continue