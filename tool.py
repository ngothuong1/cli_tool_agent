from datetime import datetime
from langchain_core.tools import tool
from langchain_tavily import TavilySearch

@tool
def get_date() -> str:
    """Get current date in YYYY-MM-DD format."""
    return datetime.now().date().isoformat()

# TavilySearch đọc TAVILY_API_KEY từ environment
tavily_tool = TavilySearch(max_results=3)

@tool
def search(query: str) -> str:
    """Search real-time information from the web."""
    resp = tavily_tool.invoke({"query": query})

    # tùy version, resp có thể là dict {"results":[...]} hoặc list
    results = resp.get("results") if isinstance(resp, dict) else resp

    if not results:
        return "No results found."

    formatted = "\n\n".join(
        f"{r.get('title','')}\n{r.get('content','')}\n{r.get('url','')}".strip()
        for r in results
    )
    return formatted
    # Mock search
    #return f"Search result for '{query}': This is a mock search result"