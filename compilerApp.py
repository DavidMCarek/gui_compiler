#!/usr/bin/python

from Tkinter import *
import tkFileDialog
import ScrolledText as stxt
from subprocess import call

class CompilerApplication(Frame):
    def __init__(self, master=None) :
        Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.compileButton = Button(self, text='Compile', command=self.compile)
        self.compileButton.grid(column = 2, row=9)
        self.optimizeText=StringVar()
        self.optimizeValue = IntVar()
        self.optimizeText.set('Optimization Off')
        self.optimizeButton = Checkbutton(self, text = 'Optimization Off', textvariable=self.optimizeText, command=self.optimizeChange, variable=self.optimizeValue)
        self.optimizeButton.grid(column=4, columnspan = 2, row=3)
        self.debuggingValue = IntVar()
        self.debuggingText = StringVar()
        self.debuggingText.set('Debugging Off')
        self.debuggingButton = Checkbutton(self, textvariable=self.debuggingText, command=self.debuggingChange, variable=self.debuggingValue)
        self.debuggingButton.grid(column = 4, columnspan = 2, row=4)
        self.executableFieldLabel =Label(self, text="Executable File Name: ")
        self.executableFieldLabel.grid(column = 1, columnspan = 1, row = 2)
        self.executableFieldValue=StringVar()
        self.executableName = Entry(self, textvariable=self.executableFieldValue, width=32)
        self.executableName.grid(column = 2, columnspan = 3, row = 2)
        self.executableFieldValue.set('a.out')
        self.standardLabel = Label(self, text="Compiler Compliance Level")
        self.standardLabel.grid(column = 4, columnspan=3, row=5)
        self.cValue = IntVar()
        self.c89Radiobutton = Radiobutton(self, text="C 89",  value=89, variable = self.cValue)
        self.c89Radiobutton.grid(column = 5, columnspan=1, row=6)
        self.c99Radiobutton = Radiobutton(self, text="C99", value=99, variable=self.cValue)
        self.c99Radiobutton.grid(column = 5, columnspan=1, row=7)
        self.c11Radiobutton = Radiobutton(self, text="C++11", value=11, variable=self.cValue)
        self.c11Radiobutton.grid(column = 5, columnspan=1, row=8)
        self.c14Radiobutton = Radiobutton(self, text="c++14", value=14, variable=self.cValue)
        self.c14Radiobutton.grid(column = 5, columnspan=1, row=9)
        self.compilerList = StringVar();
        self.compilerListbox = Listbox(self, listvariable=self.compilerList, height=1, width = 48)
        self.compilerListbox.grid(column = 2, columnspan=5, row=1)
        self.compilerListbox.insert(1, '/usr/bin/g++', '/home/gheuring/bin/g++')
        self.compilerListbox['height'] = 2
        self.compilerListbox.selection_set(0)
        self.addFileButton = Button(self, text='Add File', command=self.addFileCommand)
        self.addFileButton.grid(column = 1, columnspan = 1, row = 8)
        self.clearFilesButton = Button(self, text='Clear Files', command = self.clearCommand)
        self.clearFilesButton.grid(column = 3, columnspan = 1, row = 8)
        self.compileFiles = stxt.ScrolledText(self, height=5, width=32)
        self.compileFiles.grid(column = 1, columnspan=3, row=4, rowspan=4)
        
    def compile(self):
        pass
        print self.optimizeValue.get(), ' -- optimize value'
        print self.executableFieldValue.get(), ' -- Executable field value'
        print self.debuggingValue.get(), ' -- debugging value'
        print self.cValue.get(), ' -- C version Value'
        filelist = self.compileFiles.get(0.0, END)
        print filelist
        print self.compilerListbox.get(self.compilerListbox.curselection()[0])
        
        call([item for item in ([self.compilerListbox.get(self.compilerListbox.curselection()[0]), "-O2" if self.optimizeValue.get() else "", "-g" if self.debuggingValue.get() else "", "-o", self.executableFieldValue.get(), "-std=c++" + str(self.cValue.get())] + filelist.split("\n")) if item != ""])
        
        
    def optimizeChange(self):
        if (self.optimizeText.get() == 'Optimization Off') :
            self.optimizeText.set('Optimization On')
        else:
            self.optimizeText.set('Optimization Off')

        pass

    def debuggingChange(self):
        if (self.debuggingText.get() == 'Debugging Off') :
            self.debuggingText.set( 'Debugging On')
        else:
            self.debuggingText.set('Debugging Off')
        
    def addFileCommand(self):
        self.result = tkFileDialog.askopenfilename(parent=self, title='Add File to Project')
        print self.result
        self.result = self.result +"\n"
        self.compileFiles.insert(END, self.result)

    def clearCommand(self) :
        print 'clear files from list'
        self.compileFiles.delete(0.0, END)
        

app = CompilerApplication()
app.master.title("Compiler Application")
app.mainloop()

