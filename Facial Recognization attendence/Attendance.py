from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata = []
class attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1357x790+0+0")
        self.root.title("Face Recognition System")
        
        #variables
        self.var_attend_id = StringVar()
        self.var_attend_roll = StringVar()
        self.var_attend_name = StringVar()
        self.var_attend_dep = StringVar()
        self.var_attend_time = StringVar()
        self.var_attend_date = StringVar()
        self.var_attend_attendance = StringVar()
        
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
        title_lbl=Label(bg_img, text="ATTENDANCE", font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1400,height=45)
        
        main_frame = Frame(bg_img,bd=2,bg="lightblue")
        main_frame.place(x=0,y=50,width=1357,height=650)
        
        #left_label_frame
        Left_frame = LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Attendance Details",font=("times new roman",12,"bold"),bg="lightblue",fg="black")
        Left_frame.place(x=0,y=0,width=650,height=500)
        
        
        left_inside_frame = LabelFrame(Left_frame,bd=2,relief=RIDGE,bg="lightblue")
        left_inside_frame.place(x=0,y=0,width=630,height=400)
        
        #labels and entries
        #attendance ID
        attendance_label = Label(left_inside_frame,text="Attendance ID:",font=("times new roman",12,"bold"),bg="lightblue")
        attendance_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        attendance_entry = ttk.Entry(left_inside_frame,width=20,textvariable=self.var_attend_id,font=("times new roman",12,"bold"))
        attendance_entry.grid(row=0,column=1,padx=10,sticky=W)
        
        #roll
        roll_label = Label(left_inside_frame,text="Roll:",font=("comicsansns",12,"bold"),bg="lightblue")
        roll_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        roll_entry = ttk.Entry(left_inside_frame,width=20,textvariable=self.var_attend_roll,font=("times new roman",12,"bold"))
        roll_entry.grid(row=0,column=3,padx=10,sticky=W)
        
        #name
        name_label = Label(left_inside_frame,text="Name:",font=("times new roman",12,"bold"),bg="lightblue")
        name_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)
        name_entry = ttk.Entry(left_inside_frame,width=20,textvariable=self.var_attend_name,font=("times new roman",12,"bold"))
        name_entry.grid(row=1,column=1,padx=10,sticky=W)
        
        #department
        department_label = Label(left_inside_frame,text="Department:",font=("times new roman",12,"bold"),bg="lightblue")
        department_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)
        department_entry = ttk.Entry(left_inside_frame,width=20,textvariable=self.var_attend_dep,font=("times new roman",12,"bold"))
        department_entry.grid(row=1,column=3,padx=10,sticky=W)
        
        #time
        time_label = Label(left_inside_frame,text="Time:",font=("times new roman",12,"bold"),bg="lightblue")
        time_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)
        time_entry = ttk.Entry(left_inside_frame,width=20,textvariable=self.var_attend_time,font=("times new roman",12,"bold"))
        time_entry.grid(row=2,column=1,padx=10,sticky=W)
        
        #date
        date_label = Label(left_inside_frame,text="Date:",font=("times new roman",12,"bold"),bg="lightblue")
        date_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)
        date_entry = ttk.Entry(left_inside_frame,width=20,textvariable=self.var_attend_date,font=("times new roman",12,"bold"))
        date_entry.grid(row=2,column=3,padx=10,sticky=W)
        
        #attendance
        attendanceLabel = Label(left_inside_frame,text="Attendance Status:",font=("times new roman",12,"bold"),bg="lightblue")
        attendanceLabel.grid(row=3,column=0)
        self.atten_status=ttk.Combobox(left_inside_frame,width=20,textvariable=self.var_attend_attendance,font="comicsansns 11 bold",state="readonly")
        self.atten_status["values"] = ("Status","Present","Absent")
        self.atten_status.grid(row=3,column=1,pady=8)
        self.atten_status.current(0)
        
        #button frame
        btn_frame = Frame(left_inside_frame,bd=2,relief=RIDGE,bg="lightblue")
        btn_frame.place(x=0,y=250,width=700,height=40)
        #import csv button
        import_csv_btn = Button(btn_frame,text="Import CSV",command=self.importCSV,width=13,font=("times new roman",13,"bold"),bg="blue",fg="white")
        import_csv_btn.grid(row=0,column=0)
        #export csv button
        export_csv_btn = Button(btn_frame,text="Export CSV",command=self.exportCSV,width=13,font=("times new roman",13,"bold"),bg="blue",fg="white")
        export_csv_btn.grid(row=0,column=1)
        #update button
        update_btn = Button(btn_frame,text="Update",width=13,font=("times new roman",13,"bold"),bg="green",fg="white")
        update_btn.grid(row=0,column=2)
        #reset button
        reset_btn = Button(btn_frame,text="Reset",command=self.reset_data,width=13,font=("times new roman",13,"bold"),bg="red",fg="white")
        reset_btn.grid(row=0,column=4)
        
        #right_label_frame
        Right_frame = LabelFrame(main_frame,bd=2,relief=RIDGE,text="Attendance Details",font=("times new roman",12,"bold"),bg="lightblue",fg="black")
        Right_frame.place(x=660,y=0,width=680,height=500)
        
        table_frame = Frame(Right_frame,bd=2,relief=RIDGE,bg="lightblue")
        table_frame.place(x=0,y=0,width=680,height=480)
        
        #scroll bar and tables
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.AttendanceReportTable = ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)
        
        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")
        
        self.AttendanceReportTable["show"]="headings"
        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)
        
        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)
        
    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)
    
    def importCSV(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread = csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)
            
    def exportCSV(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("Error","No Data Found",parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile, delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Data Exported Successfully")
        except Exception as es:
            messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
    
    def get_cursor(self,event=""):
        cursor_row = self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item(cursor_row)
        rows = content['values']
        self.var_attend_id.set(rows[0])
        self.var_attend_roll.set(rows[1])
        self.var_attend_name.set(rows[2])
        self.var_attend_dep.set(rows[3])
        self.var_attend_time.set(rows[4])
        self.var_attend_date.set(rows[5])
        self.var_attend_attendance.set(rows[6])
        
    def reset_data(self):
        self.var_attend_id.set("")
        self.var_attend_roll.set("")
        self.var_attend_name.set("")
        self.var_attend_dep.set("")
        self.var_attend_time.set("")
        self.var_attend_date.set("")
        self.var_attend_attendance.set("")
        
if __name__ == "__main__":
    root = Tk()
    obj = attendance(root)
    root.mainloop()