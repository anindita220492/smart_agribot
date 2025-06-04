
def detect_disease(image_file):
    if "leaf" in image_file.name.lower():
        return "Powdery Mildew - Use sulfur-based fungicide."
    return "Unable to detect disease. Please upload a clearer image."
