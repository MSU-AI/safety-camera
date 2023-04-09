import av
import streamlit as st
from streamlit_webrtc import WebRtcMode, webrtc_streamer
import numpy as np
import cv2

st.set_page_config(page_title='Surveillance')
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
profile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_profileface.xml')
with st.sidebar:
    st.write('# Settings')
    display_settings = {
        'mirror': st.checkbox('mirror'),
        'echo': st.checkbox('echo'),
    }

def audio_frame_callback(frame: av.AudioFrame) -> av.AudioFrame:
    sound = frame.to_ndarray()

    # sound logic

    result_sound = sound if display_settings['echo'] else np.zeros_like(sound)
    result_frame = av.AudioFrame.from_ndarray(result_sound, layout=frame.layout.name)
    result_frame.sample_rate = frame.sample_rate
    return result_frame

def video_frame_callback(frame: av.VideoFrame) -> av.VideoFrame:
    image = frame.to_ndarray(format='bgr24')

    to_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(to_gray,1.3,5)
    num_faces = 0
    profiles = profile_cascade.detectMultiScale(to_gray,1.3,5)
    mirrored_image = image[:,::-1,:]
    mirrored_to_gray = cv2.cvtColor(mirrored_image, cv2.COLOR_BGR2GRAY)
    profiles_mirrored = profile_cascade.detectMultiScale(mirrored_to_gray,1.3,5)
    for (x,y,w,h) in profiles_mirrored:
        cv2.rectangle(image, (x,y), (x+w,y+h), (0,255,0), 2)
    num_faces+=len(profiles_mirrored)
    for (x,y,w,h) in profiles:
        cv2.rectangle(image, (x,y), (x+w,y+h), (0,255,0), 2)
    num_faces+=len(profiles)

    for (x,y,w,h) in faces:
        cv2.rectangle(image, (x,y), (x+w,y+h), (255,0,0), 2)
    mirrored = image[:,::-1,:] if display_settings['mirror'] else image
    num_faces+=len(faces)
    print(num_faces)

    return av.VideoFrame.from_ndarray(mirrored, format='bgr24')

streamer = webrtc_streamer(
    key='surveillance',
    mode=WebRtcMode.SENDRECV,
    audio_frame_callback=audio_frame_callback,
    video_frame_callback=video_frame_callback,
    async_processing=True,
)