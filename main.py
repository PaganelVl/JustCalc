import sys
import math
from PySide6.QtWidgets import QApplication, QMainWindow
from design import Ui_MainWindow


class Calculator(QMainWindow):
    def add_digit_and_func(self):
        btn = self.sender()
        digit_and_func = ('btn_0', 'btn_1', 'btn_2', 'btn_3', 'btn_4',
                          'btn_5', 'btn_6', 'btn_7', 'btn_8', 'btn_9',
                          'btn_plus', 'btn_min', 'btn_max', 'btn_div',
                          'btn_point', 'btn_equal', 'btn_exp', 'btn_l_bracket', 'btn_r_bracket')
        special_func = ('btn_abs', 'btn_negative', 'btn_radical', 'btn_pi')

        if btn.objectName() in special_func:
            if btn.objectName() == 'btn_abs':
                self.ui.lineEdit.setText(f'abs({self.ui.lineEdit.text()})')
            elif btn.objectName() == 'btn_negative':
                if self.ui.lineEdit.text() == '0':
                    self.ui.lineEdit.setText('-')
                else:
                    self.ui.lineEdit.setText(self.ui.lineEdit.text() + '-')
            elif btn.objectName() == 'btn_radical':
                self.ui.lineEdit.setText(f'math.sqrt({self.ui.lineEdit.text()})')
            elif btn.objectName() == 'btn_pi':
                if self.ui.lineEdit.text() == '0':
                    self.ui.lineEdit.setText(f'{math.pi}')
                else:
                    self.ui.lineEdit.setText(self.ui.lineEdit.text() + f'{math.pi}')
        elif btn.objectName() in digit_and_func:
            if self.ui.lineEdit.text() == '0':
                self.ui.lineEdit.setText(btn.text())
            else:
                self.ui.lineEdit.setText(self.ui.lineEdit.text() + btn.text())

    def calc(self):
        if '^' in self.ui.lineEdit.text():
            self.ui.lineEdit.setText(self.ui.lineEdit.text().replace('^', '**'))
        res = eval(self.ui.lineEdit.text())
        if '**' in self.ui.lineEdit.text():
            self.ui.lineEdit.setText(self.ui.lineEdit.text().replace('**', '^'))
        self.ui.label.setText(f'{res}')

    def __init__(self):
        super(Calculator, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # digits and functions
        self.ui.btn_0.clicked.connect(self.add_digit_and_func)
        self.ui.btn_1.clicked.connect(self.add_digit_and_func)
        self.ui.btn_2.clicked.connect(self.add_digit_and_func)
        self.ui.btn_3.clicked.connect(self.add_digit_and_func)
        self.ui.btn_4.clicked.connect(self.add_digit_and_func)
        self.ui.btn_5.clicked.connect(self.add_digit_and_func)
        self.ui.btn_6.clicked.connect(self.add_digit_and_func)
        self.ui.btn_7.clicked.connect(self.add_digit_and_func)
        self.ui.btn_8.clicked.connect(self.add_digit_and_func)
        self.ui.btn_9.clicked.connect(self.add_digit_and_func)
        self.ui.btn_plus.clicked.connect(self.add_digit_and_func)
        self.ui.btn_min.clicked.connect(self.add_digit_and_func)
        self.ui.btn_max.clicked.connect(self.add_digit_and_func)
        self.ui.btn_div.clicked.connect(self.add_digit_and_func)
        self.ui.btn_point.clicked.connect(self.add_digit_and_func)
        self.ui.btn_exp.clicked.connect(self.add_digit_and_func)
        self.ui.btn_abs.clicked.connect(self.add_digit_and_func)
        self.ui.btn_negative.clicked.connect(self.add_digit_and_func)
        self.ui.btn_radical.clicked.connect(self.add_digit_and_func)
        self.ui.btn_pi.clicked.connect(self.add_digit_and_func)
        self.ui.btn_l_bracket.clicked.connect(self.add_digit_and_func)
        self.ui.btn_r_bracket.clicked.connect(self.add_digit_and_func)
        self.ui.btn_equal.clicked.connect(self.calc)
        self.ui.btn_equal.clicked.connect(self.add_digit_and_func)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Calculator()
    window.show()

    sys.exit(app.exec())
