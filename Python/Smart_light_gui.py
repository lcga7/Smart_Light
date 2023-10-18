import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
import serial

def on_button_click():
    arduino.write(b'T')  # Send the 'T' command to toggle the LED state

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = QWidget()
    window.setWindowTitle("Simple GUI with Button")

    layout = QVBoxLayout()

    button = QPushButton("Toggle LED")
    button.clicked.connect(on_button_click)

    layout.addWidget(button)
    window.setLayout(layout)
    window.show()

    # Set up the serial connection to the Arduino
    try:
        arduino = serial.Serial('COM3', 9600)  # Replace 'COM3' with the correct serial port
    except serial.SerialException as e:
        print(f"Error: {e}")
        sys.exit(1)

    sys.exit(app.exec_())
