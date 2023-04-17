import streamlit as st
from streamlit_webrtc import WebRtcMode, webrtc_streamer
import av
import numpy as np
import cv2
import mediapipe as mp
st.set_page_config(page_title='Surveillance')
st.title("SafetyCam")

mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

with st.sidebar:
    st.write('# Settings')
    echo = st.checkbox('listen to audio')
    num_faces = st.slider('Number of people in the room',0,10,1)
    sound_max = st.slider('Sound Threshold',0,50000,1000)
    faces = num_faces
def audio_frame_callback(frame: av.AudioFrame) -> av.AudioFrame:
    error = "Normal"
    sound = frame.to_ndarray()
    if sound.max() > sound_max:
        if error == "Normal":
            print("Audio Range Exceeded!!")
    else:
        if error == "Audio Range Exceeded!!":
            print("In Range")
            error = "Normal"
    result_sound = sound if echo else np.zeros_like(sound)
    result_frame = av.AudioFrame.from_ndarray(result_sound, layout=frame.layout.name)
    result_frame.sample_rate = frame.sample_rate

    return result_frame

def video_frame_callback(frame: av.VideoFrame) -> av.VideoFrame:
    error_video = "Normal"
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
        
        if faces < num_faces or faces > num_faces:
            if error_video == "Normal":
                print("Number of Faces Not in Range!!")
                error_video = "Number of Faces Not in Range!!"
        else:
            pass
        # Convert the modified ndarray back to av.VideoFrame
        new_video_frame = av.VideoFrame.from_ndarray(img_array, format='bgr24')

    return new_video_frame

streamer = webrtc_streamer(
    key='surveillance',
    mode=WebRtcMode.SENDRECV,
    audio_frame_callback=audio_frame_callback,
    video_frame_callback=video_frame_callback,
)

