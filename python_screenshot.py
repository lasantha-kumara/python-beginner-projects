import pyscreenshot as ImageGrab
import random


def main():
    # generate a random number
    random_image_number = random.randint(1000, 9999)

    # get the screenshot, show it and save it
    image = ImageGrab.grab()
    image.show()
    image.save(f"{random_image_number}.jpg")


main()
