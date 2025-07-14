import speech_recognition as sr
import webbrowser
import pyttsx3
import Mymusic
import requests
from openai import OpenAI
from gtts import gTTS
import pygame
import os

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "ef7d1784fc334280a0d388d14e7cf617"

def speak_old(text):
    engine.say(text)
    engine.runAndWait()

def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3')

    # Initialize Pygame mixer
    pygame.mixer.init()

    # Load the MP3 file
    pygame.mixer.music.load('temp.mp3')

    # Play the MP3 file
    pygame.mixer.music.play()

    # Keep the program running until the music stops playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    
    pygame.mixer.music.unload()
    os.remove("temp.mp3")

def aiProcess(command):
    """
    Processes the user command using the NVIDIA API or any other AI-based API.
    """
    try:
        # Initialize the OpenAI client with NVIDIA's LLM service.
        client = OpenAI(
            base_url="https://integrate.api.nvidia.com/v1",
            api_key="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"
        )
        
        # Generate completion from the model
        completion = client.chat.completions.create(
            model="nvidia/llama-3.1-nemotron-70b-instruct",
            messages=[{"role": "user", "content": command}],
            temperature=0.3,
            top_p=0.8,
            max_tokens=100,
            stream=False  # Stream=False since streaming implementation is not handled here
        )
        
        # Extract and return the text content from the response
        return completion.choices[0].message.content if completion.choices else "No response generated."
    
    except Exception as e:
        return f"Error in processing your request: {str(e)}"



def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")    
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = Mymusic.music.get(song, None)
        if link:
            webbrowser.open(link)
        else:
            speak(f"Sorry, I couldn't find the song {song} in your library.")
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        
        if r.status_code == 200:
            # Parse the JSON response
            data = r.json()
            
            # Extract the articles
            articles = data.get('articles', [])
            
            # Read the headlines
            for article in articles[:5]:  # Limit to top 5 headlines
                speak(article['title'])
        else:
            speak("Sorry, I couldn't fetch the news at the moment.")
    else:
        # Let Gemini handle the request
        output = aiProcess(c)
        speak(output)

def main():
    speak("Initializing Kim....")
    wake_word_detected = False
    while True:
        try:
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source)
                if not wake_word_detected:
                    print("Listening for wake word...")
                    audio = recognizer.listen(source)
                    word = recognizer.recognize_google(audio)
                    if word.lower() in ["kim", "kym", "keem", "hello", "hi","helllo","hey","hiii","hallo","helo"]:
                        speak("Yes")
                        wake_word_detected = True
                else:
                    print("Kim Active...")
                    audio = recognizer.listen(source)
                    command = recognizer.recognize_google(audio)
                    processCommand(command)

        except sr.UnknownValueError:
            print("Sorry, I did not understand the audio.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
        except Exception as e:
            print(f"Error; {e}")

if __name__=="__main__":
    main()