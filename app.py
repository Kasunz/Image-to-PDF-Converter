import tkinter as tk
from tkinter import filedialog
from reportlab.pdfgen import canvas
from PIL import Image
import os


class ImageToPDFConverter:
    def __init__(self, root):
        self.root = root
        self.image_path = []        # List to store paths of selected images
        self.output_pdf_name = tk.StringVar()       # To store the PDF name entered by the user
        self.selected_images_listbox = tk.Listbox(root, selectmode=tk.MULTIPLE)     # Listbox to show selected images

        self.initialize_ui()

    # Set up the GUI components like buttons, labels, and listbox
    def initialize_ui(self):

        # Title label for the window
        title_label = tk.Label(self.root, text="Image To PDF Convertor", font=("Helvetica", 16, "bold"))
        title_label.pack(pady=10)

        # Button to open the file dialog and select images
        select_images_button = tk.Button(self.root, text="Select Images", command=self.select_images)
        select_images_button.pack(pady=(0, 10))

        # Listbox to display the selected image file names
        self.selected_images_listbox.pack(pady=(0, 10), fill=tk.BOTH, expand=True)

        # Label to prompt the user for PDF output name
        label = tk.Label(self.root, text="Enter output PDF name")
        label.pack()

        # Entry box for user to type the PDF name
        pdf_name_entry = tk.Entry(self.root, textvariable=self.output_pdf_name, width=40)
        pdf_name_entry.pack()

        # Button to trigger the conversion process
        convert_button = tk.Button(self.root, text="Convert to PDF", command=self.convert_images_to_pdf)   # convert pdf button
        convert_button.pack(pady=(20, 40))

     # Open a file dialog to select multiple images and store the file paths.
    def select_images(self):
        self.select_paths = filedialog.askopenfilenames(title="Select Images", filetypes=[("Image files", "*.png; *.jpg; *.jpeg")])
        self.update_selected_images_listbox()

    # Convert the selected images into a PDF document.
    def update_selected_images_listbox(self):
        self.selected_images_listbox.delete(0, tk.END)

        # Loop through the selected image paths and extract the file names
        for image_path in self.image_path:
            _, image_path = os.path.split(image_path)
            self.selected_images_listbox.insert(tk.END, image_path)    # Add the file name to the listbox

    def convert_images_to_pdf(self):
        # If no images are selected, do nothing
        if not self.image_path:
            return
        # If the user has entered a PDF name, use it, otherwise use a default name
        output_pdf_path = self.output_pdf_name.get() + ".pdf" if self.output_pdf_name.get() else "Converted_images.pdf"

        pdf = canvas.Canvas(output_pdf_path, pagesize=(612, 792))  # Create a new PDF document (8.5"x11" standard letter size)

        for img_path in self.image_path:  # Open each image
            img = Image.open(img_path)

            # Calculate the scale to fit the image within the page's available space
            available_width = 540
            available_height = 720
            scale_factor = min(available_width / img.width, available_height / img.height)
            new_width = img.width * scale_factor
            new_height = img.height * scale_factor  # * = into

            # Center the image on the page
            x_centered = (612 - new_width) / 2
            y_centered = (792 - new_height) / 2

            # Set a white background (to ensure proper margins)
            pdf.setFillColorRGB(255, 255, 255)
            pdf.rect(0, 0, 612, 792, fill=True)

            pdf.drawInlineImage(img, x_centered, y_centered, width=new_width, height=new_height)
            pdf.showPage()

        pdf.save()                # saving the pdf



def main():
    root = tk.Tk()              # Create the root window
    root.title("Image to PDF")
    converter = ImageToPDFConverter(root)
    root.geometry("400x600")
    root.mainloop()

if __name__ == "__main__":
    main()
