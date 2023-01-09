from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
from train import Train
from Attendance import attendance
from face_recognition import Face_Recognition
from developer import Developer
import os

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1357x790+0+0")
        self.root.title("Face Recognition System")
        #first image
        img=Image.open(r"C:\Users\ADMIN\OneDrive\Desktop\CLASS\FACE RECOG\Images\bg_img.jpg")
        img=img.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)
        
        #second image
        img1=Image.open(r"C:\Users\ADMIN\OneDrive\Desktop\CLASS\FACE RECOG\Images\bg_img.jpg")
        img1=img1.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)
        
        #third image
        img2=Image.open(r"C:\Users\ADMIN\OneDrive\Desktop\CLASS\FACE RECOG\Images\bg_img.jpg")
        img2=img2.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=500,height=130)

        #bg image
        img3=Image.open(r"C:\Users\ADMIN\OneDrive\Desktop\CLASS\FACE RECOG\Images\main_background.jpg")
        img3=img3.resize((1530,710),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)
        
        #label title
        title_lbl=Label(bg_img, text="FACE RECOGNITION ATTENDANCE SYSTEM", font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1400,height=45)

        #student button
        img4=Image.open(r"C:\Users\ADMIN\OneDrive\Desktop\CLASS\FACE RECOG\Images\student_icon.png")
        img4=img4.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=100, y=60, width=220,height=220)

        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2", font=("times new roman",20,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=100, y=270, width=220,height=40)

        #Detect Face
        img5=Image.open(r"C:\Users\ADMIN\OneDrive\Desktop\CLASS\FACE RECOG\Images\detect_face.png")
        img5=img5.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b2=Button(bg_img,image=self.photoimg5,command=self.face_data,cursor="hand2")
        b2.place(x=400, y=60, width=220,height=220)

        b2_2=Button(bg_img,text="Detect Face",command=self.face_data,cursor="hand2", font=("times new roman",20,"bold"),bg="darkblue",fg="white")
        b2_2.place(x=400, y=270, width=220,height=40)

        #Attendance Button
        img6=Image.open(r"C:\Users\ADMIN\OneDrive\Desktop\CLASS\FACE RECOG\Images\attendance_button.jpg")
        img6=img6.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b3=Button(bg_img,image=self.photoimg6,command=self.attendance_data,cursor="hand2")
        b3.place(x=700, y=60, width=220,height=220)

        b3_3=Button(bg_img,text="Attendance",command=self.attendance_data,cursor="hand2", font=("times new roman",20,"bold"),bg="darkblue",fg="white")
        b3_3.place(x=700, y=270, width=220,height=40)

        #Help Desk Button
        img7=Image.open(r"C:\Users\ADMIN\OneDrive\Desktop\CLASS\FACE RECOG\Images\help_desk.png")
        img7=img7.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b4=Button(bg_img,image=self.photoimg7,cursor="hand2")
        b4.place(x=1000, y=60, width=220,height=220)

        b4_4=Button(bg_img,text="Help Desk",cursor="hand2", font=("times new roman",20,"bold"),bg="darkblue",fg="white")
        b4_4.place(x=1000, y=270, width=220,height=40)

        #second row Button
        
        #Train Face Button
        img8=Image.open(r"C:\Users\ADMIN\OneDrive\Desktop\CLASS\FACE RECOG\Images\train_face.jpg")
        img8=img8.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b5=Button(bg_img,image=self.photoimg8,command=self.training,cursor="hand2")
        b5.place(x=100, y=320, width=220,height=220)

        b5_5=Button(bg_img,text="Train Data",command=self.training,cursor="hand2", font=("times new roman",20,"bold"),bg="darkblue",fg="white")
        b5_5.place(x=100, y=520, width=220,height=40)

        #Photos
        img9=Image.open(r"C:\Users\ADMIN\OneDrive\Desktop\CLASS\FACE RECOG\Images\photos.png")
        img9=img9.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b6=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b6.place(x=400, y=320, width=220,height=220)

        b6_6=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img, font=("times new roman",20,"bold"),bg="darkblue",fg="white")
        b6_6.place(x=400, y=520, width=220,height=40)

        #Developer
        img10=Image.open(r"C:\Users\ADMIN\OneDrive\Desktop\CLASS\FACE RECOG\Images\developer_icon.png")
        img10=img10.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b7=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.developer_data)
        b7.place(x=700, y=320, width=220,height=220)

        b7_7=Button(bg_img,text="Developer",cursor="hand2",command=self.developer_data, font=("times new roman",20,"bold"),bg="darkblue",fg="white")
        b7_7.place(x=700, y=520, width=220,height=40)

        #Exit
        img11=Image.open(r"C:\Users\ADMIN\OneDrive\Desktop\CLASS\FACE RECOG\Images\exit_icon.png")
        img11=img11.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b8=Button(bg_img,image=self.photoimg11,cursor="hand2")
        b8.place(x=1000, y=320, width=220,height=220)

        b8_8=Button(bg_img,text="Exit",cursor="hand2", font=("times new roman",20,"bold"),bg="darkblue",fg="white")
        b8_8.place(x=1000, y=520, width=220,height=40)

    def open_img(self):
        os.startfile("data")
        #Function Buttons
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app = Student(self.new_window)
    def training(self):
        self.new_window=Toplevel(self.root)
        self.app = Train(self.new_window)
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)
    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=attendance(self.new_window)
    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)



if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()