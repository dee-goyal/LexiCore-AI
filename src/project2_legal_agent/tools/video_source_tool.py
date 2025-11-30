import requests
from urllib.parse import quote

try:
    from crewai.tools import BaseTool
except ImportError:
    class BaseTool:
        pass

class LawMediaSourceTool(BaseTool):
    name: str = "Law Media Source Tool"
    description: str = "Finds relevant YouTube videos and web articles for a legal query."

    def _run(self, query: str):
        videos = youtube_search(query)
        articles = web_search(query)
        return {
            "videos": videos,
            "articles": articles
        }

def youtube_search(query, max_results=3):
    """Search YouTube for law-related videos and return a list of video URLs."""
    search_url = f"https://www.youtube.com/results?search_query={quote(query + ' law explanation')}"
    return [
        f"YouTube search for '{query}': {search_url}",
        "(For production, use YouTube Data API or youtube-search-python to get direct video links.)"
    ]

def web_search(query, max_results=3):
    """Search the web for law-related articles (demo: returns a Google search URL)."""
    search_url = f"https://www.google.com/search?q={quote(query + ' law explanation')}"
    return [
        f"Google search for '{query}': {search_url}",
        "(For production, use Google Custom Search API or BeautifulSoup to extract real links.)"
    ]

LawMediaSourceToolInstance = LawMediaSourceTool()
