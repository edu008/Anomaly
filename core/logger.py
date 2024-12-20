import logging
import os

class Logger:
    def __init__(self, log_subpath="log/network_activity.log"):
        # Dynamischer Pfad relativ zum aktuellen Arbeitsverzeichnis
        self.log_file_path = os.path.join(os.getcwd(), log_subpath)
        self._configure_logger()

    def _configure_logger(self):
        # Sicherstellen, dass das Verzeichnis existiert
        os.makedirs(os.path.dirname(self.log_file_path), exist_ok=True)

        # Logger konfigurieren
        logging.basicConfig(
            filename=self.log_file_path,
            filemode='a',  # Anhängen an bestehende Datei
            level=logging.INFO,  # Log-Level
            format='%(asctime)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )

        # Konsole als zusätzlichen Handler hinzufügen
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        console_handler.setFormatter(console_formatter)
        logging.getLogger().addHandler(console_handler)

    def log_info(self, message):
        logging.info(message)

    def log_warning(self, message):
        logging.warning(message)

    def log_error(self, message):
        logging.error(message)

    def log_critical(self, message):
        logging.critical(message)
