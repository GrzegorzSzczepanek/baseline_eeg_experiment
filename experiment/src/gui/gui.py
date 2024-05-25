import tkinter as tk
import random
from ..eeg_headset import EEGHeadset


class EEGExperiment:
    def __init__(self, root, participant_id):
        self.root = root
        self.root.title("EEG Digit Imagination Experiment")
        self.root.geometry("800x600")

        self.headset = EEGHeadset(participant_id)
        self.digits = [1, 2, 3, 4] # * 20
        # self.digits = [1] # * 20

        random.shuffle(self.digits)

        self.info_screen()

    def info_screen(self):
        self.clear_screen()

        info_text = (
            "Welcome to the EEG Digit Imagination Experiment\n\n"
            "In this experiment, you will see digits displayed on the screen.\n"
            "Your task is to imagine the digit vividly in your mind while it is displayed.\n"
            "The experiment consists of the following steps:\n"
            "1. A fixation cross will appear for 1 second.\n"
            "2. A digit will be displayed for 8 seconds. Imagine this digit as clearly as possible.\n"
            "3. A blank screen will follow for a random duration between 4 to 5 seconds.\n"
            "This sequence will repeat until all digits have been displayed.\n\n"
            "Press 'Start' to begin the experiment. The first screen will be displayed for 1 minute with this information."
        )

        info_label = tk.Label(self.root, text=info_text, font=('Helvetica', 14), justify='left', wraplength=750)
        info_label.pack(expand=True)

        start_button = tk.Button(self.root, text="Start", command=self.start_experiment, font=('Helvetica', 14))
        start_button.pack(pady=20)

    def start_experiment(self):
        self.clear_screen()
        self.headset.start_experiment()
        self.root.after(1000, self.show_fixation_cross)  # Display the info screen for 1 minute

    def show_fixation_cross(self):
        if not self.digits:
            self.thank_you_screen()
            return

        self.clear_screen()
        self.headset.annotate_event("fixation cross")

        fixation_label = tk.Label(self.root, text="+", font=('Helvetica', 48))
        fixation_label.pack(expand=True)

        self.root.after(1000, self.show_digit)  # Show fixation cross for 1 second

    def show_digit(self):
        if not self.digits:
            self.thank_you_screen()
            return

        digit = self.digits.pop(0)
        self.headset.annotate_event(f"digit {digit} shown")

        self.clear_screen()
        digit_label = tk.Label(self.root, text=str(digit), font=('Helvetica', 48))
        digit_label.pack(expand=True)

        self.root.after(8000, self.show_blank_screen)  # Show digit for 8 seconds

    def show_blank_screen(self):
        self.clear_screen()
        self.headset.annotate_event("blank screen")

        blank_duration = random.randint(4000, 5000)  # Blank screen for 4 to 5 seconds
        self.root.after(blank_duration, self.show_fixation_cross)

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def thank_you_screen(self):
        self.clear_screen()
        self.headset.stop_and_save_experiment()

        thank_you_label = tk.Label(self.root, text="Thank you for your participation!", font=('Helvetica', 24))
        thank_you_label.pack(expand=True)