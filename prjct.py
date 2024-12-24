import os
import cv2

# Paths
image_dir = "C:/Users/Khadi/Downloads/PKLot.v1-raw.yolov5-obb/train/images"
label_dir = "C:/Users/Khadi/Downloads/PKLot.v1-raw.yolov5-obb/train/labelTxt"
output_dir = "C:/Users/Khadi/Downloads/PKLot.v1-raw.yolov5-obb/train/visualizations"
os.makedirs(output_dir, exist_ok=True)

# File to log malformed annotations
malformed_log = "malformed_annotations.txt"
with open(malformed_log, "w") as log_file:
    log_file.write("Malformed Annotations Log:\n")

def visualize_annotations(image_path, label_path, output_dir):
    print(f"Processing image: {image_path}")
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error loading image: {image_path}")
        return

    height, width = image.shape[:2]
    print(f"Image dimensions (HxW): {height} x {width}")

    with open(label_path, "r") as f:
        lines = f.readlines()

    for line in lines:
        print(f"Processing annotation: {line.strip()}")
        data = line.strip().split()
        if len(data) < 9:  # Check for minimum required elements
            print(f"Malformed annotation: {line.strip()}")
            with open(malformed_log, "a") as log_file:
                log_file.write(f"Malformed annotation: {line.strip()}\n")
            continue

        try:
            # Extract coordinates and convert to integers
            x1, y1 = int(float(data[0])), int(float(data[1]))
            x2, y2 = int(float(data[2])), int(float(data[3]))
            x3, y3 = int(float(data[4])), int(float(data[5]))
            x4, y4 = int(float(data[6])), int(float(data[7]))
            class_name = data[8]  # Class name is the 9th element
            print(f"Coordinates: ({x1}, {y1}), ({x2}, {y2}), ({x3}, {y3}), ({x4}, {y4}), Class: {class_name}")
        except ValueError:
            print(f"ValueError for annotation: {line.strip()}")
            with open(malformed_log, "a") as log_file:
                log_file.write(f"Malformed annotation: {line.strip()}\n")
            continue

        # Draw bounding box
        points = [(x1, y1), (x2, y2), (x3, y3), (x4, y4)]
        for i in range(4):
            cv2.line(image, points[i], points[(i + 1) % 4], (0, 255, 0), 2)
        cv2.putText(image, class_name, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    
    # Save the image
    output_image_path = os.path.join(output_dir, os.path.basename(image_path))
    print(f"Saving annotated image to: {output_image_path}")
    cv2.imwrite(output_image_path, image)

# Process all images and labels
for label_file in os.listdir(label_dir):
    if label_file.endswith(".txt"):
        image_path = os.path.join(image_dir, label_file.replace(".txt", ".jpg"))
        label_path = os.path.join(label_dir, label_file)

        if os.path.exists(image_path):
            print(f"Found image for label: {label_file}")
            visualize_annotations(image_path, label_path, output_dir)
        else:
            print(f"Image not found for annotation: {label_file}")

print(f"Annotated images saved to: {output_dir}")
print(f"Malformed annotations logged to: {malformed_log}")
