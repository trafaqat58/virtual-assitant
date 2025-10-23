import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import google.generativeai as genai
import time
import os
import requests
import subprocess
from openai import OpenAI

# Initialize pyttsx3 engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[132].id)  # Female voice
engine.setProperty('rate', 170)

# Speak function
def speak_old(text):
    engine.say(text)
    engine.runAndWait()
    
newsapi = "enter your key"
# client = OpenAI(
#     api_key="enter you key",  # Replace with your actual key
#     base_url="https://api.deepseek.com"
# )



# Gemini AI setup
genai.configure(api_key="enter your key")
def aiProcess(c):
   try:
       model = genai.GenerativeModel("gemini-2.5-flash")
       response = model.generate_content(
           "You are a virtual assistant named Friday. Give two line and useful responses only.\nUser: " + c
       )
       return response.text
   except Exception as e:
       print("❌ Error from Gemini:", e)
       return "AI response failed."


# Command processor

def processCommand(c):
    c = c.lower()

    if "open google" in c:
        webbrowser.open("https://www.google.com/")
    elif "open facebook" in c:
        webbrowser.open("https://www.facebook.com/")
    elif "open youtube" in c:
        webbrowser.open("https://www.youtube.com/")
    elif "open linkedin" in c:
        webbrowser.open("https://www.linkedin.com/")
    elif c.startswith("play "):
        song = c.split("play ")[1]
        link = musicLibrary.music.get(song)
        if link:
            webbrowser.open(link)
        else:
            speak_old("I couldn't find that song.")
    elif "spotify" in c:
        os.system("open -a 'Spotify'")
    elif "whatsapp" in c:
        os.system("open -a 'WhatsApp'")
 
    elif "close spotify" in c.lower():
      try:
        # First try to quit Spotify gracefully
        result = subprocess.run(
            ["osascript", "-e", "tell application \"Spotify\" to quit"],
            capture_output=True,
            text=True
        )
        
        # Wait a moment for graceful quit
        time.sleep(2)
        
        # Check if Spotify is still running and force kill if necessary
        check_result = subprocess.run(
            ["pgrep", "-f", "Spotify"],
            capture_output=True,
            text=True
        )
        
        if check_result.returncode == 0:  # Spotify is still running
            # Force kill Spotify processes
            kill_result = subprocess.run(
                ["pkill", "-9", "-f", "Spotify"],
                capture_output=True,
                text=True
            )
            
            # Verify it's actually closed
            time.sleep(1)
            final_check = subprocess.run(
                ["pgrep", "-f", "Spotify"],
                capture_output=True,
                text=True
            )
            
            if final_check.returncode != 0:  # No processes found
                speak_old("Spotify closed successfully.")
            else:
                speak_old("Spotify is still running. Please close it manually.")
        else:
            speak_old("Spotify closed successfully.")
            
      except Exception as e:
        print("❌ Error:", e)
        speak_old("Something went wrong while closing Spotify.")





    elif "news" in c:
        try:
            r = requests.get(f"https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=0bd53b4b7b8c43fdbb33e75256576927")
            if r.status_code == 200:
                data = r.json()
                articles = data.get('articles', [])
                if articles:
                    speak_old("Here are the latest headlines:")
                    for i, article in enumerate(articles[:5]):
                        speak_old(f"News {i + 1}: {article['title']}")
                else:
                    speak_old("No news found.")
            else:
                speak_old("Failed to fetch news.")
        except Exception as e:
            print("News error:", e)
            speak_old("News retrieval failed.")

    else:
        output = aiProcess(c)
        # mainoutput = r.recognize_google(output)
        print("AI Response:", output)
        speak_old(output)

# Main loop
if __name__ == "__main__":
    speak_old("Initializing Friday...")

    r = sr.Recognizer() # Speech recognizer
    running = True

    while running:
        try:
            with sr.Microphone() as source:
                print("Listening for wake word...")
                r.adjust_for_ambient_noise(source, duration=1)
                audio = r.listen(source, timeout=4, phrase_time_limit=3)

            try:
                word = r.recognize_google(audio)
                print("Heard:", word)
            except sr.UnknownValueError:
                continue

            if "hello friday" in word.lower():
                speak_old("Yes")
                print(speak_old)
                time.sleep(1.5) # Short pause before listening for commands

                while True:
                    try:
                        with sr.Microphone() as source:
                            print("Listening for command...")
                            r.adjust_for_ambient_noise(source, duration=1)
                            audio = r.listen(source, timeout=6, phrase_time_limit=5)

                        try:
                            command = r.recognize_google(audio) 
                            print("Command recognized:", command)

                            if command.lower() in ["stop", "exit", "sleep"]:
                                speak_old("Okay, going to sleep.")
                                running = False
                                break

                            processCommand(command)

                        except sr.UnknownValueError:
                            speak_old("Sorry, I didn't catch that.")
                        

                    except Exception as e:
                        print("Listening error:", e)
                        break  # break inner loop to restart wake word

        except Exception as e:
            print("Wake word error:", e)