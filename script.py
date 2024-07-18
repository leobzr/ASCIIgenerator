import PIL.Image

ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

# resize image according to new width
def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio * 0.5)
    resized_image = image.resize((new_width, new_height))
    return resized_image


# Convert each pixel to grayscale
def grayscale(image):
    return image.convert("L")


# convert pizels to a string of ascii characters
def pixels_to_ascii(image):
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[pixel // 25] for pixel in pixels])
    return characters


def main(new_width=100):
    # attempt to open an image from user input
    path = input("Enter a valid image path: \n")
    try:
        image = PIL.Image.open(path)
    except:
        print("This is not a valid path, there was an error opening the image.")
        return

    # process the image
    image = resize_image(image, new_width)
    image = grayscale(image)
    ascii_str = pixels_to_ascii(image)

    # format the ascii string into lines
    ascii_str_len = len(ascii_str)
    ascii_img = "\n".join([ascii_str[index:(index + new_width)] for index in range(0, ascii_str_len, new_width)])

    print(ascii_img)

    with open("ascii_image.txt", "w") as f:
        f.write(ascii_img)


if __name__ == '__main__':
    main()