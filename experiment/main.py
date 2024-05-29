from src import EEGExperiment
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    participant_id = input("Enter participant ID: ")
    app = EEGExperiment(root=root, participant_id=participant_id)
    # app.start()

    root.mainloop()
