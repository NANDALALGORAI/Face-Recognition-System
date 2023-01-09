from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1357x790+0+0")
        self.root.title("Face Recognition System")
        
        #variables
        self.var_dept = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester=StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()
        
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
        title_lbl=Label(bg_img, text="STUDENT REGISTRATION", font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1400,height=45)
        
        main_frame = Frame(bg_img,bd=2,bg="lightblue")
        main_frame.place(x=0,y=50,width=1357,height=650)
        
        #left_label_frame
        
        Left_frame = LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"),bg="lightblue",fg="black")
        Left_frame.place(x=0,y=0,width=650,height=500)
        
        img_left=Image.open(r"C:\Users\ADMIN\OneDrive\Desktop\CLASS\FACE RECOG\Images\bg_img.jpg")
        img_left=img_left.resize((700,300),Image.Resampling.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl_left=Label(Left_frame,image=self.photoimg_left)
        f_lbl_left.place(x=0,y=0,width=640,height=100)
        
        #current_course
        current_course_frame = LabelFrame(Left_frame,bd=2,relief=RIDGE,text="Current Course Info",font=("times new roman",12,"bold"),bg="lightblue",fg="black")
        current_course_frame.place(x=5,y=105,width=650,height=120)
        
        #department
        dep_label = Label(current_course_frame,text="Department",font=("times new roman",12,"bold"),bg="lightblue")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)
        dep_combo = ttk.Combobox(current_course_frame,textvariable=self.var_dept,font=("times new roman",12,"bold"),state="read only",width=17)
        dep_combo["values"] = ("Select Department","Computer","IT","Civil","Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
        #course
        course_label = Label(current_course_frame,text="Course",font=("times new roman",12,"bold"),bg="lightblue")
        course_label.grid(row=0,column=2,padx=10,sticky=W)
        course_combo = ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),state="read only",width=17)
        course_combo["values"] = ("Select Course","FE","SE","TE","BE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)
        
        #year
        year_label = Label(current_course_frame,text="Year",font=("times new roman",12,"bold"),bg="lightblue")
        year_label.grid(row=1,column=0,padx=10,sticky=W)
        year_combo = ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),state="read only",width=17)
        year_combo["values"] = ("Select Year","2020-21","2021-22","2022-23","2023-24")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)
        
        #semester
        semester_label = Label(current_course_frame,text="Semester",font=("times new roman",12,"bold"),bg="lightblue")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)
        semester_combo = ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),state="read only",width=17)
        semester_combo["values"] = ("Select Semester","Sem-1","Sem-2","Sem-3","Sem-4","Sem-5")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)
        
        #class information
        class_info_frame = LabelFrame(Left_frame,bd=2,relief=RIDGE,text="Class Student Info",font=("times new roman",12,"bold"),bg="lightblue",fg="black")
        class_info_frame.place(x=5,y=230,width=650,height=300)
        
        #student ID
        studentId_label = Label(class_info_frame,text="Student ID:",font=("times new roman",12,"bold"),bg="lightblue")
        studentId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        studentID_entry = ttk.Entry(class_info_frame,textvariable=self.var_std_id,width=20,font=("times new roman",12,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10,sticky=W)
        
        #student name
        studentname_label = Label(class_info_frame,text="Student Name:",font=("times new roman",12,"bold"),bg="lightblue")
        studentname_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        studentName_entry = ttk.Entry(class_info_frame,textvariable=self.var_std_name,width=20,font=("times new roman",12,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10,sticky=W)
        
        #class division
        class_div_label = Label(class_info_frame,text="Class Division:",font=("times new roman",12,"bold"),bg="lightblue")
        class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)
        # class_div_entry = ttk.Entry(class_info_frame,textvariable=self.var_div,width=20,font=("times new roman",12,"bold"))
        # class_div_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        division_combo = ttk.Combobox(class_info_frame,textvariable=self.var_div,font=("times new roman",12,"bold"),state="read only",width=17)
        division_combo["values"] = ("Select Division","A","B","C","D")
        division_combo.current(0)
        division_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        
       #Roll No
        roll_no_label = Label(class_info_frame,text="Roll no:",font=("times new roman",12,"bold"),bg="lightblue")
        roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)
        roll_no_entry = ttk.Entry(class_info_frame,textvariable=self.var_roll,width=20,font=("times new roman",12,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)
        
        #Gender
        gender_label = Label(class_info_frame,text="Gender:",font=("times new roman",12,"bold"),bg="lightblue")
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)
        # gender_entry = ttk.Entry(class_info_frame,textvariable=self.var_gender,width=20,font=("times new roman",12,"bold"))
        # gender_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)
        gender_combo = ttk.Combobox(class_info_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),state="read only",width=17)
        gender_combo["values"] = ("Select Gender","Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)
        
        #DOB
        dob_label = Label(class_info_frame,text="Date Of Birth:",font=("times new roman",12,"bold"),bg="lightblue")
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)
        dob_entry = ttk.Entry(class_info_frame,textvariable=self.var_dob,width=20,font=("times new roman",12,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)
        
        #Email
        email_label = Label(class_info_frame,text="Email:",font=("times new roman",12,"bold"),bg="lightblue")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)
        email_entry = ttk.Entry(class_info_frame,textvariable=self.var_email,width=20,font=("times new roman",12,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)
        
        #phone no
        phone_label = Label(class_info_frame,text="Phone No:",font=("times new roman",12,"bold"),bg="lightblue")
        phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)
        phone_entry = ttk.Entry(class_info_frame,textvariable=self.var_phone,width=20,font=("times new roman",12,"bold"))
        phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)
        
        #Address
        address_label = Label(class_info_frame,text="Address:",font=("times new roman",12,"bold"),bg="lightblue")
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)
        address_entry = ttk.Entry(class_info_frame,textvariable=self.var_address,width=20,font=("times new roman",12,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)
        
        #teacher name
        teacher_label = Label(class_info_frame,text="Teacher Name:",font=("times new roman",12,"bold"),bg="lightblue")
        teacher_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)
        teacher_entry = ttk.Entry(class_info_frame,textvariable=self.var_teacher,width=20,font=("times new roman",12,"bold"))
        teacher_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)
        
        #radio buttons
        self.var_radio1 = StringVar()
        radiobtn1 = ttk.Radiobutton(class_info_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=6,column=0)
        
        #self.var_radio2 = StringVar()
        radiobtn2 = ttk.Radiobutton(class_info_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobtn2.grid(row=6,column=1)
        
        #button frame
        btn_frame = Frame(class_info_frame,bd=2,relief=RIDGE,bg="lightblue")
        btn_frame.place(x=0,y=200,width=700,height=40)
        #save button
        save_btn = Button(btn_frame,text="Save",command=self.add_data,width=10,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)
        #update button
        update_btn = Button(btn_frame,text="Update",command=self.update_data,width=10,font=("times new roman",13,"bold"),bg="green",fg="white")
        update_btn.grid(row=0,column=1)
        #delete button
        delete_btn = Button(btn_frame,text="Delete",command=self.delete_data,width=10,font=("times new roman",13,"bold"),bg="orange",fg="white")
        delete_btn.grid(row=0,column=2)
        #reset button
        reset_btn = Button(btn_frame,text="Reset",command=self.reset_data,width=10,font=("times new roman",13,"bold"),bg="red",fg="white")
        reset_btn.grid(row=0,column=4)
        #take photo button
        take_photo_btn = Button(btn_frame,text="Take Photo",command=self.generate_dataset,width=10,font=("times new roman",13,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=5)
        #update photo button
        update_photo_btn = Button(btn_frame,text="Update Photo",width=10,font=("times new roman",10,"bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=0,column=6)
        
        #right_label_frame
        Right_frame = LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"),bg="lightblue",fg="black")
        Right_frame.place(x=660,y=0,width=680,height=500)
        
        #Search Information
        search_info_frame = LabelFrame(Right_frame,bd=2,relief=RIDGE,text="Search System",font=("times new roman",12,"bold"),bg="lightblue",fg="black")
        search_info_frame.place(x=5,y=7,width=650,height=70)
        
        search_label = Label(search_info_frame,text="Search By:",font=("times new roman",12,"bold"),bg="lightblue")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        search_combo = ttk.Combobox(search_info_frame,font=("times new roman",12,"bold"),state="read only",width=12)
        search_combo["values"] = ("Select","Roll No","Phone No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
        search_entry = ttk.Entry(search_info_frame,width=20,font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        
        search_btn = Button(search_info_frame,text="Search",width=7,font=("times new roman",10,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=4)
        
        show_all_btn = Button(search_info_frame,text="Show All",width=7,font=("times new roman",10,"bold"),bg="blue",fg="white")
        show_all_btn.grid(row=0,column=4)
        
        #Table Frame
        table_frame = LabelFrame(Right_frame,bd=2,relief=RIDGE)
        table_frame.place(x=5,y=80,width=650,height=370)
        
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.student_table = ttk.Treeview(table_frame,column=("Dept","Course","Year","Sem","ID","Name","Div","Roll","Gender","DOB","Email","Phone","Address","Teacher","Photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        
        self.student_table.heading("Dept",text="Department")
        self.student_table.heading("Course",text="Course Name")
        self.student_table.heading("Year",text="Year")
        self.student_table.heading("Sem",text="Semester")
        self.student_table.heading("ID",text="Student ID")
        self.student_table.heading("Name",text="Student Name")
        self.student_table.heading("Div",text="Division")
        self.student_table.heading("Roll",text="Roll No")
        self.student_table.heading("Gender",text="Gender")
        self.student_table.heading("DOB",text="Date Of Birth")
        self.student_table.heading("Email",text="Email ID")
        self.student_table.heading("Phone",text="Phone No")
        self.student_table.heading("Address",text="Address")
        self.student_table.heading("Teacher",text="Teacher Name")
        self.student_table.heading("Photo",text="PhotoSampleStatus")
        self.student_table["show"] = "headings"
        
        self.student_table.column("Dept",width=100)
        self.student_table.column("Course",width=100)
        self.student_table.column("Year",width=100)
        self.student_table.column("Sem",width=100)
        self.student_table.column("ID",width=100)
        self.student_table.column("Name",width=100)
        self.student_table.column("Div",width=100)
        self.student_table.column("Roll",width=100)
        self.student_table.column("Gender",width=100)
        self.student_table.column("DOB",width=100)
        self.student_table.column("Email",width=100)
        self.student_table.column("Phone",width=100)
        self.student_table.column("Address",width=100)
        self.student_table.column("Teacher",width=100)
        self.student_table.column("Photo",width=150)
        
        
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        
    #Function Declaration
    
    #add data
    def add_data(self):
        if self.var_dept.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost",username="root",password="123456789",database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",(
                    self.var_dept.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_id.get(),
                    self.var_std_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)
    #fetch data
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="123456789",database="face_recognizer")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()
        
        if len(data) !=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    
    #get cursor
    def get_cursor(self,event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]
        self.var_dept.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])
        
        
    #update function
    def update_data(self):
        if self.var_dept.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if Update>0:
                    conn = mysql.connector.connect(host="localhost",username="root",password="123456789",database="face_recognizer")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set Dept=%s,Course=%s,Year=%s,Semester=%s,Student_Name=%s,Division=%s,Roll=%s,Gender=%s,DOB=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                        
                        
                    self.var_dept.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get(),
                    self.var_std_id.get()
                    ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Student details successfully updated",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()                       
            except Exception as es:
                messagebox.showerror("Error",f"Due To : {str(es)}",parent=self.root)
        
    #delete function
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student ID must be required",parent=self.root)
        else:
            try:
                Delete = messagebox.askyesno("Student Delete Page","Do you want to delete this student",parent=self.root)
                if Delete>0:
                    conn = mysql.connector.connect(host="localhost",username="root",password="123456789",database="face_recognizer")
                    my_cursor = conn.cursor()
                    sql="delete from student where Student_id=%s"
                    value=(self.var_std_id.get(),)
                    my_cursor.execute(sql,value)
                else:
                    if not Delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()       
                messagebox.showinfo("Delete","Successfully Deleted",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To : {str(es)}",parent=self.root)
                
    #reset function
    def reset_data(self):
        self.var_dept.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Select Gender")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")
    
    #generate dataset
    def generate_dataset(self):
        if self.var_dept.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost",username="root",password="123456789",database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set Dept=%s,Course=%s,Year=%s,Semester=%s,Student_Name=%s,Division=%s,Roll=%s,Gender=%s,DOB=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                        
                        
                    self.var_dept.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get(),
                    self.var_std_id.get()==id+1
                    ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                
                #load pre-defined data on face frontals from opencv
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                def face_cropped(img):
                    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor=1.3
                    #minimum neighbor=5
                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                cap = cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face = cv2.resize(face_cropped(my_frame),(450,450))
                        face = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path = "data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)
                    
                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating DataSet Completed")
            except Exception as es:
                messagebox.showerror("Error",f"Due To : {str(es)}",parent=self.root)

if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()