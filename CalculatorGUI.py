
import tkinter as tk
from tkinter import ttk

class CalcGUI:
    def __init__(self):

        root = tk.Tk()
        root.geometry("400x500")
        root.columnconfigure(index=0, weight=1)
        root.rowconfigure(index=1,weight=1)
        display = ttk.Frame(root, width=400,height=130)
        display.pack_propagate(0)       
        display.grid(row=0,column=0)
        result = ttk.Label(display,background="red")
        result.pack(expand=True,fill="both", padx=1, pady=1)
        buttons = ttk.Frame(root, width=400,height=370)
        buttons.pack_propagate(0)

        buttons.columnconfigure(index=0,weight=1)
        buttons.columnconfigure(index=1,weight=1)
        buttons.columnconfigure(index=2,weight=1)
        buttons.columnconfigure(index=3,weight=1)
        buttons.rowconfigure(index=0,weight=1)
        buttons.rowconfigure(index=1,weight=1)
        buttons.rowconfigure(index=2,weight=1)
        buttons.rowconfigure(index=3,weight=1)
        buttons.rowconfigure(index=4,weight=1)
        buttons.rowconfigure(index=5,weight=1)
        buttons.grid(row=1,column=0, sticky='news')

       
        # Calculator Buttons
        listOfButtonNames = ['mc','mr','m-','m+','CE','sqr','%','+','7','8','9','X','4','5','6','-','1','2','3','+','0','.','+/-','=']
        buttonList = []
 
        # Init all buttons, places them into the button frame and appends them into the buttonList
        ind = 0
        for i in range(6):
            for j in range(4) :
                button = ttk.Button(buttons,text=listOfButtonNames[ind])
                button.grid(row=i,column=j,sticky='news')
                buttonList.append(button)
                ind += 1

        root.resizable(width=False,height=False)
        root.mainloop()

def main():
    CalcGUI()

if __name__ == "__main__":
    main()