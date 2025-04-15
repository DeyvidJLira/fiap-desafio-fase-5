import os
from constants import FINE_TUNED_MODEL
from dotenv import load_dotenv
from train_model import train_model
from video_reader import execute_video, process_video
from ultralytics import YOLO


if __name__ == "__main__":
    load_dotenv()  

    if not os.path.exists(FINE_TUNED_MODEL):
        train_model()
        print("Fine tunning model finalizado, execute o programa novamente para detectar objetos em vídeos.")
    else:
        model = YOLO(FINE_TUNED_MODEL)
        #execute_video(model) # Para executar a detecção em tempo real
        process_video("videos/video_1.mp4", model, True)