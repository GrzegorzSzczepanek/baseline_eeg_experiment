import os
from typing import Optional

import brainaccess.core as bacore
from brainaccess.core.eeg_manager import EEGManager
from brainaccess.utils import acquisition

from .eeg_config import DATA_FOLDER_PATH, PORT, USED_DEVICE


class EEGHeadset:
    def __init__(self, participant_id: str) -> None:
        """
        Args:
            participant_id (str): ID to use as folder name for saved data.
        """

        self._is_started: bool = False
        self._is_connected: bool = False

        self._save_dir_path: str = os.path.join(DATA_FOLDER_PATH, participant_id)
        # Initialization of the library
        bacore.init(bacore.Version(2, 0, 0))
        self._create_dir_if_not_exist(DATA_FOLDER_PATH)
        self._create_dir_if_not_exist(self._save_dir_path)

    def _connect(self) -> None:
        """
        Raises:
            RuntimeError: If cannot connect to the headset.
        """

        self._eeg_manager = EEGManager()
        self._eeg_acquisition = acquisition.EEG()
        # Connecting to the headset
        self._eeg_acquisition.setup(self._eeg_manager, USED_DEVICE, port=PORT)
        self._is_connected = True

    def _disconnect(self) -> None:
        """
        Raises:
            RuntimeError: If there is no connection to the headset or cannot disconnect.
        """

        if self._is_started:
            raise RuntimeError("Acquisition is still ongoing.")

        if not self._is_connected:
            raise RuntimeError("The EEG headset is not connected.")

        self._eeg_manager.disconnect()

    def start_experiment(self) -> None:
        """
        Start the EEG acquisition for the experiment.
        """

        if self._is_started:
            raise RuntimeError("Experiment is already started.")

        self._connect()
        self._eeg_acquisition.start_acquisition()
        self._is_started = True

    def stop_and_save_experiment(self) -> None:
        """
        Raises:
            RuntimeError: If block was not started.
        """

        # Pobranie danych EEG
        self._eeg_acquisition.get_mne()

        # Zapisanie danych do pliku
        file_path = os.path.join(
            self._save_dir_path, f"EEG_raw.fif"
        )
        self._eeg_acquisition.data.save(file_path)

        self._is_started = False

        # przerwanie akwizycji
        self._eeg_acquisition.stop_acquisition()
        self._eeg_manager.clear_annotations()
        self._disconnect()



    def annotate_event(self, event: str) -> None:
        """
        Annotate the EEG data with a specific event.

        Args:
            event (str): Description of the event to annotate.
        """
        if not self._is_connected:
            raise RuntimeError("The headset is not connected.")

        self._eeg_acquisition.annotate(event)

    def _create_dir_if_not_exist(self, path: str) -> None:
        if not os.path.exists(path):
            os.mkdir(path)
