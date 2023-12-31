from tkinter import Tk
from tkinter.filedialog import askopenfilename
def file_open():
    Tk().withdraw()
    file_path=askopenfilename()
    scan_file(file_path)
def scan_file(file_path):
    with open(file_path, "rb") as f:
        file_content=f.read()
        virus_signature =rb"X50!P%@AP[4\PZX54(P^)7CC)7}$PRATIK-VERMA-TEST-FILE!$H+H*"
        if virus_signature in file_content:
            print("Virus found in file: ",file_path)
        else:
            print("No virus found in file: ",file_path)
file_open()
