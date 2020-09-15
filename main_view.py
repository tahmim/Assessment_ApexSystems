import tkinter as tk
from area_and_max_edge_of_triangle_view import FunctionsOfTrianglesView
from convert_to_seconds import ConvertToSecondsView
from repeat_string_view import RepeatString
from functools import partial


class ApplicationMainView:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Please Pick One')
        self.help_label = None

    @staticmethod
    def configs():
        return {
            'intro_bg_color': '#679bcb',
            'button_font': ('Open Sans', 14),
            'help_message': {
                'area':     'Find the area of a triangle. Enter the numeric values of 2 sides of a triangle and the '
                            'the press the Find Area button to find the area of the triangle',
                'convert':  'Enter the number of hours and minutes you would like to be converted to seconds. If no '
                            'value is entered, a default of 0 will be assigned',
                'max_edge': 'Find the longest edge of a triangle given sides. Enter the numeric values of 2 sides of a '
                            'triangle and then press the Find Max Length button to find the max edge length',
                'repeat':   'Enter a string you would like repeated and how many times you would like the string to be '
                            'repeated'
            }
        }

    def button_hover(self, event, message=None):
        self.help_label.configure(text=message)

    def end_button_hover(self, event):
        self.help_label.configure(text='')

    def main_view(self):

        root = self.root
        configs = self.configs()
        intro_bg_color = configs['intro_bg_color']
        button_font = configs['button_font']

        canvas = tk.Canvas(root, height=400, width=400)
        canvas.pack()
        frame = tk.Frame(root, bg=intro_bg_color, borderwidth=0, highlightthickness=0)
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

        intro_text = 'Hello! Please pick which application you would like to run!'
        tk.Label(frame, text=intro_text, wraplength=300, pady=8, bg=intro_bg_color, fg='white',
                 font=('Open Sans', 20)).pack()

        button_area_triangle = tk.Button(master=frame, text='Area of Triangle', pady=2, font=button_font,
                                         highlightbackground=intro_bg_color, borderwidth=0, highlightthickness=0,
                                         command=lambda: FunctionsOfTrianglesView(root, function='area').area_of_triangle_frame())
        button_area_triangle.pack()

        button_max_edge_triangle = tk.Button(master=frame, text='Max Edge of Triangle', pady=2, font=button_font,
                                             highlightbackground=intro_bg_color,  borderwidth=0, highlightthickness=0,
                                             command=lambda: FunctionsOfTrianglesView(root, function='max_edge').area_of_triangle_frame())
        button_max_edge_triangle.pack()

        button_convert_seconds = tk.Button(master=frame, text='Convert to Seconds', pady=2, font=button_font,
                                           highlightbackground=intro_bg_color, borderwidth=0, highlightthickness=0,
                                           command=lambda: ConvertToSecondsView(root, function='convert_seconds').convert_to_seconds_frame())
        button_convert_seconds.pack()

        button_string_repeat = tk.Button(master=frame, text='Repeat Text', pady=2, font=button_font,
                                         highlightbackground=intro_bg_color, borderwidth=0, highlightthickness=0,
                                         command=lambda: RepeatString(root, function='repeat').repeat_string_frame())
        button_string_repeat.pack()

        self.help_label = tk.Label(master=frame, text='Scroll over buttons for help', font=('Open Sans', 10, 'italic'),
                                   bd=1, relief=tk.SUNKEN, wraplength=280, justify=tk.CENTER, bg='#ffdf80')
        self.help_label.pack(fill=tk.X, side=tk.BOTTOM)

        button_area_triangle.bind('<Enter>', partial(self.button_hover, message=configs['help_message']['area']))
        button_area_triangle.bind('<Leave>', self.end_button_hover)
        button_max_edge_triangle.bind('<Enter>', partial(self.button_hover, message=configs['help_message']['max_edge']))
        button_max_edge_triangle.bind('<Leave>', self.end_button_hover)
        button_convert_seconds.bind('<Enter>', partial(self.button_hover, message=configs['help_message']['convert']))
        button_convert_seconds.bind("<Leave>", self.end_button_hover)
        button_string_repeat.bind('<Enter>', partial(self.button_hover, message=configs['help_message']['repeat']))
        button_string_repeat.bind('<Leave>', self.end_button_hover)
        return root

    def run_app(self):
        root = self.main_view()
        root.mainloop()


if __name__ == '__main__':
    ApplicationMainView().run_app()

'''
    The Applications entry point is the run_app.
    Create an instance of ApplicationMainView and call the run_app method.
    The Application can be run by running this file. 

'''
