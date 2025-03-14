from ultralytics import YOLO

# Load the  model
model = YOLO("best.pt")

# Export the model to ONNX format
model.export(format="onnx")  # creates 'best.onnx'

# Load the exported ONNX model
onnx_model = YOLO("best.onnx")

# Run inference
results = onnx_model("test.jpg")