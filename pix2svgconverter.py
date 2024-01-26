import sys
import os
from PIL import Image

def convert_pixel_to_svg_rect(x, y, width, height, color):
    """
    Generates an SVG rectangle element.

    Args:
    - x: The x-coordinate of the rectangle's starting point.
    - y: The y-coordinate of the rectangle's starting point.
    - width: The width of the rectangle.
    - height: The height of the rectangle.
    - color: The fill color of the rectangle.

    Returns:
    - A string representing the SVG rectangle element.
    """
    return f'<rect x="{x}" y="{y}" width="{width}" height="{height}" fill="{color}"/>\n'

def process_image(image_path, output_dir):
    """
    Processes an individual image, converting it to SVG format.

    Args:
    - image_path: The path to the input image.
    - output_dir: The directory where the output SVG should be saved.
    """
    try:
        image = Image.open(image_path).convert('RGBA')  # Open and convert the image to RGBA format
    except IOError:
        print(f"Error opening {image_path}. Please ensure the file exists and is an image.")
        return

    pixels = image.load()
    width, height = image.size

    svg_elements = []
    for y in range(height):
        x_start = 0
        current_color = None
        for x in range(width):
            r, g, b, a = pixels[x, y]
            # Skip fully transparent pixels
            if a == 0:
                continue
            color = f'#{r:02x}{g:02x}{b:02x}'
            if current_color == color:
                continue
            if current_color is not None:
                svg_elements.append(convert_pixel_to_svg_rect(x_start, y, x - x_start, 1, current_color))
            x_start = x
            current_color = color
        # Handle the last sequence in a row
        if current_color is not None:
            svg_elements.append(convert_pixel_to_svg_rect(x_start, y, width - x_start, 1, current_color))
    
    # Construct the SVG content
    svg_content = f'<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}">\n'
    svg_content += ''.join(svg_elements)
    svg_content += '</svg>'
    
    # Construct the output file path
    output_path = os.path.join(output_dir, os.path.basename(image_path))
    output_path = os.path.splitext(output_path)[0] + '.svg'

    try:
        os.makedirs(output_dir, exist_ok=True)  # Create the output directory if it doesn't exist
        with open(output_path, 'w') as f:
            f.write(svg_content)  # Write the SVG content to the output file
        print(f"SVG created successfully: {output_path}")
    except IOError:
        print(f"Error writing to {output_path}.")

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python script.py <source_folder> <output_folder>")
    else:
        source_folder, output_folder = sys.argv[1], sys.argv[2]

        # Check if the source folder exists
        if not os.path.isdir(source_folder):
            print(f"Source folder '{source_folder}' does not exist.")
            sys.exit(1)

        # Process each image in the source folder
        for filename in os.listdir(source_folder):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                process_image(os.path.join(source_folder, filename), output_folder)
