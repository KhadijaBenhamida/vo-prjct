# Parking Spot Detection using YOLO

## Overview
This project utilizes the YOLO (You Only Look Once) object detection model to detect parking spots in images and video footage. The model has been tested on both static images and real-time video streams to evaluate its performance in different scenarios.

## Features
- **Real-time Parking Spot Detection**: Uses YOLO to detect available and occupied parking spots.
- **Supports Images & Videos**: The model can process both static images and video streams.
- **Customizable Model**: Fine-tuned YOLO model for improved accuracy in detecting parking spots.
- **Efficient & Fast**: YOLO provides high-speed inference, making it suitable for real-time applications.

## Installation
### Prerequisites
Ensure you have the following dependencies installed before running the project:
- Python 3.x
- OpenCV
- PyTorch
- NumPy
- Matplotlib
- `ultralytics` (for YOLOv8)

To install dependencies, run:
```bash
pip install opencv-python numpy torch matplotlib ultralytics
```

## Usage
### Resuming Training from a Checkpoint
```bash
python train.py --resume "/content/drive/MyDrive/yolo_training/exp/weights/last.pt"
```

### Validating the Model
```bash
python val.py --data /content/drive/MyDrive/PKLot.v1-raw.yolov5-obb/data.yaml --weights /content/drive/MyDrive/yolo_training/exp/weights/best.pt --img 640
```

### Training YOLOv5 with Checkpoint Saving
```bash
python train.py \
--img 640 \
--batch 16 \
--epochs 50 \
--data "/content/drive/MyDrive/PKLot.v1-raw.yolov5-obb/data.yaml" \
--weights yolov5s.pt \
--project "/content/drive/MyDrive/yolo_training" \
--save-period 1
```

### Running the Model on Images
```bash
python detect.py --weights /content/drive/MyDrive/yolo_training/exp/weights/best.pt --source /content/drive/MyDrive/PKLot.v1-raw.yolov5-obb/test/images --conf 0.25 --save-txt --save-conf
```

### Running the Model on Videos
```bash
python detect.py --weights /content/drive/MyDrive/yolo_training/exp/weights/best.pt --source /content/drive/MyDrive/istockphoto-1248173933-640_adpp_is.mp4 --conf 0.25 --save-txt --save-conf
```

## Results
- The model has been tested on both **images and videos**.
- Achieved high accuracy in detecting available and occupied parking spots.
- Can be further fine-tuned by using more training data specific to different parking environments.

## Future Improvements
- Improve accuracy using a larger dataset with diverse parking conditions.
- Implement a web-based interface for real-time monitoring.
- Deploy the model on edge devices like Raspberry Pi for on-site parking management.



## Contributors
- **BENHAMIDA Khadija** - **BOUJJOU Tasnime** - Project Developers

For any inquiries or collaborations, feel free to reach out!

