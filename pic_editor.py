from PIL.ImageFile import ImageFile
from PIL.Image import Image


class Editor:

    def paste_pic(self, bg_pic: ImageFile, pics_to_paste: list[ImageFile], new_size_bg: tuple[int, int] = None,
                  new_size_paste: list[tuple[int, int]] = None, boxes: list[tuple[int, int]] | list[tuple[int, int,
                                                                                                          int, int
                                                                                                          ]] = None) \
            -> (
            Image):
        if new_size_bg:
            bg_pic = bg_pic.resize(new_size_bg)
        if new_size_paste:
            if len(new_size_paste) != len(pics_to_paste):
                raise Exception("Размер массива картинок не соответствует размеру массива размеров")
            size: tuple[int, int]
            for i, size in enumerate(new_size_paste):
                pics_to_paste[i] = pics_to_paste[i].resize(size)
        if boxes and len(boxes) != len(pics_to_paste):
            raise Exception("Размер массива картинок не соответствует размеру массива расположения")

        for i, image in enumerate(pics_to_paste):
            bg_pic.paste(image, mask=image, box=boxes[i] if boxes else None)

        return bg_pic
