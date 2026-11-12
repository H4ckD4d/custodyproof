# Public web research using Google + Gemini

The `research` command optionally uses the Gemini API with the **Google Search grounding** tool. It is not Google HTML scraping and it does not depend on the deprecated Custom Search JSON API for new customers.

```bash
python3 -m pip install -e '.[ai]'
export GEMINI_API_KEY='YOUR_OWN_API_KEY'
export GEMINI_MODEL='gemini-2.5-flash'
custodyproof research --lang pt
```

The configured topic is sent to Google. Do not use customer details, private records, emails, secrets or identifiable persons. Review quota and billing. External results have not been tested as part of the offline unit tests.

Docs: https://ai.google.dev/gemini-api/docs/google-search
