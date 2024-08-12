import os
from rembg import remove
import cv2
import numpy as np
from PIL import Image
from pic_editor import Editor

output_path = "test/output.png"
editor = Editor()


def main():
    pic = Image.open("test/output.png")
    #print(type(pic))
    output = remove(pic)
    output.save(output_path)
    new_pic = editor.paste_pic(Image.open("test/bg.png"), [pic], (700, 700), [(500, 500)])
    new_pic.save("test/test.png")


if __name__ == "__main__":
    main()
