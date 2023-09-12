
import tkinter as tk
from tkinter import ttk

class CalcGUI:
    def __init__(self):

        root = tk.Tk()
        root.geometry("400x500")
        s = ttk.Style()
        self.canv = tk.Canvas(root, width=400, height=500, bg="blue")
        self.canv.pack(expand=True, fill="both")
        s.configure('Temp.TFrame', background = self.canv['bg'])
        s.configure('calcB.TButton',background = self.canv['bg'])
        #Main = ttk.Frame(root, width=400, height = 500, style='Main.TFrame')
        #Main.pack(expand=True, fill="both")
        self.canv.columnconfigure(index=0, weight=1)
        self.canv.rowconfigure(index=1,weight=1)
        self.canv.pack_propagate()
        display = ttk.Frame(self.canv, width=400,height=130, style='Temp.TFrame')
        display.pack_propagate(0)       
        display.grid(row=0,column=0)
        result = tk.Label(display,background=self.canv['bg'], relief="sunken")
        result.pack(expand=True,fill="both", padx=10, pady=10)
        buttons = ttk.Frame(self.canv, width=400,height=370, style='Temp.TFrame')
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
                button = tk.Button(buttons,text=listOfButtonNames[ind], background=self.canv['bg'], relief='raised', foreground='white', borderwidth=2, activebackground=self.canv['bg'], activeforeground='white')
                button.grid(row=i,column=j,sticky='news', padx=5, pady=5)
                buttonList.append(button)
                ind += 1

        root.resizable(width=False,height=False)
        root.title("Calculator")
        root.mainloop()

    def gradientBg(canvas):
        (r1, b1, g1) = (102,2,61) # Purple
        (r2, b2, g2) = (255, 155, 8) # Orange
        limit = 640.312423743
        r_ratio = float(r2-r1)/limit
        b_ratio = float(b2-b1)/limit
        g_ratio = float(g2-g1)/limit

        r_mid = float(r2 - r1)/2
        b_mid = float(b2 - b1)/2
        g_mid = float(g2-g1)/2

        x,y = 0,0 # start at (0,0) move diagonally (1,1)
        while(x > 400 and y > 500):  
            canvas.create_line(x,y,x+1,y+1, fill='red')
            x += 1
            y += 1
        # right (goes brighter)

        # left (goes darker)
    gradientBg(self.canv)


        





def main():
    CalcGUI()
    #CalcGUI().gradientBg()

if __name__ == "__main__":
    main()