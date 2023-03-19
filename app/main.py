import streamlit as st
from streamlit_webrtc import webrtc_streamer
import speech_recognition as sr
import time

def speech_to_text_microphone():
    # initialize recognizer class (for recognizing the speech)
    r = sr.Recognizer()
    
    # Reading Microphone as source
    # listening the speech and store in audio_text variable
    with sr.Microphone() as source:
        audio_text = r.listen(source)
    # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
    try:
        # using google speech recognition
        return r.recognize_google(audio_text)
    except:
        return ""
    

audio = ""
st.title("SafetyCam")

webrtc_streamer(key="video")
def live_caption():
    text = ""
    # Initialize recognizer and microphone objects
    r = sr.Recognizer()
    mic = sr.Microphone()

    # Set minimum energy threshold to account for ambient noise
    with mic as source:
        r.adjust_for_ambient_noise(source)

    # Continuously listen to microphone input and print live caption
    with mic as source:
        while True:
            try:
                audio = r.listen(source)
                text = r.recognize_google(audio)
                print(text)
                st.write(text)
            except sr.UnknownValueError:
                # Handle unrecognized speech
                pass
if st.button("Start Live Caption"):
    live_caption()
