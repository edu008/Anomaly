from scapy.all import sniff
import threading

class NetworkSniffer:
    def __init__(self, detector):
        self.detector = detector
        self.stop_event = threading.Event()

    def sniff_packets(self):
        try:
            self.detector.logger.log_info("Sniffer started...")
            while not self.stop_event.is_set():
                sniff(timeout=5, prn=self.detector.analyze_packet, store=False)  # Timeout verlängern
                self.detector.detect_anomalies()
                self.detector.reset_counters()  # Reset der Zähler nach Analyse
        except Exception as e:
            self.detector.logger.log_error(f"Error during sniffing: {e}")

    def start(self):
        self.stop_event.clear()
        threading.Thread(target=self.sniff_packets, daemon=True).start()

    def stop(self):
        self.stop_event.set()
        return self.detector.save_log()
        self.detector.logger.log_info("Sniffer stopped and log saved.")
