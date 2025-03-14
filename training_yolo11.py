


#import ultralytics
from ultralytics import YOLO

#load  a Coco-pretrained yolo11n model

model = YOLO('yolo11n.pt')

#train the model on specific dataset, results will be saved in "runs" folder

results = model.train(data= 'data.yaml', epochs=100, imgsz=640)

#for Mac M1 chip using GPU
#results = model.train(data= 'data.yaml', epochs=10, imgsz=640, device= 'mps')