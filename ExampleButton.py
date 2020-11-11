# -*- coding:utf-8 -*-
__author__ = "liaokong"
__time__ = "2018/11/16 10:02"

from PySide2.QtWidgets import *

from Utils import load_style, button_style

button_style_list = ['MediumGray', 'DarkGray', 'BlueJeans', 'Aqua',
                     'Mint', 'Grass', 'Sunflower', 'Bittersweet', 'Grapefruit', 'Lavender', 'PinkRose']


class ExampleButtonWid(QDialog):
    def __init__(self, parent=None):
        super(ExampleButtonWid, self).__init__(parent)

        load_style(self)

        v_layout = QVBoxLayout(self)

        for style in button_style_list:
            btn = QPushButton(style)
            btn.setMinimumWidth(185)
            btn.setMinimumHeight(30)

            # button style
            button_style(btn, style)

            v_layout.addWidget(btn)


if __name__ == '__main__':
    app = QApplication([])

    eb = ExampleButtonWid()
    eb.show()

    app.exec_()
