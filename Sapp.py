from textblob import TextBlob
from tkinter import *;

def correct_spelling():
    get_data=input1.get()
    corr=TextBlob(get_data)
    data=corr.correct()
    input2.delete(0,END)
    input2.insert(0,data)
def main_window():
    global input1,input2
    win=Tk()
    win.geometry("400x400")
    win.resizable(False,False)
    win.config(bg="Pink")
    win.title("SPELLCR")

    label1=Label(win,text="Incorrect Spelling",font=("Time New Roman",15,"bold"),bg='Maroon',fg="White")
    label1.place(x=50,y=30,height=40,width=300)
    # label2=Label(win,text="Correct Spelling")
    label2 = Label(win, text="Correct Spelling", font=("Time New Roman", 15, "bold"), bg='Blue', fg="White")
    label2.place(x=50, y=170, height=40, width=300)

    input1=Entry(win,font=("Time New Roman",15))
    input1.place(x=30,y=80,height=40,width=340)

    input2 = Entry(win, font=("Time New Roman", 15))
    input2.place(x=30, y=220, height=40, width=340)

    button1=Button(win,text="Done",font=("Harlow Solid Italic ", 15, "bold"),bg="yellow",command=correct_spelling)
    button1.place(x=135,y=280,height=40,width=140)

    win.mainloop()

main_window()

