import openai

openai.api_key = 'Your_API_KEY'
def generate_ai_image(prompt):
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="1024x1024"
    )
    image_url = response['data'][0]['url']
    response = requests.get(image_url)
    img = Image.open(BytesIO(response.content))
    return img

from PIL import Image, ImageEnhance

def apply_luminous_effect(image_path):
    img = Image.open(image_path)
    enhancer = ImageEnhance.Brightness(img)
    img_enhanced = enhancer.enhance(1.5)  # Increase brightness
    img_enhanced.show()  # Display image for now
    return img_enhanced

import tkinter as tk
from PIL import Image, ImageTk, ImageEnhance, ImageDraw
import requests
from io import BytesIO

# Function to simulate AI image generation
def generate_ai_image(prompt):
    # Placeholder: Fetch a random image from an online source
    image_url = "https://picsum.photos/1024/1024"  # Random image placeholder
    response = requests.get(image_url)
    img = Image.open(BytesIO(response.content))
    return img

# Function to generate VIBGYOR gradient
def create_vibgyor_gradient(size):
    width, height = size
    gradient = Image.new('RGB', (width, height), color=0)
    draw = ImageDraw.Draw(gradient)
    
    vibgyor_colors = [
        (148, 0, 211),  # Violet
        (75, 0, 130),   # Indigo
        (0, 0, 255),    # Blue
        (0, 255, 0),    # Green
        (255, 255, 0),  # Yellow
        (255, 165, 0),  # Orange
        (255, 0, 0)     # Red
    ]
    
    stripe_height = height // len(vibgyor_colors)
    
    for i, color in enumerate(vibgyor_colors):
        y0 = i * stripe_height
        y1 = y0 + stripe_height
        draw.rectangle([0, y0, width, y1], fill=color)
    
    return gradient

# Function to apply VIBGYOR overlay
def apply_vibgyor_overlay(image):
    gradient = create_vibgyor_gradient(image.size)
    return Image.blend(image, gradient, alpha=0.4)  # 40% gradient overlay

# Function to apply luminous effect
def apply_luminous_effect(image):
    enhancer = ImageEnhance.Brightness(image)
    img_enhanced = enhancer.enhance(1.5)  # Increase brightness
    return img_enhanced

# Function to generate and display wallpaper
def generate_wallpaper():
    prompt = prompt_entry.get()
    
    # Generate image automatically based on prompt
    generated_image = generate_ai_image(prompt)
    
    # Apply luminous effect
    luminous_image = apply_luminous_effect(generated_image)
    
    # Apply VIBGYOR gradient overlay
    final_image = apply_vibgyor_overlay(luminous_image)
    
    # Display the final image
    display_image(final_image)

# Function to display the image in the Tkinter window
def display_image(img):
    img_tk = ImageTk.PhotoImage(img)
    canvas.create_image(0, 0, anchor=tk.NW, image=img_tk)
    canvas.image = img_tk  # Keep reference to avoid garbage collection

# Tkinter GUI setup
root = tk.Tk()
root.title("AI Wallpaper Generator with VIBGYOR Effect")

# User input for prompt
prompt_label = tk.Label(root, text="Enter wallpaper prompt:")
prompt_label.pack()

prompt_entry = tk.Entry(root, width=50)
prompt_entry.pack()

# Generate wallpaper button
generate_button = tk.Button(root, text="Generate Wallpaper", command=generate_wallpaper)
generate_button.pack()

# Canvas to display the image
canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()

root.mainloop()
