#import ultralytics
from ultralytics import YOLO

#load  custom model model

model = YOLO('best.pt')

#export the model to tflite format

model.export(format='tflite')
