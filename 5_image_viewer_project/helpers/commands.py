import os
from .images import HelperImageTk

class ImageHandler:
    def __init__(self, folder_path, image_viewer):
        self.path = folder_path
        self.images = os.listdir(self.path)
        self.viewer = image_viewer
        self.curr_idx = 0
        self.len = len(self.images)
        self.__update_image()

    def __update_image(self):
        image = os.path.join(self.path, self.images[self.curr_idx])
        self.image = HelperImageTk(image)
        self.viewer.config(image=self.image)

    def next(self):
        if self.curr_idx < self.len - 1:
            self.curr_idx += 1
        else:
            self.curr_idx = 0

        self.__update_image()

    def prev(self):
        if self.curr_idx > 0:
            self.curr_idx -= 1
        else:
            self.curr_idx = self.len - 1

        self.__update_image()
