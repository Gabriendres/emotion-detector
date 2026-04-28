import requests

def emotion_detector(text_to_analyse):

    url = "https://api.us-south.natural-language-understanding.watson.cloud.ibm.com/v1/analyze"

    params = {
        "features": "emotion",
        "text": text_to_analyse
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        return None
