from tkinter import *
import tkinter as tk
from tkinter import ttk

def ui_generateSerialPortControls(root):
    box_serialPort = LabelFrame(root, text='Select port', width=200, height=100)
    # box_serialPort.size([300, 200])
    
    lab = ttk.Label(box_serialPort, text="Port:")
    btn = ttk.Button(box_serialPort, text="Open")
    comboBox = ttk.Combobox(box_serialPort, textvariable=["1", "2", "3"])
    

    box_serialPort.rowconfigure(0, weight=1)
    box_serialPort.rowconfigure(1, weight=1)
    box_serialPort.columnconfigure(0, weight=1)
    box_serialPort.columnconfigure(1, weight=1)

    

    lab.grid(column=0, row=0, padx=5, pady=5)
    btn.grid(column=1, row=1, padx=5, pady=5)
    comboBox.grid(column=1, row=0, padx=5, pady=5)

    
    box_serialPort.place(x=20, y=20)

def main():
    root = Tk()
    root.geometry("1200x800")
    root.resizable(False, False)
    root.call('tk', 'scaling', 1.5)

    ui_generateSerialPortControls(root)

    # box_channel = LabelFrame(root, text='Channel')
    # box_trigger = LabelFrame(root, text='Trigger')
    # box_voltages = LabelFrame(root, text='Volt scale')

    
    

    root.mainloop()


main()