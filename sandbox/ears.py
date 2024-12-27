import speech_recognition as sr
import pyaudio as pa

from sandbox.mouth import who_speaks

# Initialize the recognizer
recognizer = sr.Recognizer()

language_map = {
    'Portuguese': 'pt-BR',
    'English': 'en-US'
}

def who_listens():
    # Start listening
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        print("Heard something...")

        # Dictionary to store results
        results = {}

        # Try recognizing speech in Portuguese
        try:
            understood_pt = recognizer.recognize_google(audio, language='pt-BR')
            print(f"Detected (Portuguese): {understood_pt}")
            results['Portuguese'] = understood_pt
        except sr.UnknownValueError:
            print("No clear result in Portuguese.")
        except sr.RequestError:
            print("Google API unreachable for Portuguese.")

        # Try recognizing speech in English
        try:
            understood_en = recognizer.recognize_google(audio, language='en-US')
            print(f"Detected (English): {understood_en}")
            results['English'] = understood_en
        except sr.UnknownValueError:
            print("No clear result in English.")
        except sr.RequestError:
            print("Google API unreachable for English.")

        # Analyze results
        if results:
            # Prioritize longer text (assuming it’s more likely accurate)
            detected_language = max(results, key=lambda lang: len(results[lang]))
            print(f"Final detected language: {detected_language}")
            print(f"Recognized text: {results[detected_language]}")

            if detected_language in language_map:
                return results[detected_language], language_map[detected_language]
            else:
                return results[detected_language], "en-US"

        print("Sorry, I couldn't recognize any speech.")
        return None