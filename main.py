import cv2
from fastapi import FastAPI, Response
from fastapi.responses import StreamingResponse
app = FastAPI()

username = "username" # Username of the camera
password = "password" # Password of the camera
ip_address = "192.168.1.64:554" # IP address of the camera with port number (default is 554)
camera_url = "rtsp://" + username + ":" + password + "@" + ip_address + "/Streaming/Channels/1/"

resolution = (1024, 768)
fps = 10

def stream_video():
    cap = cv2.VideoCapture(camera_url, cv2.CAP_FFMPEG)
    if not cap.isOpened():
        raise Exception("Failed to connect to camera")
    cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        

        frame = cv2.resize(frame, resolution)
        _, img_encoded = cv2.imencode('.jpg', frame)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + img_encoded.tobytes() + b'\r\n')

@app.get("/")
async def read_root():
    return {"Hello": "World"}
    

@app.get("/video_feed")
async def video_feed():
    return StreamingResponse(stream_video(), media_type="multipart/x-mixed-replace; boundary=frame", headers={"FPS": str(fps)})
