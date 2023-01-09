from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
from train import Train
from Attendance import attendance
from face_recognition import Face_Recognition
import os

class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1357x790+0+0")
        self.root.title("Face Recognition System")
        
        title_lbl=Label(self.root, text="DEVELOPER", font=("times new roman",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1400,height=55)
        
        img_top=Image.open(r"C:\Users\ADMIN\OneDrive\Desktop\CLASS\FACE RECOG\Images\developer.jpg")
        img_top=img_top.resize((1400,770),Image.Resampling.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=50,width=1400,height=790)
        
        main_frame = Frame(f_lbl,bd=2,bg="lightblue")
        main_frame.place(x=30,y=30,width=300,height=500)
        
        #Developer Info
        dev_label = Label(main_frame,text="XYZ",font=("times new roman",30,"bold"),bg="lightblue")
        dev_label.place(x=0,y=5)
        
if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()