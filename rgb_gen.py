import requests
from PIL import Image
from webcolors import hex_to_rgb

response_data = ''

parameters = {"col": "128", "num": "9984", "min": "0", "max": "16777215", "base": "16", "format": "plain", "rnd": "new"}

# Make the call to get our block of integers
response = requests.get('https://www.random.org/integers/', params = parameters)
response_data += response.text.strip(' \t')

parameters["num"] = "6400"
response = requests.get('https://www.random.org/integers/', params = parameters)
response_data += response.text.strip(' \t')

rows = [hex_row.strip(' \t').split("\t") for hex_row in response_data.split("\n") if hex_row.strip(' \t')]

rows = [list(map(lambda hex_str: hex_to_rgb("#" + hex_str), row)) for row in rows]

# Load the integers into an RGB File

image = Image.new("RGB", (128, 128))
pixels = image.load()

# This could also be done without a matrix nesting just using a counter for rows
for index_x, row in enumerate(rows):
    for index_y, column_value in enumerate(row):
        pixels[index_x, index_y] = column_value


image.save("random.bmp")
