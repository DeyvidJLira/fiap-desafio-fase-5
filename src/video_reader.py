import cv2
import os
from constants import CONFIDENCE, ERROR_AT_OPEN_VIDEO, PROCESSING_VIDEO_LABEL, WARNING_LIST
from ultralytics import YOLO
from tqdm import tqdm


def detect_in_frame(model: YOLO, frame):
    results = model(frame, stream=True)

    for result in results:
        for box in result.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            confidence = box.conf[0]
            label = result.names[int(box.cls[0])]
        
            if confidence >= CONFIDENCE:
                if label in WARNING_LIST:
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.putText(frame, f"{label} {confidence:.2f}", (x1, y1 - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                else:
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
                    cv2.putText(frame, f"{label} {confidence:.2f}", (x1, y1 - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)


def execute_video(model: YOLO):
    video_capture = cv2.VideoCapture(0)

    while video_capture.isOpened():
        frame_was_read, frame = video_capture.read()
        if not frame_was_read:
            break
        
        detect_in_frame(model, frame)

        cv2.imshow("Detecção em Tempo Real", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
    video_capture.release()
    cv2.destroyAllWindows()


def process_video(video_path: str, model: YOLO, must_record=False, output_file="processado.mp4"):
    if not os.path.exists(video_path):
        print("O caminho do vídeo deve ser válido!")
        exit()
    
    video_capture = cv2.VideoCapture(video_path)
    if not video_capture.isOpened():
        print(ERROR_AT_OPEN_VIDEO)
        exit()

    if must_record:
        fourcc = cv2.VideoWriter.fourcc(*'mp4v')
        width = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
        global_fps = int(video_capture.get(cv2.CAP_PROP_FPS))
        out = cv2.VideoWriter(output_file, fourcc, global_fps, (width, height))

    global_total_frames = int(video_capture.get(cv2.CAP_PROP_FRAME_COUNT))
    
    for _ in tqdm(range(global_total_frames), desc=PROCESSING_VIDEO_LABEL):
      frame_was_read, frame = video_capture.read()

      if not frame_was_read:
        break
      
      detect_in_frame(model, frame)

      if must_record:
        out.write(frame)

    if must_record:
        out.release()
    
    video_capture.release()
    cv2.destroyAllWindows()



