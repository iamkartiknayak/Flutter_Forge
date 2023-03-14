from PyQt6.QtWidgets import QFileDialog
from PIL import Image

from update_status_info import update_status
from data_handler import set_image_path


supported_image_type = (
    ".jpg",
    ".jpeg",
    ".png",
    ".JPG",
    ".JPEG",
    ".PNG"
)


def validate_image():
    image = Image.open(image_path)
    if image.size[0] > 1024 and image.size[1] > 1024:
        return True

    return False


def select_image(self):
    global new_image_selected, image_path
    content = QFileDialog.getOpenFileName(
        directory="./", filter="Image File, *.jpg *.jpeg *.jfif *.png", caption="Select App Image")

    image_path = content[0]
    if image_path != "":
        if validate_image():
            set_image_path(self, image_path)
            update_status(self)
        else:
            set_image_path(self, "")
            update_status(self)
            self.label_status.setText("Image size must be atleast 1024 x 1024")
            self.label_status.setStyleSheet("color: orange")
