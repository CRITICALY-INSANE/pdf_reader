#pdf_reader for Ronak Bhaiya
import PyPDF2
import tkinter 
from tkinter import filedialog
import tkinter as tk

global loc,once
def nxt():
        m=input("Press Y for another one Or N to exit  (y,n) ")
        if(m=='y' or m=='Y'):
            once()
        else:
            pass
        
def once():
        global loc
        root = tk.Tk()

        loc=filedialog.askopenfilename(initialdir = "/",title = "Select a pdf you want to scrap",filetypes = (("Text files","*.pdf*"),("all files", "*.*")))
        print(loc)
        root.destroy()
        ob=PyPDF2.PdfFileReader(loc)
        print('Document Info')
        print(ob.documentInfo)
        print()
        k=ob.getNumPages()
        print('pages = '+str(k))
        for i in range(1,k):
            print('Page Number = '+str(i))
            print(ob.getPage(i).extractText())

        nxt()
once()
