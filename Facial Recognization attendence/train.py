from cProfile import label
from cgitb import text
from logging import root
from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
# import mysql.connector
# import cv2
import os
import numpy as np



class Train:
    def __init__(self,root) : 
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face recognition system ")

        title_lbl=Label(self.root,text="Training Data Set",font=("times new roman",30,"bold" ),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1538,height=45)

        img_top=Image.open(r"K:\Final_Year_Project\img_used\facialrecognition.png")
        img_top=img_top.resize((1530,325),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=325)

        b1_1=Button(self.root,text="Train Data",cursor="hand2",font=("times new roman",30,"bold"),bg="red",fg="white")
        b1_1.place(x=0,y=380,width=1530,height=60)



        img_bottom=Image.open(r"K:\Final_Year_Project\img_used\peoples.jpg")
        img_bottom=img_bottom.resize((1530,325),Image.ANTIALIAS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=0,y=450,width=1530,height=325)

    def train_classifier(self):
        data_dir= ("")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)] 

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')  #Grey Scale image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.'[1]))


if __name__ =="__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()