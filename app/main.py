import streamlit as st
from streamlit_webrtc import WebRtcMode, webrtc_streamer
import av
import numpy as np
import cv2
import mediapipe as mp
import warning as wn

st.set_page_config(page_title='Surveillance')
st.title("SafetyCam")

mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

with st.sidebar:
    st.write('# Settings')
    # mirror = st.checkbox('mirror')
    echo = st.checkbox('listen to audio')
    num_faces = st.slider('Number of people in the room',0,10,(0,10))
    sound_max = st.slider('Sound Threshold',0,50000,1000)
    min_faces = num_faces[0]
    max_faces = num_faces[1]
warn = wn.Alerts(max_faces,min_faces,sound_max)

def audio_frame_callback(frame: av.AudioFrame) -> av.AudioFrame:
    sound = frame.to_ndarray()
    warn.by_audiolevel_threshold(sound.max())
    result_sound = sound if echo else np.zeros_like(sound)
    result_frame = av.AudioFrame.from_ndarray(result_sound, layout=frame.layout.name)
    result_frame.sample_rate = frame.sample_rate

    return result_frame

def video_frame_callback(frame: av.VideoFrame) -> av.VideoFrame:
     # Initialize face detection
    with mp_face_detection.FaceDetection(min_detection_confidence=0.8) as face_detection:

        # Convert av.VideoFrame to ndarray
        img_array = np.array(frame.to_ndarray(format='bgr24'))

        # Convert the image to RGB, as MediaPipe uses RGB
        img_rgb = cv2.cvtColor(img_array, cv2.COLOR_BGR2RGB)

        # Create a mutable MediaPipe image object
        img_rgb.flags.writeable = True

        # Perform face detection
        results = face_detection.process(img_rgb)

        # Draw face landmarks on the image
        img_rgb.flags.writeable = False
        img_array = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2BGR)
        if results.detections:
            for detection in results.detections:
                mp_drawing.draw_detection(img_array, detection)
            faces = len(results.detections)
        else:
            faces = 0
        warn.by_number_of_faces(faces)
        # Convert the modified ndarray back to av.VideoFrame
        new_video_frame = av.VideoFrame.from_ndarray(img_array, format='bgr24')

    return new_video_frame


streamer = webrtc_streamer(
    key='surveillance',
    mode=WebRtcMode.SENDRECV,
    audio_frame_callback=audio_frame_callback,
    video_frame_callback=video_frame_callback,
    async_processing=True,
)