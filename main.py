from extractor import extract_nic_details

if __name__ == "__main__":
    image_path = "D:/Computer science/KD enterprises/first jupyter project/pic/back2.jpg"
    results = extract_nic_details(image_path)

    if results:
        print("\n🔹 Extracted NIC Details:")
        for key, value in results.items():
            print(f"{key}: {value}")
