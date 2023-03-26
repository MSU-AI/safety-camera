#!/usr/bin/env python3
import av
import streamlit as st
from streamlit_webrtc import WebRtcMode, webrtc_streamer
import numpy as np

st.set_page_config(page_title='Surveillance')

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

    mirrored = image[:,::-1,:] if display_settings['mirror'] else image

    # image logic

    return av.VideoFrame.from_ndarray(mirrored, format='bgr24')

streamer = webrtc_streamer(
    key='surveillance',
    mode=WebRtcMode.SENDRECV,
    audio_frame_callback=audio_frame_callback,
    video_frame_callback=video_frame_callback,
    async_processing=True,
)