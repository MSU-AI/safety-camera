# Safety Cam
Safety Cam is a project developed by the Artificial Intelligence Club (AI Club) at Michigan State University (MSU). The goal of this project is to develop a camera capable of detecting dangers using camera visuals and sound detection.

## How it Works
The Safety Cam uses a combination of computer vision and sound detection algorithms to identify potentially dangerous situations.
The camera captures live footage and processes it in real-time using various computer vision techniques such as object detection and tracking.
At the same time, the camera also analyzes the sound in the environment and identifies sounds and speeches that potentially signify dangers.
If the camera detects a dangerous situation, it alerts the user through a mobile app and sends an emergency alert to predefined contacts.
 
## Getting Started
To get started with the Safety Cam, you will need the following:
- A computer with a camera and microphone
- Python 3.10 or later installed
- Git

To set up the Safety Cam, follow the steps below:
1. Clone the Safety Cam repository to your computer using the following command:
```
git clone https://github.com/MSU-AI/safety-camera.git
```
2. Install the required dependencies by running the following command in the Safety Cam directory:
```
pip install -r requirements.txt
```
3. Start the Safety Cam by running:
```
cd app/
streamlit run main.py
```
4. The Safety Cam web app will open in your default web browser.
5. Click on the "Start" button to start the camera stream.
6. The camera will start capturing footage and processing it in real-time.
7. If the Safety Cam detects a potentially dangerous situation, it will display an alert on the screen.
8. To stop the camera stream, click on the "Stop Stream" button.

## Contributing
We welcome contributions to the Safety Cam project. If you would like to contribute, please follow the steps below:
1. Set up a virtual environment named `env`:
```
python -m venv env
```
2. Activate the virtual environment. On Windows, run:
```
env\Scripts\activate
```
On Linux or macOS, run:
```
source env/bin/activate
```
3. Install the required dependencies by running the following command in the Safety Cam directory:
```
pip install -r requirements.txt
```
4. Install `safetycam` as a local editable package:
```
pip install -e .
```

## License
The Safety Cam project is licensed under the MIT License.
See the [LICENSE](LICENSE) file for more information.
