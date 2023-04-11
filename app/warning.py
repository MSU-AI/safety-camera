import streamlit as st

class Alerts():
    
    def __init__(self, max_faces, min_faces, threshold_decibals):
        self.max_faces = max_faces
        self.min_faces = min_faces
        self.threshold_decibals = threshold_decibals
    
    def by_audiolevel_threshold(self, current_audio_decibals):
        if self.threshold_decibals<=current_audio_decibals:
            st.markdown(
                """
                <style>
                    @keyframes blink {
                        0% {opacity: 1;}
                        50% {opacity: 0;}
                        100% {opacity: 1;}
                    }
                    .blink {
                        animation: blink 1.5s linear infinite;
                    }
                    .button {
                        display: inline-block;
                        padding: 0.75em 1.5em;
                        text-decoration: none;
                        background: #ffffff;
                        color: #333333;
                        border-radius: 4px;
                        border: solid 2px #333333;
                        transition: .4s;
                    }
                    .button:hover {
                        background: #ff0000;
                        color: #ffffff;
                        font-weight: bold;
                    }
                </style>
                <div class="blink" style="background-color: red; padding: 10px; border-radius: 5px;">
                    <h2 style="color: white; text-align: center;">Warning!</h2>
                </div>
                <br>
                <div style="padding: 10px; border-radius: 5px; margin-top: 10px;">
                    <h4 style="text-align: center;">
                        ⚠️ Audio level is higher than the threshold audio level ⚠️
                    </h4>
                </div>
                """,
                unsafe_allow_html=True
            )
            st.write('---')
            st.markdown(
                """
                <div style="text-align:center;">
                    <a class="button" href="https://police.msu.edu/contact/report-a-crime/" target="_blank">CONTACT 911</a>
                </div>
                """,
                unsafe_allow_html=True
            )
                        
    def by_audio_keywords(self, words):
        pass
    
    def by_number_of_faces(self, faces_seen):
        if faces_seen>=self.max_faces:
            st.markdown(
                """
                <style>
                    @keyframes blink {
                        0% {opacity: 1;}
                        50% {opacity: 0;}
                        100% {opacity: 1;}
                    }
                    .blink {
                        animation: blink 1.5s linear infinite;
                    }
                    .button {
                        display: inline-block;
                        padding: 0.75em 1.5em;
                        text-decoration: none;
                        background: #ffffff;
                        color: #333333;
                        border-radius: 4px;
                        border: solid 2px #333333;
                        transition: .4s;
                    }
                    .button:hover {
                        background: #ff0000;
                        color: #ffffff;
                        font-weight: bold;
                    }
                </style>
                <div class="blink" style="background-color: red; padding: 10px; border-radius: 5px;">
                    <h2 style="color: white; text-align: center;">Warning!</h2>
                </div>
                <div style="padding: 10px; border-radius: 5px; margin-top: 10px;">
                    <h4 style="text-align: center;">
                        ⚠️ Number of faces seen greater than the threshold value ⚠️
                    </h4>
                </div>
                """,
                unsafe_allow_html=True
            )
            st.write('---')
            st.markdown(
                """
                <div style="text-align:center;">
                    <a class="button" href="https://police.msu.edu/contact/report-a-crime/" target="_blank">CONTACT 911</a>
                </div>
                """,
                unsafe_allow_html=True
            )
        elif faces_seen<=self.min_faces:
            st.markdown(
                """
                <style>
                    @keyframes blink {
                        0% {opacity: 1;}
                        50% {opacity: 0;}
                        100% {opacity: 1;}
                    }
                    .blink {
                        animation: blink 1.5s linear infinite;
                    }
                    .button {
                        display: inline-block;
                        padding: 0.75em 1.5em;
                        text-decoration: none;
                        background: #ffffff;
                        color: #333333;
                        border-radius: 4px;
                        border: solid 2px #333333;
                        transition: .4s;
                    }
                    .button:hover {
                        background: #ff0000;
                        color: #ffffff;
                        font-weight: bold;
                    }
                </style>
                <div class="blink" style="background-color: red; padding: 10px; border-radius: 5px;">
                    <h2 style="color: white; text-align: center;">Warning!</h2>
                </div>
                <div style="padding: 10px; border-radius: 5px; margin-top: 10px;">
                    <h4 style="text-align: center;">
                        ⚠️ Number of faces seen lower than the threshold value ⚠️
                    </h4>
                </div>
                """,
                unsafe_allow_html=True
            )
            st.write('---')
            st.markdown(
                """
                <div style="text-align:center;">
                    <a class="button" href="https://police.msu.edu/contact/report-a-crime/" target="_blank">CONTACT 911</a>
                </div>
                """,
                unsafe_allow_html=True
            )

a=Alerts(1,1,1)
a.by_number_of_faces(-1)