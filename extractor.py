import pathlib
import google.generativeai as genai
import json
import re
import cv2
import requests
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import display
from config import GEMINI_API_KEY
from translator import convert_tamil_to_sinhala
from visualizer import show_extraction_results

# Configure API
genai.configure(api_key=GEMINI_API_KEY)

def extract_nic_details(image_path):
    """Extract NIC details from an image."""
    try:
        model = genai.GenerativeModel('gemini-1.5-pro')
        with open(image_path, 'rb') as image_file:
            image_bytes = image_file.read()

        prompt = """This is a Sri Lankan National Identity Card..."""
        
        response = model.generate_content(
            [prompt, {"mime_type": "image/jpeg", "data": image_bytes}]
        )
        
        raw_text = response.text
        nic_data = {
            "First Name": convert_tamil_to_sinhala(_extract_field(raw_text, "First Name")),
            "Other Names": convert_tamil_to_sinhala(_extract_field(raw_text, "Other Names")),
            "Date of Birth": _extract_date(raw_text),
            "Birth Place": convert_tamil_to_sinhala(_extract_field(raw_text, "Birth Place")),
            "Occupation": convert_tamil_to_sinhala(_extract_field(raw_text, "Occupation")),
            "Address": convert_tamil_to_sinhala(_extract_field(raw_text, "Address")),
        }

        output_file = f"nic_data_{pathlib.Path(image_path).stem}.json"
        with open(output_file, "w", encoding='utf-8') as json_file:
            json.dump(nic_data, json_file, indent=4, ensure_ascii=False)

        show_extraction_results(image_path, nic_data)
        return nic_data
        
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        return None

def _extract_field(text, field_name):
    """Extracts a specific field from the text."""
    match = re.search(f"{field_name}:\s*([^\n]+)", text)
    return match.group(1).strip() if match else "Not Found"

def _extract_date(text):
    """Extracts and formats date from text."""
    patterns = [r'\b\d{4}[-./]\d{2}[-./]\d{2}\b', r'\b\d{2}[-./]\d{2}[-./]\d{4}\b']
    for pattern in patterns:
        match = re.search(pattern, text)
        if match:
            return match.group()
    return "Not Found"
