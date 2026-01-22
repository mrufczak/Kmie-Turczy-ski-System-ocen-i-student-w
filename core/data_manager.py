import json
import os

students_file = "students.json"

def load_students(file_name):
    if not os.path.exists(file_name):
        return []

    try:
        with open(file_name, "r") as f:
            return json.load(f)
    
    except json.JSONDecodeError:
        return []
    

def save_students(students_list):
    with open(students_file, "w") as f:
        json.dump(students_list, f, indent = 4)

