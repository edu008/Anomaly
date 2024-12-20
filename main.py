from core.logger import Logger
from core.anomaly_detection import AnomalyDetector
from core.network_sniffer import NetworkSniffer
from plugins.ui import NetworkUI

if __name__ == "__main__":
    # Logger mit dynamischem Speicherort initialisieren
    logger = Logger("log/network_activity.log")

    # Thresholds und Ports definieren
    thresholds = {
        "packets_per_second": 100,
        "unique_connections": 50
    }
    common_ports = {80, 443, 22, 21, 25, 110, 445}

    # Komponenten initialisieren
    detector = AnomalyDetector(thresholds, common_ports, logger.log_file_path, logger)
    sniffer = NetworkSniffer(detector)
    ui = NetworkUI(sniffer)

    # UI starten
    logger.log_info("Starting Network Anomaly Detection UI.")
    ui.create_ui()
