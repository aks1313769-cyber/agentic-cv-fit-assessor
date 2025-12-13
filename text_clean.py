import re
from functools import lru_cache

import spacy


WORD_PATTERN = r"\b[a-zA-Z0-9\-\+\.#]+\b"


@lru_cache(maxsize=1)
def _load_nlp():
    """Load spaCy English model with a safe fallback."""
    try:
        return spacy.load("en_core_web_sm")
    except OSError:
        # Fall back to a lightweight English pipeline to avoid import errors
        nlp = spacy.blank("en")
        if "sentencizer" not in nlp.pipe_names:
            nlp.add_pipe("sentencizer")
        return nlp


def clean_text(text):
    tokens = re.findall(WORD_PATTERN, text)
    return list(set(tokens))


def extract_phrases(text):
    nlp = _load_nlp()
    text_lower = text.lower()

    try:
        doc = nlp(text_lower)
        phrases = [chunk.text.strip() for chunk in doc.noun_chunks if len(chunk.text.strip()) > 1]
        if phrases:
            return phrases
    except (AttributeError, ValueError):
        # Missing parser or noun chunk support
        pass

    tokens = re.findall(WORD_PATTERN, text_lower)
    return [" ".join(tokens[i : i + 2]) for i in range(len(tokens) - 1) if len(tokens[i : i + 2]) == 2]
