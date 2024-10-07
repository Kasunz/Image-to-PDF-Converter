import tkinter as tk
from tkinter import filedialog
from reportlab.pdfgen import canvas
from PIL import Image
import os


class ImageToPDFConverter:
    def __init__(self, root):
        self.root = root
        self.image_path = []
        self.output_pdf_name = tk.StringVar()
        self.selected_images_listbox = tk.Listbox(root, selectmode=tk.MULTIPLE)

        self.initialize_ui()

    def initialize_ui(self):
        title_label = tk.Label(self.root, text="Image To PDF Convertor", font=("Helvetica", 16, "bold"))   # create the title
        title_label.pack(pady=10)

        select_images_button = tk.Button(self.root, text="Select Images", command=self.select_images)
        select_images_button.pack(pady=(0, 10))

        self.selected_images_listbox.pack(pady=(0, 10), fill=tk.BOTH, expand=True) # list box for storing the images (names)

        label = tk.Label(self.root, text="Enter output PDF name")       # label for indicate the user
        label.pack()

        pdf_name_entry = tk.Entry(self.root, textvariable=self.output_pdf_name, width=40) # Entry for users to type pdf names
        pdf_name_entry.pack()

        convert_button = tk.Button(self.root, text="Convert to PDF", command=self.convert_images_to_pdf)   # convert pdf button
        convert_button.pack(pady=(20, 40))


    def select_images(self):
        self.select_paths = filedialog.askopenfilenames(title="Select Images", filetypes=[("Image files", "*.png; *.jpg; *.jpeg")])
        self.update_selected_images_listbox()

    def update_selected_images_listbox(self):
        self.selected_images_listbox.delete(0, tk.END)

        for image_path in self.image_path:
            _, image_path = os.path.split(image_path)
            self.selected_images_listbox.insert(tk.END, image_path)     # Delete the image path and display the image name.

    def convert_images_to_pdf(self):
        if not self.image_path:
            return
        # If the user does not specify an output name, the app will return the output name as Converted_images.
        output_pdf_path = self.output_pdf_name.get() + ".pdf" if self.output_pdf_name.get() else "Converted_images.pdf"

        pdf = canvas.Canvas(output_pdf_path, pagesize=(612, 792))  # Create the pdf with page size

        for img_path in self.image_path: # Taking the images one by one
            img = Image.open(img_path)
            available_width = 540
            available_height = 720
            scale_factor = min(available_width / img.width, available_height / img.height)
            new_width = img.width * scale_factor
            new_height = img.height * scale_factor  # * = into
            x_centered = (612 - new_width) / 2              # place the images into center
            y_centered = (792 - new_height) / 2

            pdf.setFillColorRGB(255, 255, 255)     # margin color
            pdf.rect(0, 0, 612, 792, fill=True)
            pdf.drawInlineImage(img, x_centered, y_centered, width=new_width, height=new_height)
            pdf.showPage()

        pdf.save()                # saving the pdf



def main():
    root = tk.Tk()
    root.title("Image to PDF")
    converter = ImageToPDFConverter(root)
    root.geometry("400x600")
    root.mainloop()

if __name__ == "__main__":
    main()
