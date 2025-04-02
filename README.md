NIC Text Extraction System for Sri Lanka 🇱🇰

A Python-based system for extracting text from Sri Lankan National Identity Cards (NICs) using Google Gemini AI, OpenCV, and OCR techniques. The system also supports Tamil-to-Sinhala translation to enhance accuracy.

🌟 Features

Extracts text from NIC images using OCR.

Enhances text accuracy with Google Gemini AI.

Preprocesses images using OpenCV for better OCR results.

Supports Tamil-to-Sinhala translation for improved understanding.

Provides structured output for easy integration with other applications.

🚀 Technologies Used

Python - Core programming language.

OpenCV - Image processing library.

Tesseract OCR - Optical character recognition for text extraction.

Google Gemini AI - AI-powered enhancement of extracted text.

Google Translate API - Tamil-to-Sinhala translation.

🔧 Setup Instructions

Clone the repository:

git clone https://github.com/ashentharushikez/nic-text-extraction.git
cd nic-text-extraction

Install dependencies:

pip install opencv-python pytesseract google-cloud-translate google-generativeai

Configure API keys for Google services.

Run the NIC text extraction script:

python extract_nic_text.py --image path/to/nic_image.jpg

📌 Future Improvements

Optimize OCR preprocessing for various NIC conditions.

Improve AI model fine-tuning for better text accuracy.

Develop a web-based or mobile application interface.

Support Sinhala-to-Tamil translation.

📜 License

This project is open-source and available under the MIT License.

👤 Author

H.G. Ashen Tharushika

