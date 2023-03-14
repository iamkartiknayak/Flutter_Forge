from PyQt6 import QtWidgets, uic
from sys import argv

from fetch_image import select_image
from fetch_project_folder import select_project
from dialog_box import show_dialog
from update_icon import update_icons
from data_handler import reset_data


class AppIGen(QtWidgets.QMainWindow):
    def __init__(self):
        super(AppIGen, self).__init__()
        uic.loadUi("ui.ui", self)

        self.btn_select_image.clicked.connect(self.select_source_image)
        self.btn_select_project.clicked.connect(self.select_project_folder)
        self.btn_reset.clicked.connect(self.reset_fields)
        self.btn_apply_changes.clicked.connect(self.apply_app_icons)
        self.show()

    def select_source_image(self):
        select_image(self)

    def select_project_folder(self):
        select_project(self)

    def apply_app_icons(self):
        update_icons(self)

    def reset_fields(self):
        reset_selected_data = show_dialog(self, "Reset Selection?")
        if reset_selected_data == 1024:
            reset_data(self)


app = QtWidgets.QApplication(argv)
window = AppIGen()
app.exec()
