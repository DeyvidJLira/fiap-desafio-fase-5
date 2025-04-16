BASE_MODEL = "yolo11n.pt" # Modelo base
FINE_TUNED_MODEL = "best.pt" # Modelo treinado
DATASET_CONFIG_FILE = "dataset.yaml" # Arquivo de configuração do dataset
DISABLE_EMAIL_SERVICE = False    # Para desativar o serviço de e-mail, defina como True

CONFIDENCE = 0.5 # Limite de confiança para detecção de objetos

ERROR_AT_OPEN_VIDEO = "Falhou em abrir o arquivo de vídeo."

LABEL_ALERT_DATASETS_EXISTS = "Alerta: a pasta datasets já existe, exclua ela primeiro para evitar falhas, este processo será ignorado por enquanto!"
LABEL_SPLIT_SUCCESS = "Distribuição concluída com sucesso!"

LABEL_START_TRAIN = "Iniciando treinamento..."
LABEL_SAVE_MODEL = "Salvando o modelo..."
LABEL_FINE_TUNED_MODEL_SAVED = f"Modelo fine tuned salvo como {FINE_TUNED_MODEL}"

MINIMUM_INTERVAL_EMAIL_IN_SECONDS = 300  # 5 minutos

PROCESSING_VIDEO_LABEL = "Processando video..."

WARNING_LIST = ["knife"]
SECURE_LIST = ["ball", "hand", "ruler"]