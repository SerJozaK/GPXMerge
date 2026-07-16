import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox


class GPXMergeGUI:

    def __init__(self, root):

        self.root = root
        self.files = []

        self.create_widgets()

    def create_widgets(self):

        top = ttk.Frame(self.root)
        top.pack(fill="x", padx=10, pady=10)

        ttk.Button(
            top,
            text="Add GPX",
            command=self.add_files,
            width=20
        ).pack(side="left", padx=5)

        ttk.Button(
            top,
            text="Remove",
            command=self.remove_selected,
            width=20
        ).pack(side="left", padx=5)

        ttk.Button(
            top,
            text="Merge",
            command=self.merge_tracks,
            width=20
        ).pack(side="left", padx=5)

        ttk.Button(
            top,
            text="Export",
            command=self.export_track,
            width=20
        ).pack(side="left", padx=5)

        columns = ("File",)

        self.tree = ttk.Treeview(
            self.root,
            columns=columns,
            show="headings",
            height=20
        )

        self.tree.heading("File", text="Loaded GPX Files")

        self.tree.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        bottom = ttk.LabelFrame(
            self.root,
            text="Statistics"
        )

        bottom.pack(
            fill="x",
            padx=10,
            pady=10
        )

        self.stats = tk.Text(
            bottom,
            height=8
        )

        self.stats.pack(
            fill="x",
            padx=10,
            pady=10
        )

        self.stats.insert(
            "1.0",
            "No GPX loaded.\n"
        )

    def add_files(self):

        filenames = filedialog.askopenfilenames(
            title="Select GPX files",
            filetypes=[
                ("GPX files", "*.gpx")
            ]
        )

        for f in filenames:

            if f not in self.files:

                self.files.append(f)

                self.tree.insert(
                    "",
                    "end",
                    values=(f,)
                )

        self.update_statistics()

    def remove_selected(self):

        selected = self.tree.selection()

        for item in selected:

            file = self.tree.item(item)["values"][0]

            if file in self.files:
                self.files.remove(file)

            self.tree.delete(item)

        self.update_statistics()

    def merge_tracks(self):

        messagebox.showinfo(
            "Information",
            "Track merge engine will be added in Phase 1.2"
        )

    def export_track(self):

        messagebox.showinfo(
            "Information",
            "Export engine will be added in Phase 1.3"
        )

    def update_statistics(self):

        self.stats.delete("1.0", tk.END)

        self.stats.insert(
            tk.END,
            f"Loaded GPX files : {len(self.files)}\n"
        )

        for file in self.files:

            self.stats.insert(
                tk.END,
                file + "\n"
            )
