from PyQt6 import QtWidgets, QtGui


def show_dialog(self, message):
    msg_box = QtWidgets.QMessageBox()
    msg_box.setWindowTitle("AppIGen")
    msg_box.setWindowIcon(QtGui.QIcon("./Logo/logo.ico"))
    msg_box.setText(message)
    msg_box.setIcon(QtWidgets.QMessageBox.Icon.Question)
    msg_box.setStandardButtons(
        QtWidgets.QMessageBox.StandardButton.Ok
        | QtWidgets.QMessageBox.StandardButton.Cancel
    )

    ax = self.geometry().x() + 180
    ay = self.geometry().y() + 180
    msg_box.setGeometry(ax, ay, 399, 603)

    response = msg_box.exec()
    return response
