import os
import shutil
import random
from constants import LABEL_ALERT_DATASETS_EXISTS, LABEL_SPLIT_SUCCESS
from glob import glob

TRAIN = "train"
TEST= "test"
VAL = "val"
DATASETS = "datasets"
IMAGES = "images" 
LABELS = "labels"

# Função para distribuir as imagens e labels para treino, validação e teste
def split_img_label(images_path, labels_path, train_ratio=0.7, val_ratio=0.2, test_ratio=0.1, seed=42):
    assert round(train_ratio + val_ratio + test_ratio) == 1, "A soma de Ratios deve resultar em 1."

    if os.path.exists(DATASETS):
        print(LABEL_ALERT_DATASETS_EXISTS)
        return

    for split in [TRAIN, VAL, TEST]:
        os.makedirs(os.path.join(DATASETS, IMAGES, split), exist_ok=True)
        os.makedirs(os.path.join(DATASETS, LABELS, split), exist_ok=True)

    # Obtém a lista de path dos arquivos de imagem e faz um embaralhamento
    list_image_files = glob(os.path.join(images_path, '*.jpg')) + glob(os.path.join(images_path, '*.webp')) + glob(os.path.join(images_path, '*.jpeg'))
    random.seed(seed)
    random.shuffle(list_image_files)

    # Obtém o total e indexadores para serem utilizados na distribuição
    total = len(list_image_files)
    train_split = int(total * train_ratio)
    val_split = int(total * (train_ratio + val_ratio))

    # Passa a lista para cada grupo distribuido
    train_files = list_image_files[:train_split]
    val_files = list_image_files[train_split:val_split]
    test_files = list_image_files[val_split:]

    # Função que será reutilizada para move os arquivos para seu destino específico, além disso move txt que tenha o mesmo nome da imagem
    def move_files(file_list, split):
        for img_path in file_list:
            label_path = os.path.join(labels_path, os.path.splitext(os.path.basename(img_path))[0] + ".txt")
            if os.path.exists(label_path):
                shutil.move(img_path, os.path.join(DATASETS, IMAGES, split, os.path.basename(img_path)))
                shutil.move(label_path, os.path.join(DATASETS, LABELS, split, os.path.basename(label_path)))
            else:
                print(f"No label found for {img_path}")

    move_files(train_files, TRAIN)
    move_files(val_files, VAL)
    move_files(test_files, TEST)

    print(LABEL_SPLIT_SUCCESS)
    