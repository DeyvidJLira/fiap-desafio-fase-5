import os

from constants import FINE_TUNED_MODEL
from train_model import train_model
from video_reader import execute_video, process_video
from util import split_img_label
from ultralytics import YOLO


if __name__ == "__main__":
    split_img_label("dataset_to_split/images", 'dataset_to_split/labels')

    if not os.path.exists(FINE_TUNED_MODEL):
        train_model()
        print("Fine tunning model finished, execute program again")
    else:
        model = YOLO(FINE_TUNED_MODEL)
        
        #execute_video(model)
        process_video("videos/video_1.mp4", model, True)