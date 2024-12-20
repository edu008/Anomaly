from collections import Counter
import json
import os
from scapy.all import IP, TCP, UDP

class AnomalyDetector:
    def __init__(self, thresholds, common_ports, log_file_path, logger):
        self.THRESHOLD_PACKETS_PER_SECOND = thresholds['packets_per_second']
        self.THRESHOLD_UNIQUE_CONNECTIONS = thresholds['unique_connections']
        self.COMMON_PORTS = common_ports
        self.LOG_FILE_PATH = log_file_path
        self.logger = logger

        self.packet_counts = Counter()
        self.connection_counts = Counter()
        self.port_usage = Counter()

        self.log_data = {
            "alerts": [],
            "traffic_summary": {
                "packet_counts": {},
                "unique_connections": 0,
                "unusual_ports": []
            }
        }

    def reset_counters(self):
        """Reset all counters for the next monitoring interval."""
        self.packet_counts = Counter()
        self.connection_counts = Counter()
        self.port_usage = Counter()

    def analyze_packet(self, packet):
        if IP in packet:
            src_ip = packet[IP].src
            dest_ip = packet[IP].dst
            self.logger.log_info(f"Packet captured: {src_ip} -> {dest_ip}")

            if TCP in packet or UDP in packet:
                port = packet[TCP].dport if TCP in packet else packet[UDP].dport
                self.port_usage[port] += 1
            self.packet_counts[src_ip] += 1
            connection = tuple(sorted((src_ip, dest_ip)))
            self.connection_counts[connection] += 1

    def detect_anomalies(self):
    # Temporäre Liste, um neue Alerts zu speichern
        alerts = []

        # Check for high packet rates
        for ip, count in self.packet_counts.items():
            if count > self.THRESHOLD_PACKETS_PER_SECOND:
                alert = f"High packet rate detected from IP: {ip} ({count} packets/second)"
                self.logger.log_warning(alert)  # Warnung loggen
                alerts.append(alert)

        # Check for a large number of unique connections
        if len(self.connection_counts) > self.THRESHOLD_UNIQUE_CONNECTIONS:
            alert = f"High number of unique connections detected: {len(self.connection_counts)}"
            self.logger.log_warning(alert)
            alerts.append(alert)

        # Check for unusual port usage
        unusual_ports = [port for port in self.port_usage if port not in self.COMMON_PORTS]
        if unusual_ports:
            alert = f"Unusual ports detected: {unusual_ports}"
            self.logger.log_warning(alert)
            alerts.append(alert)

        # Neue Alerts zu `log_data` hinzufügen
        self.log_data["alerts"].extend(alerts)

        # Traffic-Übersicht aktualisieren
        self.log_data["traffic_summary"]["packet_counts"] = dict(self.packet_counts)
        self.log_data["traffic_summary"]["unique_connections"] = len(self.connection_counts)
        self.log_data["traffic_summary"]["unusual_ports"] = unusual_ports

    # Debug-Ausgabe der aktualisierten `log_data`
        self.logger.log_info(f"Updated log data: {self.log_data}")

    # Daten in die JSON-Datei speichern
        self.save_log()

    def save_log(self):
        try:
        # Sicherstellen, dass das Verzeichnis existiert
            os.makedirs(os.path.dirname(self.LOG_FILE_PATH), exist_ok=True)

        # Debug-Ausgabe, um sicherzustellen, dass log_data korrekt ist
            self.logger.log_info(f"Saving log data: {json.dumps(self.log_data, indent=4)}")

        # Log-Daten in die Datei schreiben
            with open(self.LOG_FILE_PATH, 'w') as log_file:
                json.dump(self.log_data, log_file, indent=4)

            self.logger.log_info(f"Log saved to {self.LOG_FILE_PATH}")
        except Exception as e:
            self.logger.log_error(f"Error saving log file: {e}")


