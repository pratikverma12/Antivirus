from tkinter import Tk, Label, filedialog, ttk

class AntivirusApp:
    def __init__(self, master):
        self.master = master
        master.title("Antivirus Scanner")

        style = ttk.Style()
        style.configure("TFrame", background="#ECECEC")
        style.configure("TLabel", background="#ECECEC", font=("Helvetica", 14))
        style.configure("TButton", background="#4CAF50", foreground="white", font=("Helvetica", 12))
        style.map("TButton", background=[("active", "#45a049")])

        self.frame = ttk.Frame(master, style="TFrame")
        self.frame.pack(padx=10, pady=10)

        self.label = ttk.Label(self.frame, text="Welcome to the Antivirus Scanner!", style="TLabel")
        self.label.pack(pady=10)

        self.open_button = ttk.Button(self.frame, text="Open File", command=self.file_open)
        self.open_button.pack(pady=10)

    def file_open(self):
        file_path = filedialog.askopenfilename()
        self.scan_file(file_path)

    def scan_file(self, file_path):
        try:
            with open(file_path, "rb") as f:
                file_content = f.read()
                virus_signature = rb"X50!P%@AP[4\PZX54(P^)7CC)7}$PRATIK-VERMA-TEST-FILE!$H+H*"
                if virus_signature in file_content:
                    result = "Virus found in file: " + file_path
                else:
                    result = "No virus found in file: " + file_path

                self.show_result(result)
        except FileNotFoundError:
            self.show_result("File not selected!")

    def show_result(self, result):
        result_label = ttk.Label(self.frame, text=result, style="TLabel")
        result_label.pack()

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    window.geometry(f"{width}x{height}+{x}+{y}")

if __name__ == "__main__":
    root = Tk()
    app = AntivirusApp(root)
    
    # Set the window size
    window_width = 400
    window_height = 300
    
    # Center the window on the screen
    center_window(root, window_width, window_height)
    
    root.mainloop()
