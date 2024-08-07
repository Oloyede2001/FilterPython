import os

# Define the paths to your annotation directories
annotation_dirs =[
    '/Users/jesutomisinoloyede/Downloads/TrainingSet/Annotations/labelTxt',
    '/Users/jesutomisinoloyede/Downloads/TrainingSet/Annotations/trainset_reclabelTxt',
    '/Users/jesutomisinoloyede/Downloads/ValidationSet/Annotations/labelTxt-v1.0/labelTxt',
    '/Users/jesutomisinoloyede/Downloads/ValidationSet/Annotations/labelTxt-v1.0/valset_reclabelTxt'
]

# Iterate through each directory
for annotations_path in annotation_dirs:
    # Check if the path exists
    if not os.path.exists(annotations_path):
        print(f"The directory {annotations_path} does not exist.")
    else:
        # Iterate through all files in the annotations directory
        for filename in os.listdir(annotations_path):
            if filename.endswith('.txt'):
                file_path = os.path.join(annotations_path, filename)
                with open(file_path, 'r') as file:
                    content = file.read()
                    # Check if the file contains "plane" or "ship"
                    if "plane" not in content and "ship" not in content:
                        os.remove(file_path)
                        print(f"Deleted {filename} from {annotations_path}")

print("Processing complete.")
