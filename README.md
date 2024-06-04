Sure, here's an updated README.md with badges for the tech stack and instructions for setting up a virtual environment:

# EEG Digit Recognition

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![MNE](https://img.shields.io/badge/MNE-8AE234?style=for-the-badge&logo=mne&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-013243?style=for-the-badge&logo=matplotlib&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-3776AB?style=for-the-badge&logo=seaborn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)

This project aims to recognize digits from EEG signals. We use MNE-Python for EEG data processing and analysis.

## Project Structure

1. `extract_as_epochs.ipynb` - extracts epochs or ICA from raw EEG data for specific events related to digit recognition.
2. `eda.ipynb` - basic EDA 
3. `models.ipynb` - Machine Learning models in grid search
4. `eeg_headset.py` fully functonal class for eeg data aquisition

## How to Run

1. Clone this repository.
   ```
   git clone https://github.com/GrzegorzSzczepanek/eeg_digit_classification.git
   ```
2. Navigate to the project directory.
   ```
   cd your-repo-name
   ```
3. Create a virtual environment.
   ```
   python3 -m venv env
   ```
4. Activate the virtual environment.
   ```
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```
5. Install the required dependencies.
   ```
   pip install -r requirements.txt
   ```
6. Run the `main.py` script to start the experiment using brainaccess device.

## Functionality

The `create_epochs_for_digits` function in `extract_as_epochs.ipynb` performs the following steps:

1. Loads raw EEG data from .fif files.
2. Converts the data to microvolts and applies a bandpass filter.
3. Extracts events from the raw data and selects those related to digit recognition.
4. Optionally applies Independent Component Analysis (ICA) to the raw data.
5. Creates epochs from the raw data based on the selected events.
6. Saves the epochs to .epo.fif files for further analysis.

## Dependencies

This project uses the following Python libraries:

- MNE
- NumPy
- Matplotlib
- Seaborn
- Pandas

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.
