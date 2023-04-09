import streamlit as st
from streamlit_webrtc import WebRtcMode, webrtc_streamer
import surveillance as sv

st.set_page_config(page_title='Surveillance')
st.title("SafetyCam")
if 'mirror' not in st.session_state:
    st.session_state['mirror'] = 1

if 'echo' not in st.session_state:
    st.session_state['echo'] = 1

with st.sidebar:
    st.write('# Settings')
    st.session_state['mirror']: st.checkbox('mirror')
    st.session_state['echo']: st.checkbox('echo')

streamer = webrtc_streamer(
    key='surveillance',
    mode=WebRtcMode.SENDRECV,
    audio_frame_callback=sv.audio_frame_callback,
    video_frame_callback=sv.video_frame_callback,
    async_processing=True,
)