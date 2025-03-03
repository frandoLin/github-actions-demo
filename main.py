def add_numbers(a, b):
    return a + b

def get_medical_info(condition):
    medical_database = {
        "liver": "The liver is responsible for hundreds of functions including protein synthesis and detoxification.",
        "heart": "The heart pumps blood throughout the body via the circulatory system.",
        "diabetes": "Diabetes is a metabolic disease causing elevated blood sugar levels."
    }
    return medical_database.get(condition.lower(), "Information not found.")

if __name__ == "__main__":
    print(get_medical_info("liver"))