# Live-Streaming-Using-FastAPI

This code sets up a FastAPI web server that streams video from an RTSP camera. It uses OpenCV to capture frames from the camera, resize them, and encode them as JPEG images. The images are then streamed to the client using the multipart/x-mixed-replace content type, which allows for seamless streaming of multiple images.

The video stream is accessed via the ```"/video_feed"``` endpoint, which returns a StreamingResponse object that streams the frames to the client.

 

## Requirements

- Python 3.6+
- OpenCV
- FastAPI (with Uvicorn)
 

> **NOTE:** To run this code, you need to have OpenCV and FastAPI installed. You also need to update the "camera_url" variable to the URL of your RTSP camera.





## Installation

1. Clone the repository using ```git clone https://github.com/neerajparkashsharma/Live-Streaming-Using-FastAPI```

2. Create a virtual environment using ```python3 -m venv venv``` and activate it using ```source venv/bin/activate```

3. Install the requirements using ```pip install -r requirements.txt```

4. Run the app using ```uvicorn main:app --reload```


## Usage

1. Run the app

2. Open the browser and go to http://localhost:8000

3. navigate to the /video_feed route
