from data_handler import get_image_status, get_project_status


def update_status(self):

    if get_image_status() and get_project_status():
        self.btn_apply_changes.setDisabled(False)
        self.label_status.setText("Ready to apply new icon...")
        self.label_status.setStyleSheet("color: green")

    elif get_image_status() and not get_project_status():
        self.btn_apply_changes.setDisabled(True)
        self.line_edit_project_path.clear()
        self.label_status.setText("Waiting for project directory...")
        self.label_status.setStyleSheet("color: black")

    elif get_project_status() and not get_image_status():
        self.btn_apply_changes.setDisabled(True)
        self.line_edit_image_path.clear()
        self.label_status.setText("Waiting for app image...")
        self.label_status.setStyleSheet("color: black")
