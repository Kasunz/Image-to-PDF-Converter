# Image to PDF Converter

This is a Python-based graphical user interface (GUI) application that allows users to select multiple image files and convert them into a single PDF document. The application is built using the **Tkinter** library for the GUI, **Pillow (PIL)** for handling image operations, and **ReportLab** for generating PDF files.

## Features
- Select multiple images from your computer.
- View the selected images in a list before converting.
- Specify a custom name for the output PDF.
- Automatically scales and centers images in the PDF document.
- Supports common image formats like `.png`, `.jpg`, and `.jpeg`.

## Prerequisites
Ensure you have the following installed before running the program:

1. **Python 3.x**: You can download it from [here](https://www.python.org/downloads/).
2. **Tkinter**: Usually comes pre-installed with Python, but if not, you can install it by following the official [Tkinter documentation](https://docs.python.org/3/library/tkinter.html).
3. **Pillow (PIL)**: For handling image operations. Install it via pip:
   ```bash
   pip install pillow
   ```
4. **ReportLab**: For generating PDF files. Install it via pip:
   ```bash
   pip install reportlab
   ```

## Installation
1. Clone this repository or download the source code:
   ```bash
    https://github.com/Kasun-Madusanka-Bandara/imgToPDF.git
   ```

2. Navigate to the project directory:
   ```bash
   cd image-to-pdf-converter
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Run the Python script to launch the Image-to-PDF converter:
   ```bash
   python main.py
   ```

2. In the application window:
   - Click **Select Images** to choose multiple image files.
   - The selected images will be displayed in a list.
   - Enter a name for the output PDF file in the provided text box.
   - Click **Convert to PDF** to generate the PDF file.

3. The converted PDF will be saved in the same directory as the script or in a location specified by the user.

## How It Works
- **Tkinter** is used to create the graphical interface.
- **Pillow** is used to open and manipulate the selected images.
- **ReportLab** is used to create the PDF file, scale the images to fit the page, and center them.
- Images are automatically scaled to fit within a standard 8.5" x 11" page size (612x792 points).

## Code Overview
- `ImageToPDFConverter`: Main class that handles the entire image selection and PDF conversion process.
  - **Methods**:
    - `initialize_ui()`: Sets up the UI elements.
    - `select_images()`: Allows users to select images using a file dialog.
    - `update_selected_images_listbox()`: Updates the listbox with selected image names.
    - `convert_images_to_pdf()`: Converts selected images to a PDF.

## Screenshots
![image](https://github.com/user-attachments/assets/6f28d641-7867-4157-bbd3-3b75f7bd1537)
![image](https://github.com/user-attachments/assets/1a274cbe-f940-495c-a223-bebcd444acaa)


## License

This project is for educational purposes and does not come with any specific license.

