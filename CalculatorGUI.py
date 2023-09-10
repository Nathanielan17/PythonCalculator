
import tkinter as tk
from tkinter import ttk

class CalcGUI:
    def __init__(self):

        root = tk.Tk()
        root.geometry("400x500")
        s = ttk.Style()
        canv = tk.Canvas(root, width=400, height=500, bg="blue")
        canv.pack(expand=True, fill="both")
        s.configure('Temp.TFrame', background = canv['bg'])
        s.configure('calcB.TButton',background = canv['bg'])
        #Main = ttk.Frame(root, width=400, height = 500, style='Main.TFrame')
        #Main.pack(expand=True, fill="both")
        canv.columnconfigure(index=0, weight=1)
        canv.rowconfigure(index=1,weight=1)
        canv.pack_propagate()
        display = ttk.Frame(canv, width=400,height=130, style='Temp.TFrame')
        display.pack_propagate(0)       
        display.grid(row=0,column=0)
        result = tk.Label(display,background=canv['bg'], relief="sunken")
        result.pack(expand=True,fill="both", padx=10, pady=10)
        buttons = ttk.Frame(canv, width=400,height=370, style='Temp.TFrame')
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
                button = tk.Button(buttons,text=listOfButtonNames[ind], background=canv['bg'], relief='raised', foreground='white', borderwidth=2, activebackground=canv['bg'], activeforeground='white')
                button.grid(row=i,column=j,sticky='news', padx=5, pady=5)
                buttonList.append(button)
                ind += 1

        root.resizable(width=False,height=False)
        root.title("Calculator")
        root.mainloop()

def main():
    CalcGUI()

if __name__ == "__main__":
    main()