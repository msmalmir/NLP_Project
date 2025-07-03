import wikipedia 
from textblob import TextBlob

def search_wikipedia(name):
    """
    Search Wikipedia for the given name.
    """
    results = wikipedia.search(name)
    print(f"Search results for '{name}':")
    return results

def summarize_wikipedia(name):
    """
    Summarize the Wikipedia page for the given name.
    """
    summary = wikipedia.summary(name)
    print(f"Summary for '{name}':")
    return summary

def get_text_blob(text):
    """
    Get a TextBlob object for the given text.
    """
    blob = TextBlob(text)
    return blob

def get_phrases(name):
    """
    Get noun phrases from the given text.
    """
    text = summarize_wikipedia(name)
    blob = get_text_blob(text)
    phrases = blob.noun_phrases
    return phrases