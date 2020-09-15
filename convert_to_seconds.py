import tkinter as tk
from Applications import convert_to_seconds
from tkinter import messagebox


class ConvertToSecondsView:

    def __init__(self, root, function):
        self.root = root
        self.function = function
        self.directions = 'Enter hours and/or minutes to be converted to seconds'

    @staticmethod
    def configs():
        return {
            'font': ('Open Sans', 14),
            'background_color': '#47476b',
            'entry_color': '#d1d1e0',
        }

    def button_convert_to_seconds(self, seconds_label, hours=None, minutes=None):

        hours = hours if hours else 0
        minutes = minutes if minutes else 0

        try:
            hours = float(hours)
            minutes = float(minutes)

            seconds = convert_to_seconds(hours, minutes)
            output = f'{hours} Hours and {minutes} minutes is equivalent to \n {seconds} seconds!'

            seconds_label['text'] = output
            seconds_label.pack()

        except ValueError:
            messagebox.showerror('Incorrect Format',
                                 message='Please provide numbers in decimal format for hours and minutes.\n'
                                         '\nExamples:\n'
                                         '0.0, 1, 100.5 -- ACCEPTABLE \n'
                                         'One Hundred, One point 5, 0.1.002. -- Unacceptable')

    def convert_to_seconds_frame(self):

        configs = self.configs()
        bg_color = configs['background_color']
        entry_color = configs['entry_color']
        font = configs['font']

        convert_to_seconds_window = tk.Toplevel(self.root, bg=bg_color)
        convert_to_seconds_window.title('Convert to Seconds')

        top_frame = tk.Frame(convert_to_seconds_window, bg=bg_color)
        top_frame.pack()

        directions_label = tk.Label(top_frame, text=self.directions, bg=bg_color, justify=tk.CENTER, fg='white',
                                    padx=10, pady=10)
        directions_label.pack(side='top')

        to_convert_frame = tk.Frame(top_frame)
        to_convert_frame.pack()

        hours_label = tk.Label(to_convert_frame, text='Hours: ', bg=bg_color, font=font, fg='white',
                               highlightthickness=0)
        hours_label.pack(side='left')
        hours_entry = tk.Entry(to_convert_frame, bg=entry_color, borderwidth=0, highlightthickness=0)
        hours_entry.pack(side='left')

        tk.LabelFrame(to_convert_frame, width=10, borderwidth=0, highlightthickness=0).pack(side='left')

        minutes_label = tk.Label(to_convert_frame, text='Minutes :', bg=bg_color, font=font, fg='white',
                                 highlightthickness=0, padx=5)
        minutes_label.pack(side='left')
        minutes_entry = tk.Entry(to_convert_frame, bg=entry_color, borderwidth=0, highlightthickness=0)
        minutes_entry.pack(side='left')

        bottom_frame = tk.Frame(convert_to_seconds_window, bg=bg_color)
        bottom_frame.pack()
        tk.LabelFrame(bottom_frame, height=10, bg=bg_color).pack()

        convert_button = tk.Button(bottom_frame, text='Convert to Seconds', justify=tk.CENTER,
                                   highlightbackground=bg_color,
                                   command=lambda: self.button_convert_to_seconds(seconds_label,
                                                                                  hours_entry.get(),
                                                                                  minutes_entry.get()
                                                                                  ))
        seconds_label = tk.Label(bottom_frame, bd=7, bg=entry_color, font=font, pady=7)
        convert_button.pack()

        quit_button = tk.Button(convert_to_seconds_window, text='Quit', justify=tk.RIGHT,
                                highlightbackground=bg_color,
                                command=convert_to_seconds_window.destroy)
        quit_button.pack(side='bottom')
