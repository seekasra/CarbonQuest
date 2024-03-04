import sys
import requests
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QWidget,
    QTextEdit,
    QLineEdit,
    QLabel,
    QGridLayout,
    QMessageBox,
)
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import datetime
import json


class CarbonIntensityApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("UK Carbon Intensity Data Viewer")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.layout = QGridLayout()

        self.setup_ui()
        self.central_widget.setLayout(self.layout)
        self.setCentralWidget(self.central_widget)

    def setup_ui(self):
        self.current_intensity_btn = QPushButton("Get Current Intensity")
        self.current_intensity_btn.clicked.connect(self.get_current_intensity)

        self.today_intensity_btn = QPushButton("Get Today's Intensity")
        self.today_intensity_btn.clicked.connect(
            lambda: self.get_intensity_for_date(
                datetime.datetime.now().strftime("%Y-%m-%d")
            )
        )

        self.intensity_factors_btn = QPushButton("Get Intensity Factors")
        self.intensity_factors_btn.clicked.connect(self.get_intensity_factors)

        self.date_label = QLabel("Enter Date (YYYY-MM-DD):")
        self.date_input = QLineEdit()

        self.get_date_intensity_btn = QPushButton("Get Intensity for Date")
        self.get_date_intensity_btn.clicked.connect(
            lambda: self.get_intensity_for_date(self.date_input.text())
        )

        self.response_text = QTextEdit()
        self.response_text.setReadOnly(True)

        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)

        self.layout.addWidget(self.current_intensity_btn, 0, 0)
        self.layout.addWidget(self.today_intensity_btn, 0, 1)
        self.layout.addWidget(self.intensity_factors_btn, 0, 2)
        self.layout.addWidget(self.date_label, 1, 0)
        self.layout.addWidget(self.date_input, 1, 1)
        self.layout.addWidget(self.get_date_intensity_btn, 1, 2)
        self.layout.addWidget(self.response_text, 2, 0, 1, 3)
        self.layout.addWidget(self.canvas, 3, 0, 1, 3)

    def fetch_data(self, url):
        try:
            headers = {"Accept": "application/json"}
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Error", str(e))
            return None

    def display_response(self, data: dict):
        self.response_text.setText(json.dumps(data, sort_keys=True, indent=4))

    def get_current_intensity(self):
        data = self.fetch_data("https://api.carbonintensity.org.uk/intensity")
        if data:
            self.display_response(data)

    def get_intensity_today(self):
        self.get_intensity_for_date(datetime.datetime.now().strftime("%Y-%m-%d"))

    def get_intensity_factors(self):
        data = self.fetch_data("https://api.carbonintensity.org.uk/intensity/factors")
        if data:
            self.display_response(data)

    def get_intensity_for_date(self, date):
        if not date:
            QMessageBox.warning(
                self, "Invalid Date", "Please enter a valid date in YYYY-MM-DD format."
            )
            return
        data = self.fetch_data(
            f"https://api.carbonintensity.org.uk/intensity/date/{date}"
        )
        if data:
            self.plot_data(data)

    def plot_data(self, data):
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        dates = []
        intensities = []
        for item in data.get("data", []):
            start = item.get("from")
            intensity = item.get("intensity", {}).get("forecast")
            if start and intensity is not None:
                dates.append(start)
                intensities.append(intensity)

        ax.plot(dates, intensities, marker="o", linestyle="-")
        ax.set_xlabel("Time")
        ax.set_ylabel("Carbon Intensity (gCO2eq/kWh)")
        ax.set_title("Carbon Intensity Forecast")
        ax.tick_params(axis="x", rotation=45)
        self.canvas.draw()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = CarbonIntensityApp()
    mainWin.show()
    sys.exit(app.exec_())
