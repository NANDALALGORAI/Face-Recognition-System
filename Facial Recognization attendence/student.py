from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk

class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Student Record")

        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_std_email=StringVar()
        self.var_phone_no=StringVar()
        self.var_add=StringVar()
        self.var_cgpa=StringVar()
        self.var_mentor=StringVar()
        self.var_ForG=StringVar()

        img=Image.open(r"D:\Final Year project\Facial Recognization attendence\images\Student1.webp")
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
        f_lbl.place(x=1040,y=0,width=540,height=130)

        #bg image

        img3=Image.open(r"D:\Final Year project\Facial Recognization attendence\images\student2.jpg")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl=Label(bg_img, text="Student Record..", font=("times new roman",35,"bold"),bg="Blue",fg="White")
        title_lbl.place(x=0,y=0,width=1530,height=45)


        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=10,y=55,width=1500,height=650)

        #left lab_frame

        left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("Times New Roman",12,"bold"))
        left_frame.place(x=10,y=10,width=745, height=580)

        img_lf=Image.open(r"D:\Final Year project\Facial Recognization attendence\images\Student1.webp")
        img_lf=img_lf.resize((730,130),Image.ANTIALIAS)   #High level img to Low level img
        self.photoimg_lf=ImageTk.PhotoImage(img_lf)

        first_lb=Label(left_frame, image=self.photoimg_lf)
        first_lb.place(x=10,y=10,width=720,height=130)


  
        #current course
        current_course_frame=LabelFrame(left_frame,bd=2,bg="#f0ecdf",relief=RIDGE,text="Current Course Information",font=("time new roman",13,"bold"))
        current_course_frame.place(x=10,y=135,width=720,height=115)
        
        
        # Department
        dep_label=Label(current_course_frame,text="Department:",font=("time new roman",12,"bold"),bg="#f0ecdf")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("time new roman",12,"bold"),state="readonly",width=20)
        dep_combo['values']=("Select Department","CSE","Civil","Mechanical","ECE")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=5,pady=10,sticky=W)

        # Course
        course_label=Label(current_course_frame,text="Course:",font=("time new roman",12,"bold"),bg="#f0ecdf")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("time new roman",12,"bold"),state="readonly",width=20)
        course_combo['values']=("Select Course","B.Tech","Bsc","M.Tech","Phd")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=5,pady=10,sticky=W)

        # Year
        year_label=Label(current_course_frame,text="Year:",font=("time new roman",12,"bold"),bg="#f0ecdf")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("time new roman",12,"bold"),state="readonly",width=20)
        year_combo['values']=("Select Year","2020-21","2021-22","2022-23","2023-24")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=5,pady=10,sticky=W)

        # Semester
        sem_label=Label(current_course_frame,text="Semester:",font=("time new roman",12,"bold"),bg="#f0ecdf")
        sem_label.grid(row=1,column=2,padx=10,sticky=W)

        sem_combo=ttk.Combobox(current_course_frame,textvariable=self.var_sem,font=("time new roman",12,"bold"),state="readonly",width=20)
        sem_combo['values']=("Select Semester","1st","2nd","3rd","4th","5th","6th")
        sem_combo.current(0)
        sem_combo.grid(row=1,column=3,padx=5,pady=10,sticky=W)

        # Class student Information
        class_student_frame=LabelFrame(left_frame,bd=2,bg="#f0ecdf",relief=RIDGE,text="Student Information",font=("time new roman",13,"bold"))
        class_student_frame.place(x=10,y=250,width=720,height=305)
        
        # Student Id
        studentId_label=Label(class_student_frame,text="Student ID:",font=("time new roman",12,"bold"),bg="#f0ecdf")
        studentId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        studentID_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=20,font=("time new roman",12,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)


        # Student Name
        studentName_label=Label(class_student_frame,text="Student Name:",font=("time new roman",12,"bold"),bg="#f0ecdf")
        studentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentName_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=22,font=("time new roman",12,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)


        # Student Email
        studentEmail_label=Label(class_student_frame,text="Student Email:",font=("time new roman",12,"bold"),bg="#f0ecdf")
        studentEmail_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        studentEmail_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_email,width=20,font=("time new roman",12,"bold"))
        studentEmail_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        # Gender
        studentGender_label=Label(class_student_frame,text="Gender:",font=("time new roman",12,"bold"),bg="#f0ecdf")
        studentGender_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        studentGender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,state="readonly",font=("time new roman",12,"bold"))
        studentGender_combo['values']=("Select Gender","Male","Female","Others")
        studentGender_combo.current(0)
        studentGender_combo.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        # Phone No
        PhoneNo_label=Label(class_student_frame,text="Phone No:",font=("time new roman",12,"bold"),bg="#f0ecdf")
        PhoneNo_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        PhoneNo_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone_no,width=20,font=("time new roman",12,"bold"))
        PhoneNo_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)


        # Address
        address_label=Label(class_student_frame,text="Address:",font=("time new roman",12,"bold"),bg="#f0ecdf")
        address_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        address_entry=ttk.Entry(class_student_frame,textvariable=self.var_add,width=22,font=("time new roman",12,"bold"))
        address_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)
       
       
        # Father/Gardian Name
        Father_Gardian_Name=Label(class_student_frame,text="Father/Gardian:",font=("time new roman",12,"bold"),bg="#f0ecdf")
        Father_Gardian_Name.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        Father_Gardian_Name=ttk.Entry(class_student_frame,textvariable=self.var_ForG,width=20,font=("time new roman",12,"bold"))
        Father_Gardian_Name.grid(row=3,column=1,padx=10,pady=5,sticky=W)
       
        # DOB
        DOB=Label(class_student_frame,text="DOB:",font=("time new roman",12,"bold"),bg="#f0ecdf")
        DOB.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        DOB=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=22,font=("time new roman",12,"bold"))
        DOB.grid(row=3,column=3,padx=10,pady=5,sticky=W)
       
        # Eno
        Eno=Label(class_student_frame,text="E. NO.:",font=("time new roman",12,"bold"),bg="#f0ecdf")
        Eno.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        Eno=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=20,font=("time new roman",12,"bold"))
        Eno.grid(row=4,column=1,padx=10,pady=5,sticky=W)
       
       
        # Mentor 
        Mentor=Label(class_student_frame,text="Mentor:",font=("time new roman",12,"bold"),bg="#f0ecdf")
        Mentor.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        Mentor=ttk.Entry(class_student_frame,textvariable=self.var_mentor,width=22,font=("time new roman",12,"bold"))
        Mentor.grid(row=4,column=3,padx=10,pady=5,sticky=W)
       
        # cgpa
        CGPA=Label(class_student_frame,text="CGPA:",font=("time new roman",12,"bold"),bg="#f0ecdf")
        CGPA.grid(row=5,column=0,padx=10,pady=5,sticky=W)

        CGPA=ttk.Entry(class_student_frame,textvariable=self.var_cgpa,width=20,font=("time new roman",12,"bold"))
        CGPA.grid(row=5,column=1,padx=10,pady=5,sticky=W)

        #Radio Buttons
        self.var_radio1=StringVar()
        radio1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radio1.grid(row=5,column=2)
        
        radio2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radio2.grid(row=5,column=3)


        #  Button Frame
        btn_frame=LabelFrame(class_student_frame,bd=2,bg="#f0ecdf",relief=RIDGE)
        btn_frame.place(x=10,y=210,width=700,height=45)

        #Save btn
        save_btn=Button(btn_frame,text="Save",width=15,font=("time new roman",12,"bold"),bg="grey",fg="white")
        save_btn.grid(row=0,column=0,padx=10,pady=5)

        #Update btn
        update_btn=Button(btn_frame,text="Update",width=15,font=("time new roman",12,"bold"),bg="grey",fg="white")
        update_btn.grid(row=0,column=1,padx=5,pady=5)

        #Delete btn
        delete_btn=Button(btn_frame,text="Delete",width=15,font=("time new roman",12,"bold"),bg="grey",fg="white")
        delete_btn.grid(row=0,column=2,padx=5,pady=5)

        #Reset btn
        Reset_btn=Button(btn_frame,text="Reset",width=15,font=("time new roman",12,"bold"),bg="grey",fg="white")
        Reset_btn.grid(row=0,column=3,padx=10,pady=5)

        # Second Button Frame
        btn_frame_2=LabelFrame(class_student_frame,bd=2,bg="#f0ecdf",relief=RIDGE)
        btn_frame_2.place(x=10,y=245,width=700,height=35)

        #take photo btn
        take_photo_btn=Button(btn_frame_2,text="Take Photo",width=32,font=("time new roman",12,"bold"),bg="grey",fg="white")
        take_photo_btn.grid(row=0,column=0,padx=10)

        #Update photo btn
        # update_photo_btn=Button(btn_frame_2,text="Update Photo",width=32,font=("time new roman",12,"bold"),bg="grey",fg="white")
        # update_photo_btn.grid(row=0,column=1,padx=10)

        #Right label frame

        Right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Students Records",font=("Times New Roman",12,"bold"))
        Right_frame.place(x=740,y=10,width=740,height=580)

if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()