import tkinter as tk
import time
from threading import Thread

# Simulate loading
def show_loading(location_entry, result_label):
    location = location_entry.get()
    if not location.strip():
        result_label.config(text="Please enter a location!")
        return

    result_label.config(text="Finding weather...")
    time.sleep(2)  # Simulate loading
    result_label.config(text="Analyzing weather patterns...")
    time.sleep(2)  # Simulate more loading
    result_label.config(text=f"Result for '{location}':\nGo outside and touch some grass bruh!")

# Start the loading process in a separate thread
def start_prank(location_entry, result_label):
    Thread(target=show_loading, args=(location_entry, result_label)).start()

# Main GUI setup
def main():
    # Create the main window
    root = tk.Tk()
    root.title("Weather App 3000")
    root.geometry("400x300")
    root.resizable(False, False)

    # Instructions
    tk.Label(root, text="Enter Location to Check Weather", font=("Arial", 14)).pack(pady=10)

    # Location input
    location_entry = tk.Entry(root, font=("Arial", 12))
    location_entry.pack(pady=10)

    # Result label
    result_label = tk.Label(root, text="", font=("Arial", 12), wraplength=350, justify="center")
    result_label.pack(pady=20)

    # Prank button
    prank_button = tk.Button(
        root, 
        text="Check Weather", 
        font=("Arial", 12), 
        command=lambda: start_prank(location_entry, result_label)
    )
    prank_button.pack(pady=10)

    # Run the app
    root.mainloop()

# Run the prank app
if __name__ == "__main__":
    main()
