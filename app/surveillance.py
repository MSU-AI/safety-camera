import av
import streamlit as st
import numpy as np
import cv2
import mediapipe as mp
mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils



def audio_frame_callback(frame: av.AudioFrame) -> av.AudioFrame:
    sound = frame.to_ndarray()
    # print(sound.max(),flush=True)
    result_sound = sound if st.session_state['echo'] else np.zeros_like(sound)
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
        # Convert the modified ndarray back to av.VideoFrame
        new_video_frame = av.VideoFrame.from_ndarray(img_array, format='bgr24')

    return new_video_frame


