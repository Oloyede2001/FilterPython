import os

# Define the paths for source directories and the destination directory
source_dirs = [
    "/Users/jesutomisinoloyede/Downloads/TrainingSet/Annotations/DOTA-v1.5_train_hbb",
    "/Users/jesutomisinoloyede/Downloads/TrainingSet/Annotations/DOTA-v1.5_train",
    "/Users/jesutomisinoloyede/Downloads/ValidationSet/Annotations/DOTA-v1.5_val",
    "/Users/jesutomisinoloyede/Downloads/ValidationSet/Annotations/DOTA-v1.5_val_hbb"
]

destination_dir = "/Users/jesutomisinoloyede/Downloads/ProcessedAnnotations"

# Ensure the destination directory exists
os.makedirs(destination_dir, exist_ok=True)

def process_line(line):
    parts = line.strip().split()

    # Check if the line has at least 5 parts (four coordinates and a label)
    if len(parts) < 5:
        return None  # Skip lines that don't have enough values

    # The label is assumed to be the last item in the parts list
    label = parts[-1]
    if label not in ['0', '1']:  # Assuming '0' is for planes and '1' is for ships
        return None

    # Extract coordinates and convert to float
    x1, y1, x2, y2 = map(float, parts[:4])

    # Convert to YOLO format
    x_center = (x1 + x2) / 2
    y_center = (y1 + y2) / 2
    width = x2 - x1
    height = y2 - y1

    # Build the YOLO format string
    yolo_format = f"{label} {x_center} {y_center} {width} {height}"
    return yolo_format

# Process files in each source directory
for source_dir in source_dirs:
    for filename in os.listdir(source_dir):
        file_path = os.path.join(source_dir, filename)
        print(f"Processing file: {filename}")

        with open(file_path, 'r') as file:
            lines = file.readlines()

        new_lines = []
        for line in lines:
            processed_line = process_line(line)
            if processed_line:
                new_lines.append(processed_line)

        # Write processed lines to a new file if there are any
        if new_lines:
            new_file_path = os.path.join(destination_dir, filename)
            with open(new_file_path, 'w') as new_file:
                new_file.write("\n".join(new_lines))
            print(f"Written {len(new_lines)} lines to {new_file_path}")
        else:
            print(f"No valid data found in file: {filename}")
