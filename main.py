from PIL import Image
import glob

r_left_border = 255
r_right_border = 255
g_left_border = 255
g_right_border = 255
b_left_border = 255
b_right_border = 255

r_fill = 255
g_fill = 255
b_fill = 255


def restore_images(directory_path):
    types = (".jpg", ",jpeg")
    for type in types:
        for filename in glob.glob(directory_path + r"\*" + type):
            image = Image.open(filename)
            restore_image(image)
            image.save(filename)


def restore_image(image: Image):
    for i in range(image.size[0]):
        for j in range(image.size[1]):
            r = image.getpixel((i, j))[0]
            g = image.getpixel((i, j))[1]
            b = image.getpixel((i, j))[2]
            if r_left_border <= r <= r_right_border and g_left_border <= g <= g_right_border \
                    and b_left_border <= b <= b_right_border:  # От 170 до 223 для всех
                image.putpixel((i, j), (r_fill, g_fill, b_fill))  # r, g и b равны 255


if __name__ == '__main__':
    r_left_border = int(input("Enter bottom value for Red (0-255): "))
    r_right_border = int(input("Enter top value for Red (0-255): "))
    g_left_border = int(input("Enter bottom value for Green (0-255): "))
    g_right_border = int(input("Enter top value for Green (0-255): "))
    b_left_border = int(input("Enter bottom value for Blue (0-255): "))
    b_right_border = int(input("Enter top value for Blue (0-255): "))
    r_fill = int(input("\nEnter Red value to paint the watermark (0-255): "))
    g_fill = int(input("Enter Green value to paint the watermark (0-255): "))
    b_fill = int(input("Enter Blue value to paint the watermark (0-255): "))
    print("\nAll images placed in the folder will be changed. Save a copy"
          " of them before starting recovery! Are you sure you want to change the images?\n(y/n)")
    confirmation = input()
    if confirmation == "y":
        directory_path = '.\images_for_restore'
        restore_images(directory_path)
        print("\nRestore successful")
