import numpy as np
data_type = [("name", "S15"), ("Class", int), ("Height", float)]
student_details = [("James", 5, 48.5), ("Nail", 6, 52.5), ("Paul", 5, 42.10), ("Pit", 5, 40.11)]

student = np.array(student_details, dtype=data_type)
print("Original array:")
print(student)
print("Sort by height")
print(np.sort(student, order="Height"))