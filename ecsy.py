# This is a sample Python script
import torch
import tensorflow as tf
import pyttsx3


def ml_models(a, b):
    x = torch.rand(a, b)
    y = tf.reduce_sum(x, axis=1)
    print(x, y)


def speak_phrase(phrase):
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    # Set voice properties (macOS uses built-in voices like "Alex")
    voices = engine.getProperty('voices')
    for voice in voices:
        if 'en_US' in voice.id:  # Select an English voice
            engine.setProperty('voice', voice.id)
            break

    # Speak the phrase
    engine.say(phrase)
    engine.runAndWait()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    ml_models(5, 3)
    speak_phrase("Hi! I'm ECSY, and I am ready to serve.")
