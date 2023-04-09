import streamlit as st

class Warnings():
    
    def __init__(self, max_faces=2, min_faces=0, threshold_decibals=1000):
        self.max_faces = max_faces
        self.min_faces = min_faces
        self.threshold_decibals = threshold_decibals
    
    def by_audiolevel_threshold(self, current_audio_decibals):
        if self.threshold_decibals<current_audio_decibals:
            st.write("Warning, audio threshold exceeded.")
            
    def by_audio_keywords(self, words):
        pass
    
    def by_number_of_faces(self, faces_seen):
        if faces_seen>self.max_faces:
            st.write("Warning, number of faces greater than threshold value")
        elif faces_seen<self.min_faces:
            st.write("Warning, number of faces seen lesser than threshold value")