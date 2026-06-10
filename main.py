from langdetect import detect
from unidecode import unidecode
from nltk.tokenize import word_tokenize
import nltk

#Download the necessary resources for NLTK
nltk.download('punkt_tab')

def handle_multilingual_text(text):
    #Detect the language of the input text
    try:
        language = detect(text)
    except:
        language = 'unknown'

    #Transliterate the text to ASCII
    transliterated_text = unidecode(text)
    #Tokenize the text
    tokens = word_tokenize(transliterated_text)
    return {
        'original_text': text,
        'language': language,
        'transliterated_text': transliterated_text,
        'tokens': tokens
    }


##Example usage

texts = [
    "Hello, how are you?",  # English
    "Hola, ¿cómo estás?",  # Spanish
    "你好，你怎么样？",  # Chinese
    "Привет, как дела?",  # Russian
    "مرحبا، كيف حالك؟"  # Arabic
    "Hello, 你好, Привет!"  # Mixed language
]

for text in texts:
    result = handle_multilingual_text(text)
    print(f"Original Text: {result['original_text']}")
    print(f"Language: {result['language']}")
    print(f"Transliterated Text: {result['transliterated_text']}")
    print(f"Tokens: {result['tokens']}")
    print("-" * 50)