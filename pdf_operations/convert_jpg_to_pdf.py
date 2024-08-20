from PIL import Image
import os

# Define the directory paths for input and output folders
input_folder = './input'
output_folder = './output'

# Ensure output folder exists
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Loop through each file in the input directory
for filename in os.listdir(input_folder):
    if filename.endswith('.jpg'):
        # Create the full file path for input and output
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename.replace('.jpg', '.pdf'))

        # Open the image file
        image = Image.open(input_path)

        # Convert the image to PDF and save it
        image.convert('RGB').save(output_path, 'PDF')

        # Optionally, close the image file if desired
        image.close()

print("Conversion completed.")