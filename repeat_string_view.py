import tkinter as tk
from Applications import recursive_string_repeat
from tkinter import messagebox


class RepeatString:

    def __init__(self, root, function):
        self.root = root
        self.function = function

    @staticmethod
    def configs():
        return {
            'background_color': '#9fdf9f',
            'text_font': ('Open Sans', 14)
        }

    def button_repeat_string(self, string, repetitions, label):

        try:
            string = str(string)
            repetitions = int(repetitions)

            repeated = recursive_string_repeat(string, int(repetitions))

            output = f'Output is:\n {repeated}'

            label['text'] = output
            label.pack()

        except ValueError:
            messagebox.showerror('Incorrect Input',
                                 message='Please provide ASCII values for the string which is to be repeated and '
                                         'integer values for how many times the string is to be repeated.')

    def repeat_string_frame(self):

        configs = self.configs()
        bg_color = configs['background_color']
        text_font = configs['text_font']

        repeat_string_window = tk.Toplevel(self.root, bg=bg_color, borderwidth=0, highlightthickness=0)
        repeat_string_window.title('Repeat String')

        top_frame = tk.Frame(repeat_string_window, borderwidth=0, highlightthickness=0, bg=bg_color, pady=10)
        top_frame.pack()

        string_inputs_frame = tk.Frame(repeat_string_window, bg=bg_color, borderwidth=0, highlightthickness=0)
        string_inputs_frame.pack()

        tk.Label(string_inputs_frame, text='What is the string you would like repeated?', font=text_font, bg=bg_color,
                 borderwidth=0, highlightthickness=0, padx=10, pady=10).pack(side='left')
        string_entry = tk.Entry(string_inputs_frame, bg='#ecf9ec', borderwidth=0, highlightthickness=0)
        string_entry.pack(side='right')

        int_inputs_frame = tk.Frame(repeat_string_window, borderwidth=0, highlightthickness=0, bg=bg_color)
        int_inputs_frame.pack()

        tk.LabelFrame(int_inputs_frame, pady=3).pack()

        tk.Label(int_inputs_frame, text='How many times would you like the string to be repeated?', font=text_font,
                 bg=bg_color, borderwidth=0, highlightthickness=0, padx=10).pack(side='left')
        repeat_int_entry = tk.Entry(int_inputs_frame, bg='#ecf9ec', borderwidth=0, highlightthickness=0)
        repeat_int_entry.pack(side='right')

        repeat_string_button = tk.Button(repeat_string_window, text='Repeat String', justify=tk.CENTER, pady=10,
                                         borderwidth=0, highlightthickness=0, highlightbackground=bg_color,
                                         command=lambda: self.button_repeat_string(string_entry.get(),
                                                                                   repeat_int_entry.get(),
                                                                                   results))
        repeat_string_button.pack()

        results = tk.Label(repeat_string_window, wraplength=250, bg='#ecf9ec', bd=7, pady=7)

        quit_button = tk.Button(repeat_string_window, text='Quit', justify=tk.RIGHT,
                                borderwidth=0, highlightthickness=0, highlightbackground=bg_color,
                                command=repeat_string_window.destroy)
        quit_button.pack(side='bottom')
