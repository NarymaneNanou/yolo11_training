from ultralytics import YOLO

# Load a COCO-pretrained YOLO11n model
#model = YOLO("runs/detect/train/weight/best.pt")

model = YOLO("best.pt")

# Run inference with the trained model on images in 'test_images' folder, results saved in "runs/detect/predict/" folder


model.predict('test_images', save=True, imgsz=640, conf=0.2)

#direct prediction
#results = model("test.jpg")
#results = model("test.mp4")