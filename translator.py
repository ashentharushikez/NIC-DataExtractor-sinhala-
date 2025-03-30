import requests

def is_tamil_text(text):
    """Check if text contains Tamil characters."""
    return any(0x0B80 <= ord(char) <= 0x0BFF for char in text)

def translate_text(text, source_lang='ta', target_lang='si'):
    """Translate text from Tamil to Sinhala using Google Translate API."""
    try:
        url = "https://translate.googleapis.com/translate_a/single"
        params = {"client": "gtx", "sl": source_lang, "tl": target_lang, "dt": "t", "q": text}
        response = requests.get(url, params=params)
        return response.json()[0][0][0] if response.status_code == 200 else text
    except:
        return text

def convert_tamil_to_sinhala(text):
    """Convert any Tamil text to Sinhala."""
    return " ".join(translate_text(word) if is_tamil_text(word) else word for word in text.split())
