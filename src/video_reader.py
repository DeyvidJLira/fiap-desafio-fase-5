import cv2
import os
import time
from email_service import send_email
from constants import CONFIDENCE, ERROR_AT_OPEN_VIDEO, MINIMUM_INTERVAL_EMAIL_IN_SECONDS, PROCESSING_VIDEO_LABEL, SECURE_LIST, WARNING_LIST
from ultralytics import YOLO
from tqdm import tqdm

last_email_sent = {}

# Função para detectar objetos em um frame
def detect_in_frame(model: YOLO, frame):
    results = model(frame, stream=True)

    for result in results:
        for box in result.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            confidence = box.conf[0]
            label = result.names[int(box.cls[0])]
            if confidence >= CONFIDENCE:
                print(f"Detectado: {label} com confiança de {confidence:.2f}")  
                if label in WARNING_LIST:
                    handle_warning(label, confidence, frame)
                    draw_rectangle(frame, x1, y1, x2, y2, label, confidence)
                else:
                    print(f"{label} não está na lista de alerta.")


# Função para lidar com alertas
def handle_warning(label, confidence, frame):
    current_time = time.time()
        
    if label in WARNING_LIST:
        if label not in last_email_sent or (current_time - last_email_sent[label]) > MINIMUM_INTERVAL_EMAIL_IN_SECONDS:
            # Converte o frame para JPEG e salva em memória
            _, buffer = cv2.imencode('.jpg', frame)
            image_bytes = buffer.tobytes()

            # Envia o e-mail com o frame como anexo
            send_email(
                "Alerta de Segurança",
                f"Detectado cortante com confiança de {confidence:.2f}",
                attachment_content=image_bytes,
                attachment_name="detected_frame.jpg",
                attachment_type="image/jpeg"
            )
            last_email_sent[label] = current_time
    else:
        print(f"{label} não está na lista de avisos.") 


# Função para desenhar um retângulo indicando o objeto detectado em um frame
def draw_rectangle(frame, x1, y1, x2, y2, label, confidence):
    color = (0, 255, 0) if label in WARNING_LIST else (255, 0, 0)
    cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
    cv2.putText(frame, f"{label} {confidence:.2f}", (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)


# Função para executar a detecção em tempo real
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


# Função para processar um arquivo de vídeo mp4
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



