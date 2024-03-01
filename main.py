from tkinter import *
from tkinter.filedialog import asksaveasfile, askopenfilename
from PIL import Image, ImageTk, ImageOps

WIDTH = 800
HEIGHT = 800

STAMP = "./stamp_white.png"

def init_ui():
    window = Tk()
    window.config(padx=10, pady=10)
    window.title("Watermarker")
    
    save_button = Button(text="Save image", command=save_img)
    save_button.grid(row=1, column=1)
    
    load_button = Button(text="Open image", command=open_img)
    load_button.grid(row=1, column=0)
    
    window.mainloop()

def save_img():
    filepath = asksaveasfile(mode='w', defaultextension=".jpg", filetypes=[("JPG", "*.jpg")])
    try:
        if filepath:
            merged_image.save(filepath)
    except NameError:
        print("No image to save")
        
def open_img():
    filepath = askopenfilename(filetypes=[("Image files", "*.jpg; *.png")])
    if filepath:
        stamp = Image.open(STAMP).resize((179,214))
        global merged_image
        merged_image = Image.open(filepath).copy()
        merged_image.paste(stamp,(70,70), stamp)
            
        resized_img = ImageOps.contain(merged_image, (WIDTH,HEIGHT))
        img = ImageTk.PhotoImage(resized_img)
        canvas = Canvas(width=WIDTH, height=HEIGHT)
        
        canvas.image = img
        canvas.create_image(WIDTH/2,HEIGHT/2, image=img, anchor="center")
        canvas.grid(row=0, column=0, columnspan=2)

if __name__ == "__main__":
    init_ui()
    
    