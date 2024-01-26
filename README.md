# Pix2SVGConverter

Pix2SVGConverter is a simple yet powerful tool designed to convert pixel-based images (PNG) into Scalable Vector Graphics (SVG) format.

## Features

- **Pixel-to-Vector Conversion**: Converts pixels from source images into SVG rectangles, ensuring a high-fidelity vector representation.
- **Optimized for Simplicity**: Best suited for images like pixel art or icons, where simplicity and clear lines are key.
- **Transparency Handling**: Fully transparent pixels are skipped, making the SVG output more efficient and true to the original image.
- **Automatic Output Management**: Automatically creates the output directory if it doesn't exist, streamlining the conversion process.

## Prerequisites

Before you start using Pix2SVGConverter, ensure you have Python installed on your system along with the PIL library, which is used for image processing. You can install PIL (Pillow) using pip:

```bash
pip install Pillow
```

## Installation

Clone this repository to your local machine to get started with Pix2SVGConverter:

```bash
git clone https://github.com/anjieyang/Pix2SVGConverter.git
```

## Usage

Navigate to the cloned repository, and run the script from the command line by specifying the source directory containing your images and the desired output directory for the SVG files:

```bash
python pix2svgconverter.py <source_folder> <output_folder>
```

The script will process each compatible image in the source directory and save the resulting SVG files in the specified output directory. If the output directory does not exist, it will be created automatically.

## Contributing

Contributions are welcome! If you have improvements or bug fixes, please open a pull request. For major changes, please open an issue first to discuss what you would like to change.

## License

MIT License - Feel free to use, modify, and distribute this tool as you see fit.