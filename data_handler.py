from update_image_info import add_info

image_path = ""
project_path = ""
image_selected = False
project_selected = False


def reset_data(self):
    global image_path, project_path, image_selected, project_selected
    image_path = ""
    project_path = ""
    image_selected = False
    project_selected = False

    self.btn_apply_changes.setDisabled(True)
    self.line_edit_image_path.clear()
    self.line_edit_project_path.clear()
    self.label_image_display.clear()
    self.label_img_info.clear()
    self.label_status.setText("Waiting for app image...")
    self.label_status.setStyleSheet("color: black")


def get_image_path():
    return image_path


def get_image_status():
    return image_selected


def get_project_path():
    return project_path


def get_project_status():
    return project_selected


def set_image_path(self, new_image_path):
    global image_path, image_selected

    image_path = new_image_path
    if image_path == "":
        image_selected = False
        self.line_edit_image_path.clear()
        self.label_img_info.clear()
        self.label_image_display.clear()
    else:
        image_selected = True
        add_info(self, image_path)


def set_project_path(self, new_project_path):
    global project_path, project_selected

    project_path = new_project_path
    if project_path == "":
        project_selected = False
        self.line_edit_project_path.clear()
    else:
        project_selected = True
        self.line_edit_project_path.setText(new_project_path)
