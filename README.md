# 🌐 Multilingual Text Handler

A simple Python utility for detecting language, transliterating text into ASCII, and tokenizing multilingual input using `langdetect`, `unidecode`, and `nltk`.

---

## 📦 Installation

Install the required dependencies:

```bash
pip install langdetect unidecode nltk
```

## ⚙️ How It Works

The function processes text in three steps:

Language Detection → Uses langdetect to identify the language

Transliteration → Converts non-ASCII characters using unidecode

Tokenization → Splits text into tokens using NLTK

## 📌 Output Example

Original Text: Привет, как дела?

Language: ru

Transliterated Text: Privet, kak dela?

Tokens: ['Privet', ',', 'kak', 'dela', '?']

## ⚠️ Notes

Language detection may be inaccurate for very short texts
Transliteration is approximate, not phonetic
Mixed-language input may produce imperfect tokenization

