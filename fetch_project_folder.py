import os
from PyQt6.QtWidgets import QFileDialog


from update_status_info import update_status
from data_handler import set_project_path

android_app_path = r"/android/app/src/main/res"
ios_app_path = r"/ios/Runner/Assets.xcassets/AppIcon.appiconset"
main_file_path = r"/lib/main.dart"
pubspec_yaml_file_path = r"/pubspec.yaml"

android_path_exists = False
ios_path_exists = False
main_file_exists = False
pubspec_yaml_exists = False


def validate_project_folder(project_path):
    global android_path_exists, ios_path_exists, main_file_exists, pubspec_yaml_exists

    android_path_exists = True if os.path.exists(
        f"{project_path}{android_app_path}") else False

    ios_path_exists = True if os.path.exists(
        f"{project_path}{ios_app_path}") else False

    main_file_exists = True if os.path.exists(
        f"{project_path}{main_file_path}") else False

    pubspec_yaml_exists = True if os.path.exists(
        f"{project_path}{pubspec_yaml_file_path}") else False

    if android_path_exists and ios_path_exists and main_file_exists and pubspec_yaml_exists:
        return True

    elif not android_path_exists and not ios_path_exists and not main_file_exists and not pubspec_yaml_exists:
        return False

    else:
        return None


def select_project(self):
    global android_path_exists, ios_path_exists, main_file_exists

    selected_project_path = QFileDialog.getExistingDirectory(
        caption="Select Flutter Project")
    if selected_project_path != "":
        self.label_status.setText("Validating project folder...")
        is_project_folder_valid = validate_project_folder(
            selected_project_path)

        if is_project_folder_valid:
            set_project_path(self, selected_project_path)
            update_status(self)
            self.line_edit_project_path.setText(selected_project_path)
            self.line_edit_project_path.setCursorPosition(0)

        elif is_project_folder_valid == None:
            self.label_status.setText(
                "android folder doesn\"t exist or missing contents!") if not android_path_exists else None
            self.label_status.setText(
                "ios folder doesn\"t exist or missing contents!") if not ios_path_exists else None
            self.label_status.setText(
                "main.dart file in lib folder doesn\"t exist!") if not main_file_exists else None
            self.label_status.setText(
                "pubspec.yaml file doesn\"t exist!") if not pubspec_yaml_exists else None
            self.label_status.setStyleSheet("color: orange")

        else:
            set_project_path(self, "")
            update_status(self)
            self.label_status.setText(
                "Select a valid flutter project directory")
            self.label_status.setStyleSheet("color: orange")
