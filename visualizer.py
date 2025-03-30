import cv2
import numpy as np
import matplotlib.pyplot as plt

def show_extraction_results(image_path, nic_data):
    """Displays the NIC image with highlighted text for extracted fields."""
    image = cv2.imread(image_path)
    highlighted = image.copy()

    colors = {
        "First Name": (255, 255, 0), "Other Names": (0, 255, 255),
        "Date of Birth": (255, 200, 200), "Birth Place": (200, 255, 200),
        "Occupation": (200, 200, 255), "Address": (255, 200, 255)
    }

    for field, value in nic_data.items():
        if value and value != "Not Found":
            x, y, w, h = 50, 50, 200, 50  # Example fixed position for demo
            cv2.rectangle(highlighted, (x, y), (x + w, y + h), colors[field], 2)
            cv2.putText(highlighted, f"{field}: {value}", (x, y - 5), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, colors[field], 1)

    plt.figure(figsize=(10, 8))
    plt.imshow(cv2.cvtColor(highlighted, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.title('NIC Text Extraction Results')
    plt.show()
