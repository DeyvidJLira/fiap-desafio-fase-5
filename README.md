# Desafio Fase 5 FIAP

Projeto destinado ao desafio da fase 5 do curso de pós graduação "AI para devs" na FIAP.

## Quer ver no Google Colab? (Uso mais fácil)

[![Ver no Colab](https://colab.research.google.com/drive/153mcmwWoSCypodpIetesmG2X0Iyg0Qv0?usp=sharing)

## 💻 Pré-requisitos

Antes de começar, verifique se você atendeu ao seguintes requisitos:

- Python na versão 3.11.
- Colocou os 2 arquivos de vídeos na pasta de vídeo, o nome deles devem ser respectivamente video_1.mp4 e video_2.mp4, mas você pode alterar no arquivo `main.py`.

## 🚀 Configurando

- Instale as dependências do projeto
```
pip install -r requirements.txt
```

## 🤝 Integrantes do projeto

- [Abimael Silva](https://github.com/abimael-boby)
- [Anne Izaura](https://github.com/anneizaura)
- [Deyvid Jaguaribe](https://github.com/DeyvidJLira)
- [Lucas Cervantes](https://github.com/Cervas23)
- [Thiago Bussiki](https://github.com/ThiagoBussiki)

## Como está organizado

O código fonte do projeto, na pasta src, é composto por 5 arquivos, sendo eles:

- constants.py -> Como o próprio nome diz, é onde estar todas as constantes do projeto;
- email_service.py -> Contém a função de enviar email com texto e anexo, no projeto é utilizado para enviar alerta de que detectou um objeto cortante e o print do frame é enviado;
- main.py -> Arquivo principal para execução do projeto;
- train_model.py -> Contém a função de treinamento;
- util.py -> Destinado a funções utilitárias, nesse projeto contém a função de distribuir as imagens e labels em train, val e test (opcional);
- video_reader.py -> Contém as funções de detecta o objeto usando o módulo e processar vídeos (vindo da câmera ou arquivo).

Além disso temos o arquivo `dataset.yaml` que será utilizada pelo modelo. 

A pasta `dataset_to_split` é destinada colocar as pastas de images e labels para que a função de split faça a distribuição, gerando assim a pasta `datasets`.

Para este projeto usamos como base o modelo yolo11s.

O código encontrar-se comentado na partes mais importantes para facilitar o entendimento.

## Informação adicional

Para facilitar a execução, o modelo que passou por fine tunning já estar disponível nesse repositório com o nome best.pt 

## Como treinar um novo modelo

Caso queira treinar um novo modelo, deverá seguir os passos:

- apagar o arquivo best.pt;
- crie a pasta `dataset_to_split` na raiz do projeto e adicione as pastas images e labels com seus respectivos arquivos. Para facilitar utilize [Label Studio](https://labelstud.io/);
- utilize uma das funções disponíveis em util.py para distribuir em train, val e test;
- execute main.py;
- pronto agora você verá um novo best.pt disponível na raiz do projeto.

Saiba mais em: [Documentação](https://github.com/DeyvidJLira/fiap-desafio-fase-5/wiki/Documenta%C3%A7%C3%A3o)
