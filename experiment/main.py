from src import EEGExperiment
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
        
    app = EEGExperiment(root=root, participant_id="P001")
    # app.start()

    root.mainloop()
