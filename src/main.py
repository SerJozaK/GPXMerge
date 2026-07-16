"""
GPXMerge
Main application entry point

Author: SerJozaK
"""

import tkinter as tk
from gui import GPXMergeGUI


def main():
    root = tk.Tk()

    root.title("GPXMerge v1.0")
    root.geometry("900x650")
    root.minsize(900, 650)

    app = GPXMergeGUI(root)

    root.mainloop()


if __name__ == "__main__":
    main()
