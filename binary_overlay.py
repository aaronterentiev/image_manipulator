from PIL import Image, ImageDraw, ImageFont
import random
import os
import sys


def binary_overlay(path_name, new_background_color=(0, 0, 0, 255), font_size=10, font_file_name="Inconsolata-Regular.ttf"):

    input_image = Image.open(path_name)
    input_image = input_image.convert("RGBA")

    # Info from the input image
    input_pixels = list(input_image.getdata())
    input_mode = input_image.mode
    width, height = input_image.size

    # Info for the font and text
    chars_per_row = (width // font_size) * 2
    row_count = (height // font_size) + 1

    # Create an image of random 0s and 1s
    binary_mask = Image.new("RGBA", (width, height))
    b_m = ImageDraw.Draw(binary_mask)

    font = ImageFont.truetype(font_file_name, font_size)
    for row in range(row_count):
        string = str(random.randint(0, 1))
        for x in range(chars_per_row):
            my_new_pal = random.randint(0, 1)
            string += str(my_new_pal)
        b_m.text((0, row*font_size), string, fill=(0, 0, 0), font=font)

    # # Save the image of 0s & 1s for Debugging
    # binary_mask.save('binary_text.png')

    # Get the values of the pixels from the "binary mask"
    binary_mask_pixels = list(binary_mask.getdata())

    # Make the new textified image
    binary_img = Image.new(input_mode, (width, height))
    b_i_pixels = list(binary_img.getdata())
    num_pixels = width * height

    # print(b_i_pixels)
    for pixel_num in range(num_pixels):
        # Draws background color from input
        # To make it transparent, make fourth int of new_background_color = 0
        if binary_mask_pixels[pixel_num][3] is not 0:
            b_i_pixels[pixel_num] = input_pixels[pixel_num]
            # print(input_pixels[pixel_num])
        else:
            b_i_pixels[pixel_num] = new_background_color
    # print(b_i_pixels)

    binary_img = Image.new(input_mode, (width, height))
    binary_img.putdata(b_i_pixels)

    file_name = os.path.basename(path_name)
    name_and_ext = os.path.splitext(file_name)

    binary_img.save("binary_" + name_and_ext[0] + ".png")


def test_binary_overlay():
    path_name = "George_Boole_color.jpg"

    binary_overlay(path_name, new_background_color=(127, 0, 200, 127), font_size=15)

if __name__ == "__main__":
    test_binary_overlay()
    # binary_overlay(sys.argv[1])
