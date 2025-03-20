from constants import BASE_MODEL, FINE_TUNED_MODEL, DATASET_CONFIG_FILE, LABEL_START_TRAIN, LABEL_SAVE_MODEL, LABEL_FINE_TUNED_MODEL_SAVED
from ultralytics import YOLO

# Função de treinamento
def train_model():
    model = YOLO(BASE_MODEL)

    print(LABEL_START_TRAIN)
    model.train(data=DATASET_CONFIG_FILE, epochs=150, imgsz=640)

    print(LABEL_SAVE_MODEL)
    model.save(FINE_TUNED_MODEL)

    print(LABEL_FINE_TUNED_MODEL_SAVED)


