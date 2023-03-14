import os
from time import sleep
from PIL import Image
from threading import Thread

from data_handler import get_image_path, get_project_path


def start_execution(platform_thread):
    platform_thread.start()
    platform_thread.join()


def update_icons(self):
    t1 = Thread(target=update_android_app_icons, args=(self,))
    start_execution(t1)

    t2 = Thread(target=update_ios_app_icons, args=(self,))
    start_execution(t2)

    icon_applied_platforms = ["android", "ios"]

    project_path = get_project_path()

    if os.path.exists(f"{project_path}/web"):
        t3 = Thread(target=update_web_app_icons, args=(self,))
        start_execution(t3)
        icon_applied_platforms.append("web")

    if os.path.exists(f"{project_path}/windows"):
        t4 = Thread(target=update_windows_app_icon, args=(self,))
        start_execution(t4)
        icon_applied_platforms.append("windows")

    if os.path.exists(f"{project_path}/macos"):
        t5 = Thread(target=update_mac_os_app_icons, args=(self,))
        start_execution(t5)
        icon_applied_platforms.append("macos")

    platform_count = len(icon_applied_platforms)
    if platform_count == 2:
        self.label_status.setText(
            f"Icons applied to {icon_applied_platforms[0]} and {icon_applied_platforms[1]} apps")

    elif platform_count <= 3:
        self.label_status.setText(
            f"Icons applied to {icon_applied_platforms[0]}, {icon_applied_platforms[1]} and {icon_applied_platforms[2]} apps")

    else:
        self.label_status.setText("Icons applied to different platform apps")


def update_android_app_icons(self):
    # Not updating label...
    self.label_status.setText("Applying icons to android app...")
    android_app_icon_main_path = f"/android/app/src/main/res/"
    android_app_icons_subpath_size = {
        "mipmap-hdpi/": (72, 72),
        "mipmap-mdpi/": (48, 48),
        "mipmap-xhdpi/": (96, 96),
        "mipmap-xxhdpi/": (144, 144),
        "mipmap-xxxhdpi/": (192, 192),
    }

    icon_name = "ic_launcher"
    image_path = get_image_path()
    project_path = get_project_path()

    for sub_path, size in android_app_icons_subpath_size.items():
        image = Image.open(image_path)
        image = image.resize(size)
        image.save(
            f"{project_path}{android_app_icon_main_path}{sub_path}{icon_name}.png")
        image.close()
        sleep(0.1)


def update_ios_app_icons(self):
    # Not updating label...
    self.label_status.setText("Applying icons to ios app...")
    ios_app_icon_main_path = f"/ios/Runner/Assets.xcassets/AppIcon.appiconset/"
    ios_app_icons_name_size = {
        "20x20@1x": (20, 20),
        "20x20@2x": (40, 40),
        "20x20@3x": (60, 60),
        "29x29@1x": (29, 29),
        "29x29@2x": (58, 58),
        "29x29@3x": (87, 87),
        "40x40@1x": (40, 40),
        "40x40@2x": (80, 80),
        "40x40@3x": (120, 120),
        "60x60@2x": (120, 120),
        "60x60@3x": (180, 180),
        "76x76@1x": (76, 76),
        "76x76@2x": (152, 152),
        "83.5x83.5@2x": (167, 167),
        "1024x1024@1x": (1024, 1024),
    }

    project_path = get_project_path()
    image_path = get_image_path()
    for icon_name, size in ios_app_icons_name_size.items():
        image = Image.open(image_path)
        image = image.resize(size)
        image.save(
            f"{project_path}{ios_app_icon_main_path}Icon-App-{icon_name}.png")
        image.close()
        sleep(0.1)


def update_web_app_icons(self):
    # Not updating label...
    self.label_status.setText("Applying icons to web app...")
    web_app_icon_main_path = "/web/"
    icon_name = "favicon"

    project_path = get_project_path()
    image_path = get_image_path()

    image = Image.open(image_path)
    image = image.resize((16, 16))
    image.save(f"{project_path}{web_app_icon_main_path}{icon_name}.png")
    image.close()

    web_app_icons_name_size = {
        "Icon-192": (192, 192),
        "Icon-512": (512, 512),
        "Icon-maskable-192": (192, 192),
        "Icon-maskable-512": (512, 512)
    }

    web_app_icon_sub_path = "/web/icons/"
    for icon_name, size in web_app_icons_name_size.items():
        image = Image.open(image_path)
        image = image.resize(size)
        image.save(f"{project_path}{web_app_icon_sub_path}{icon_name}.png")
        image.close()


def update_windows_app_icon(self):
    # Not updating label...
    self.label_status.setText("Applying icons to windows app...")
    windows_app_icon_main_path = "/windows/runner/resources/"

    project_path = get_project_path()
    image_path = get_image_path()
    icon_name = "app_icon"

    image = Image.open(image_path)
    image = image.resize((48, 48))
    image.save(
        f"{project_path}{windows_app_icon_main_path}{icon_name}.ico")
    image.close()


def update_mac_os_app_icons(self):
    # Not updating label...
    self.label_status.setText("Applying icons to macos app...")
    mac_os_app_icon_main_path = "/macos/Runner/Assets.xcassets/AppIcon.appiconset/"
    mac_os_app_icons_name_size = {
        "app_icon_16": (16, 16),
        "app_icon_32": (32, 32),
        "app_icon_64": (64, 64),
        "app_icon_128": (128, 128),
        "app_icon_256": (256, 256),
        "app_icon_512": (512, 512),
        "app_icon_1024": (1024, 1024)
    }

    project_path = get_project_path()
    image_path = get_image_path()

    for icon_name, size in mac_os_app_icons_name_size.items():
        image = Image.open(image_path)
        image = image.resize(size)
        image.save(f"{project_path}{mac_os_app_icon_main_path}{icon_name}.png")
        image.close()
