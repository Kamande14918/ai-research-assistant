def format_citations(results):
    citations =[]
    for i, r in enumerate(results):
        citation = f"[{i+1}] {r['title']}. {r['url']}"
        citations.append(citation)
    return citations