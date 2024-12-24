import os
import cv2

def convert_to_yolo_format(line, img_width, img_height):
    data = line.strip().split()
    x1, y1 = int(float(data[0])), int(float(data[1]))
    x2, y2 = int(float(data[2])), int(float(data[3]))
    x3, y3 = int(float(data[4])), int(float(data[5]))
    x4, y4 = int(float(data[6])), int(float(data[7]))
    class_name = data[8]

    class_id = 0 if class_name == 'space-empty' else 1

    # Calculate center, width, and height of the bounding box
    x_center = (x1 + x2 + x3 + x4) / 4.0
    y_center = (y1 + y2 + y3 + y4) / 4.0
    width = max(x1, x2, x3, x4) - min(x1, x2, x3, x4)
    height = max(y1, y2, y3, y4) - min(y1, y2, y3, y4)

    # Normalize the values by dividing by the image dimensions
    x_center /= img_width
    y_center /= img_height
    width /= img_width
    height /= img_height

    print(f"Converted annotation: {class_id} {x_center} {y_center} {width} {height}")
    return f"{class_id} {x_center} {y_center} {width} {height}"

def process_annotations(label_dir, output_dir, img_dir):
    os.makedirs(output_dir, exist_ok=True)
    for label_file in os.listdir(label_dir):
        if label_file.endswith(".txt"):
            with open(os.path.join(label_dir, label_file), "r") as f:
                lines = f.readlines()
            img_path = os.path.join(img_dir, label_file.replace(".txt", ".jpg"))
            img = cv2.imread(img_path)
            if img is None:
                print(f"Image not found: {img_path}")
                continue
            img_height, img_width = img.shape[:2]
            print(f"Processing file: {label_file}")
            with open(os.path.join(output_dir, label_file), "w") as out_f:
                for line in lines:
                    yolo_annotation = convert_to_yolo_format(line, img_width, img_height)
                    out_f.write(yolo_annotation + "\n")
            print(f"Finished processing {label_file}")

# Example usage:
img_dir = "C:/Users/Khadi/Downloads/PKLot.v1-raw.yolov5-obb/train/images"
label_dir = "C:/Users/Khadi/Downloads/PKLot.v1-raw.yolov5-obb/train/labelTxt"
output_dir = "C:/Users/Khadi/Downloads/PKLot.v1-raw.yolov5-obb/train/yoloformat"
process_annotations(label_dir, output_dir, img_dir)
