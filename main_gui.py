import tkinter as tk
from ship_gui import ShipGUI

def main():
    root = tk.Tk()
    app = ShipGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main() 