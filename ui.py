"""
created by Nagaj at 03/07/2021
"""
from tkinter import Tk, Canvas, PhotoImage


class WindowWidget(Tk):
    """"
    ui class for app
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def config(self, title, image=None, is_center=False, **kwargs):
        """
        :param title: window title
        :param image: image title bar
        :param is_center: window to center ?
        :param kwargs: more options like width, height
        :return:
        """
        self.title(title)
        canvas = Canvas(self, width=200, height=224)
        canvas.grid(column=1, row=1)
        super().config(**kwargs)
        if is_center:
            self.__center()
        if image:
            self.iconbitmap(image)

    def __center(self) -> None:
        """
        add window to the center of screen
        :return:
        """
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x_cordinate = int((screen_width / 2) - (self["width"] / 2))
        y_cordinate = int((screen_height / 2) - (self["height"] / 2))
        self.geometry(f'{self["width"]}x{self["height"]}+{x_cordinate}+{y_cordinate}')

    def add_canvas_image(self, w, h, x, y, img_path):
        canvas = Canvas(self, width=w, height=h)
        tomato = PhotoImage(file=img_path)
        canvas.create_image(x, y, image=tomato)

    def run(self):
        """
        keep app opened
        :return:
        """
        self.mainloop()
