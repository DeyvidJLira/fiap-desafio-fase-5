BASE_MODEL = "yolo11n.pt"
FINE_TUNED_MODEL = "best.pt"
DATASET_CONFIG_FILE = "dataset.yaml"

CONFIDENCE = 0.35

ERROR_AT_OPEN_VIDEO = "Falhou em abrir o arquivo de vídeo."

LABEL_ALERT_DATASETS_EXISTS = "Alerta: a pasta datasets já existe, exclua ela primeiro para evitar falhas, este processo será ignorado por enquanto!"
LABEL_SPLIT_SUCCESS = "Distribuição concluída com sucesso!"

LABEL_START_TRAIN = "Iniciando treinamento..."
LABEL_SAVE_MODEL = "Salvando o modelo..."
LABEL_FINE_TUNED_MODEL_SAVED = f"Modelo fine tuned salvo como {FINE_TUNED_MODEL}"

MINIMUM_INTERVAL_EMAIL_IN_SECONDS = 300  # 5 minutos

PROCESSING_VIDEO_LABEL = "Processando video..."

WARNING_LIST = ["Knife"]
SECURE_LIST = ["Hand"]