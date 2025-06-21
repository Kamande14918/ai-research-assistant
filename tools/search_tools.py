from langchain_community.utilities.tavily_search import TavilySearchAPIWrapper

def search_web(query):
    search = TavilySearchAPIWrapper()
    raw_results = search.results(query=query, max_results=5)
    results = "\n\n".join([f"Title: {r['title']}\nURL: {r['url']}\nSnippet: {r['content']}" for r in raw_results])
    return results
