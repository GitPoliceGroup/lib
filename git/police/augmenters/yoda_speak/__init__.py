import random
import re
from git.police.augmenters.core import Augmenter

def translate_to_yoda(text):
    """
    Translates English text into Yoda-style speech.
    
    Args:
        text (str): Input English text
        
    Returns:
        str: Yoda-style translated text
    """
    if not text.strip():
        return ""
    
    # Split into sentences
    sentences = re.split(r'([.!?]+)', text)
    translated_sentences = []
    
    for i in range(len(sentences)):
        sentence = sentences[i].strip()
        punctuation = sentences[i+1] if i+1 < len(sentences) else ""
        
        if not sentence:
            continue
            
        # Translate each sentence
        translated = _translate_sentence(sentence)
        translated_sentences.append(translated + punctuation + " ")
        
    result = "".join(translated_sentences).strip()
    return result[0].upper() + result[1:] if len(result) > 1 else result

def _translate_sentence(sentence):
    """Helper function to translate a single sentence to Yoda speech."""
    
    # Split sentence into words
    words = sentence.lower().split()
    if len(words) <= 3:
        return sentence
    
    # Basic Yoda patterns:
    # 1. Object-Subject-Verb: Move last part to front
    # 2. Sometimes keep adjectives with their nouns
    # 3. Keep common phrases together
    
    # Split sentence into parts
    if len(words) >= 5 and random.random() < 0.7:
        # Take last chunk and move to front
        chunk_size = min(3, len(words) // 2)
        front = words[-chunk_size:]
        middle = words[:-chunk_size]
        
        # Reconstruct with Yoda's pattern
        words = front + middle
    
    # Special cases for common phrases
    result = " ".join(words)
    
    # Fix common word patterns
    result = re.sub(r'\b(am|is|are|was|were)\b(.+?)\b(a|an|the)\b', r'\3\2\1', result)
    result = re.sub(r'\b(will|shall)\b(.+?)\b(a|an|the)\b', r'\3\2\1', result)
    
    # Handle negations
    result = re.sub(r'\b(do|does|did)\s+not\b', 'not', result)
    
    # Fix articles at the end
    result = re.sub(r'\s+(a|an|the)\s*$', '', result)
    
    return result

def _is_common_phrase(words, start_idx, phrase_list):
    """Helper function to identify common phrases that should stay together."""
    for phrase in phrase_list:
        phrase_words = phrase.lower().split()
        if len(words) - start_idx >= len(phrase_words):
            if all(words[start_idx + i] == phrase_words[i] for i in range(len(phrase_words))):
                return len(phrase_words)
    return 0

# Example common phrases to keep together (can be expanded)
COMMON_PHRASES = [
    "of course",
    "in fact",
    "as well",
    "at last",
    "after all",
]

class YodaSpeakAugmenter(Augmenter):
    def __init__(self):
        super().__init__(
            "YodaSpeak",
            "Convert text to Yoda Speak"
        )
    
    def augment(self, message):
        return translate_to_yoda(message)