import tkinter as tk
from Applications import area_of_triangle, max_side_of_triangle
from tkinter import messagebox


class FunctionsOfTrianglesView:

    def __init__(self, root, function):
        self.root = root
        self.function = function

    @staticmethod
    def configs():

        triangles = {
            'area': {
                'background_color':         '#ff9999',
                'entry_background_color':   '#ffe6e6',
                'font':                     ('Open Sans', 14),
                'title':                    'Find the Area of a Triangle',
                'result_text':              f'The area of the triangle is:',
                'fn_button_attr':           {'text': 'Find Area',
                                             },
            },
            'max_edge': {
                'background_color':         '#df9fbf',
                'entry_background_color':   '#f9ebf2',
                'font':                     ('Open Sans', 14),
                'title':                    'Find the Max Length of a Triangle',
                'result_text':              f'The max side length of a triangle is:',
                'fn_button_attr':           {'text': 'Find Max Length',
                                             }
            }
        }

        return triangles

    def button_triangle_function(self, side1, side2, frame):

        if not side1 or not side2:
            messagebox.showwarning(title='Missing Side',
                                   message='Please fill in the numeric lengths for both sides')

        try:
            side1 = float(side1)
            side2 = float(side2)

            if self.function == 'area':
                area = area_of_triangle(side1, side2)
                result = f'The area of the triangle is: {area}'
            elif self.function == 'max_edge':
                max_length = max_side_of_triangle(side1, side2)
                result = f'The max side length of a triangle is: {max_length}'

            frame['text'] = result
            frame.pack()

        except ValueError:
            messagebox.showerror(title='Input Error',
                                 message='Please provide decimal numbers as side length inputs')

    def area_of_triangle_frame(self):

        configs = self.configs()[self.function]
        bg_color = configs['background_color']
        font = configs['font']
        entry_bg_color = configs['entry_background_color']

        area_of_triangle_window = tk.Toplevel(self.root,
                                              bg=bg_color,
                                              borderwidth=0,
                                              highlightthickness=0,
                                              highlightbackground=bg_color)
        area_of_triangle_window.title(configs['title'])

        top_frame = tk.Frame(area_of_triangle_window,
                             bg=bg_color,
                             borderwidth=0,
                             highlightthickness=0,
                             highlightbackground=bg_color)
        top_frame.pack()

        directions_label = tk.Label(top_frame,
                                    text='Enter the numeric values of 2 sides of a Triangle',
                                    borderwidth=0,
                                    bg=bg_color,
                                    highlightthickness=0,
                                    justify=tk.CENTER,
                                    padx=10,
                                    pady=10)
        directions_label.pack(side='top')

        side1_frame = tk.Frame(top_frame, bg=bg_color)
        side1_frame.pack()

        side1_label = tk.Label(side1_frame, text='Side 1', bg=bg_color, font=font, justify=tk.LEFT, padx=5)
        side1_label.pack(side='left')

        side1_entry = tk.Entry(side1_frame, bg=entry_bg_color, borderwidth=0, highlightthickness=0, justify=tk.LEFT)
        side1_entry.pack(side='left')

        side2_frame = tk.Frame(top_frame, bg=bg_color)
        side2_frame.pack()

        side2_label = tk.Label(side2_frame, text='Side 2', bg=bg_color, font=font, justify=tk.LEFT, padx=5)
        side2_label.pack(side='left')
        side2_entry = tk.Entry(side2_frame, bg=entry_bg_color, borderwidth=0, highlightthickness=0, justify=tk.LEFT)
        side2_entry.pack(side='left')

        function_button = tk.Button(top_frame,
                                    borderwidth=0,
                                    font=font,
                                    justify=tk.CENTER,
                                    highlightbackground=bg_color,
                                    highlightthickness=0,
                                    command=lambda: self.button_triangle_function(side1_entry.get(),
                                                                                  side2_entry.get(),
                                                                                  result_label))
        function_button.configure(configs['fn_button_attr'])
        function_button.pack()

        bottom_frame = tk.Frame(area_of_triangle_window, bd=7, bg=entry_bg_color, pady=7)
        bottom_frame.pack()
        result_label = tk.Label(bottom_frame, bg=entry_bg_color)

        quit_button = tk.Button(area_of_triangle_window,
                                text='Quit',
                                borderwidth=0,
                                highlightbackground=bg_color,
                                highlightthickness=0,
                                justify=tk.RIGHT,
                                command=area_of_triangle_window.destroy)
        quit_button.pack(side='bottom')
