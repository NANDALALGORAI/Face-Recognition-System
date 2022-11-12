from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        img=Image.open(r"D:\Final Year project\Facial Recognization attendence\images\face recog.jpg")
        img=img.resize((510,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=510,height=130)

        img1=Image.open(r"D:\Final Year project\Facial Recognization attendence\images\download.jpg")
        img1=img1.resize((530,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=510,y=0,width=530,height=130)

        img2=Image.open(r"D:\Final Year project\Facial Recognization attendence\images\images.jpg")
        img2=img2.resize((540,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=500,height=130)


        #bg image

        img3=Image.open(r"D:\Final Year project\Facial Recognization attendence\images\bg.jpg")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl=Label(bg_img, text="Face Recogniton Attendence System Software", font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        #student button

        img4=Image.open(r"D:\Final Year project\Facial Recognization attendence\images\student.jpg")
        img4=img4.resize((220,220),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,cursor="hand2")
        b1.place(x=200, y=100, width=220,height=220)

        b1_1=Button(bg_img,text="Student Details",cursor="hand2", font=("times new roman",20,"bold"),bg="red",fg="white")
        b1_1.place(x=200, y=300, width=220,height=40)

        #Detect Face

        img5=Image.open(r"D:\Final Year project\Facial Recognization attendence\images\detect_face.jpg")
        img5=img5.resize((220,220),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b2=Button(bg_img,image=self.photoimg5,cursor="hand2")
        b2.place(x=500, y=100, width=220,height=220)

        b2_2=Button(bg_img,text="Detect Face",cursor="hand2", font=("times new roman",20,"bold"),bg="red",fg="white")
        b2_2.place(x=500, y=300, width=220,height=40)

        img6=Image.open(r"D:\Final Year project\Facial Recognization attendence\images\download.png")
        img6=img6.resize((220,220),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b3=Button(bg_img,image=self.photoimg6,cursor="hand2")
        b3.place(x=800, y=100, width=220,height=220)

        b3_3=Button(bg_img,text="Attendence",cursor="hand2", font=("times new roman",20,"bold"),bg="red",fg="white")
        b3_3.place(x=800, y=300, width=220,height=40)

        img7=Image.open(r"D:\Final Year project\Facial Recognization attendence\images\help.png")
        img7=img7.resize((220,220),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b4=Button(bg_img,image=self.photoimg7,cursor="hand2")
        b4.place(x=1100, y=100, width=220,height=220)

        b4_4=Button(bg_img,text="Help Desk",cursor="hand2", font=("times new roman",20,"bold"),bg="red",fg="white")
        b4_4.place(x=1100, y=300, width=220,height=40)


        #second row Button

        img8=Image.open(r"D:\Final Year project\Facial Recognization attendence\images\train.jpg")
        img8=img8.resize((220,220),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b5=Button(bg_img,image=self.photoimg8,cursor="hand2")
        b5.place(x=200, y=400, width=220,height=220)

        b5_5=Button(bg_img,text="Train Data",cursor="hand2", font=("times new roman",20,"bold"),bg="red",fg="white")
        b5_5.place(x=200, y=600, width=220,height=40)

        

        img9=Image.open(r"D:\Final Year project\Facial Recognization attendence\images\photos.jpg")
        img9=img9.resize((220,220),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b6=Button(bg_img,image=self.photoimg9,cursor="hand2")
        b6.place(x=500, y=400, width=220,height=220)

        b6_6=Button(bg_img,text="Photos",cursor="hand2", font=("times new roman",20,"bold"),bg="red",fg="white")
        b6_6.place(x=500, y=600, width=220,height=40)

        img10=Image.open(r"D:\Final Year project\Facial Recognization attendence\images\developer.jpg")
        img10=img10.resize((220,220),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b7=Button(bg_img,image=self.photoimg10,cursor="hand2")
        b7.place(x=800, y=400, width=220,height=220)

        b7_7=Button(bg_img,text="Developer",cursor="hand2", font=("times new roman",20,"bold"),bg="red",fg="white")
        b7_7.place(x=800, y=600, width=220,height=40)

        img11=Image.open(r"D:\Final Year project\Facial Recognization attendence\images\Exit.jpg")
        img11=img11.resize((220,220),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b8=Button(bg_img,image=self.photoimg11,cursor="hand2")
        b8.place(x=1100, y=400, width=220,height=220)

        b8_8=Button(bg_img,text="Exit",cursor="hand2", font=("times new roman",20,"bold"),bg="red",fg="white")
        b8_8.place(x=1100, y=600, width=220,height=40)






if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()