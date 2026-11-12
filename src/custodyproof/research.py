"""Opt-in Gemini API research, grounded with Google Search (public topics only)."""
import os

def lookup(topic: str, lang: str = "pt") -> dict:
    key = os.getenv("GEMINI_API_KEY")
    if not key:
        raise RuntimeError("GEMINI_API_KEY is missing; this optional feature is disabled.")
    try:
        from google import genai
        from google.genai import types
    except ImportError as exc:
        raise RuntimeError("Install the optional SDK: pip install -e '.[ai]'") from exc
    language = {"pt": "Portuguese", "en": "English", "es": "Spanish"}.get(lang, "Portuguese")
    prompt = (f"Answer in {language}. Research only publicly available technical standards, "
              "official documentation and defensive best practices. Include citations and "
              "distinguish uncertain information. Never disclose private data or provide "
              "unauthorized attack instructions. Topic: " + topic[:300])
    client = genai.Client(api_key=key)
    response = client.models.generate_content(
        model=os.getenv("GEMINI_MODEL", "gemini-2.5-flash"),
        contents=prompt,
        config=types.GenerateContentConfig(tools=[types.Tool(google_search=types.GoogleSearch())]))
    sources = []
    for candidate in getattr(response, "candidates", None) or []:
        meta = getattr(candidate, "grounding_metadata", None)
        for chunk in getattr(meta, "grounding_chunks", None) or []:
            web = getattr(chunk, "web", None)
            url = getattr(web, "uri", None)
            if isinstance(url, str) and url.startswith("https://") and url not in sources:
                sources.append(url)
    return {"answer": response.text or "", "sources": sources, "topic": topic, "language": lang}
