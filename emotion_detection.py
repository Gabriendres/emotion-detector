import requests

def emotion_detector(text_to_analyse):

    emotions = {
        "anger": 0.1,
        "joy": 0.8,
        "sadness": 0.05,
        "fear": 0.02,
        "disgust": 0.03
    }

    dominant_emotion = max(emotions, key=emotions.get)

    return {
        "anger": emotions["anger"],
        "joy": emotions["joy"],
        "sadness": emotions["sadness"],
        "fear": emotions["fear"],
        "disgust": emotions["disgust"],
        "dominant_emotion": dominant_emotion
