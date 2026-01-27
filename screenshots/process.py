import os
from PIL import Image, ImageDraw, ImageFont

def process_image(filename, output_filename, overlay_text, text_color):
    if not os.path.exists(filename):
        print(f"Error: {filename} not found.")
        return

    try:
        with Image.open(filename) as img:
            img = img.convert("RGBA")
            width, height = img.size

            # --- 1. Create the Black Gradient ---
            gradient_layer = Image.new('RGBA', (width, height), (0, 0, 0, 0))
            draw_gradient = ImageDraw.Draw(gradient_layer)

            # Increased gradient height to 35% to accommodate the higher text position
            gradient_height = int(height * 0.35)
            start_y = height - gradient_height

            for y in range(start_y, height):
                ratio = (y - start_y) / gradient_height
                alpha = int(ratio * 220)
                draw_gradient.line([(0, y), (width, y)], fill=(0, 0, 0, alpha))

            out = Image.alpha_composite(img, gradient_layer)

            # --- 2. Add the Text ---
            draw_text = ImageDraw.Draw(out)

            # Font size: 10% of image height
            font_size = int(height * 0.10) 
            
            font_names = ["ariblk.ttf", "Arial Black.ttf", "Arial_Black.ttf"]
            font = None
            
            for name in font_names:
                try:
                    font = ImageFont.truetype(name, font_size)
                    break
                except IOError:
                    continue
            
            if font is None:
                print("Arial Black font not found. Using default.")
                font = ImageFont.load_default()

            text_bbox = draw_text.textbbox((0, 0), overlay_text, font=font)
            text_width = text_bbox[2] - text_bbox[0]
            text_height = text_bbox[3] - text_bbox[1]

            x_pos = (width - text_width) // 2
            
            # Increased margin: 10% padding from the bottom edge
            y_pos = height - text_height - int(height * 0.10)

            draw_text.text((x_pos, y_pos), overlay_text, font=font, fill=text_color)

            out.save(output_filename)
            print(f"Saved processed image to: {output_filename}")

    except Exception as e:
        print(f"An error occurred processing {filename}: {e}")

# --- Execute ---

process_image(
    filename="locked.png",
    output_filename="locked-text.png",
    overlay_text="Without Ely Unlocker",
    text_color=(255, 0, 0)
)

process_image(
    filename="unlocked.png",
    output_filename="unlocked-text.png",
    overlay_text="With Ely Unlocker",
    text_color=(0, 255, 0)
)