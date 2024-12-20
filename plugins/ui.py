import tkinter as tk
from tkinter import messagebox

class NetworkUI:
    def __init__(self, sniffer):
        self.sniffer = sniffer

    def start_sniffing(self):
        self.sniffer.start()
        print("Started sniffing...")

    def stop_sniffing(self):
        log_path = self.sniffer.stop()
        print("Stopped sniffing.")
        messagebox.showinfo("Network Monitoring", f"Log saved to {log_path}")

    def create_ui(self):
        window = tk.Tk()
        window.title("Network Anomaly Detection")

        start_button = tk.Button(window, text="Start Monitoring", command=self.start_sniffing, width=20, height=2, bg="green", fg="white")
        start_button.pack(pady=10)

        stop_button = tk.Button(window, text="Stop Monitoring", command=self.stop_sniffing, width=20, height=2, bg="red", fg="white")
        stop_button.pack(pady=10)

        window.mainloop()
