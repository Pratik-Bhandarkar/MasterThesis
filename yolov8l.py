from ultralytics import YOLO
if __name__ == '__main__':
    # Load a model
    model = YOLO("yolov8l.pt")  # load a pretrained model

    # Use the model
    results = model.train(data='/content/drive/My Drive/Colab Notebooks/data.yaml',
                          imgsz=640,
                          epochs=20,
                          batch=4,
                          name='yolov8n_custom')  # train the model
    results = model.val()
