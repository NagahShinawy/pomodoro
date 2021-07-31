"""
created by Nagaj at 10/07/2021
"""

from ui import WindowWidget
from constants import TOMATO_CANVAS


def main():
    window = WindowWidget()
    window.config(title="Pomodoro", image=TOMATO_CANVAS, is_center=True)
    window.run()


if __name__ == '__main__':
    main()