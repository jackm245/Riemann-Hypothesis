import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QHBoxLayout, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import matplotlib


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Set Matplotlib Chart Value with QLineEdit Widget')
        self.window_width, self.window_height = 1200, 800
        self.setMinimumSize(self.window_width, self.window_height)

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.input = QLineEdit()
        self.input.textChanged.connect(self.update_chart)
        layout.addWidget(self.input)

        self.canvas = FigureCanvas(plt.Figure(figsize=(15, 6)))
        layout.addWidget(self.canvas)

        self.insert_ax()

    def insert_ax(self):
        font = {
            'weight': 'normal',
            'size': 16
        }
        matplotlib.rc('font', **font)

        self.ax = self.canvas.figure.subplots()
        self.ax.set_ylim([0, 100])
        self.ax.set_xlim([0, 1])
        self.bar = None

    def update_chart(self):
        value = self.input.text()
        try:
            value = float(value)
        except ValueError:
            value = 0

        x_position = [0.5]

        if self.bar:
            self.bar.remove()
        self.bar = self.ax.bar(x_position, value, width=0.2, color='g')
        self.canvas.draw()

if __name__ == '__main__':
    # don't auto scale when drag app to a different monitor.
    # QApplication.setAttribute(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)

    app = QApplication(sys.argv)
    app.setStyleSheet('''
        QWidget {
            font-size: 30px;
        }
    ''')

    myApp = MyApp()
    myApp.show()

    try:
        sys.exit(app.exec_())
    except SystemExit:
        print('Closing Window...')
