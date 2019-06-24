#Front_End

from tkinter import*
import tkinter.messagebox

import stdDatabase as DB


class Student:
    def __init__(self,root):
        self.root = root
        self.root.title("Student Database Management System")
        self.root.geometry("1000x600+0+0")
        self.root.config(bg="cadet blue")

        StdID = StringVar()
        FirstName = StringVar()
        SurName = StringVar()
        DoB = StringVar()
        Age = StringVar() 
        Gender = StringVar()
        Address = StringVar()
        Mobile = StringVar()

        #===================================================Functions========================================================

        def iExit():
            iExit = tkinter.messagebox.askyesno("Student Database Management System","Confirm if you want to exit")
            if iExit > 0:
                root.destroy()
                return()
        def clearData():
            self.txtStdID.delete(0,END)
            self.txtFirstName.delete(0,END)
            self.txtSurName.delete(0,END)
            self.txtDoB.delete(0,END)
            self.txtAge.delete(0,END)
            self.txtGender.delete(0,END)
            self.txtAddress.delete(0,END)
            self.txtMobile.delete(0,END)
        def addData():
            if(len(StdID.get())!=0):
                DB.addStdRec(StdID.get(), FirstName.get(), SurName.get(), DoB.get(), Age.get(), Gender.get(), Address.get(), Mobile.get())
                studentlist.delete(0,END)
                studentlist.insert(END,(StdID.get(), FirstName.get(), SurName.get(), DoB.get(), Age.get(), Gender.get(), Address.get(), Mobile.get()))
                tkinter.messagebox.showinfo("Student Database Management System", "Student Record Added")
            else:
                tkinter.messagebox.showinfo("Student Database Management System", "Please fill all the fields")
                

        def DisplayData():
            studentlist.delete(0,END)
            for row in DB.viewData():
                for k,v in row.items():
                    studentlist.insert(END,str(k)+str(" : ")+str(v),str("\n"))
                studentlist.insert(END,str("----------------------------------------------------------------"))

        def DeleteData():
            if(len(StdID.get())!=0):
                DB.deleteRec(StdID.get())
                tkinter.messagebox.showinfo("Student Database Management System", "Student Record Deleted")
                clearData()
                DisplayData()
            else:
                tkinter.messagebox.showinfo("Student Database Management System", "Cannot Delete Record. Please fill all the fields")
        def SearchData():
            if(len(StdID.get())!=0):
                studentlist.delete(0,END)
                
                for row in DB.searchData(StdID.get()):
                    for k,v in row.items():
                        studentlist.insert(END,str(k)+str(" : ")+str(v),str("\n"))
            else:
                tkinter.messagebox.showinfo("Student Database Management System", "Record not found.")

        def UpdateData():
            if(len(StdID.get())!=0):
                iUpdate = tkinter.messagebox.askyesno("Student Database Management System","Confirm if you want to Update?")
                if(iUpdate!=0):
                    DB.dataUpdate(StdID.get(), FirstName.get(), SurName.get(), DoB.get(),Age.get(),Gender.get(),Address.get(),Mobile.get())
                    SearchData()
                
            else:
                tkinter.messagebox.showinfo("Student Database Management System", "Record not found.")
            
                
                    
            
                
                
                
            



        #===================================================Frames========================================================
        MainFrame = Frame(self.root, bg="cadet blue")
        MainFrame.grid()

        TitFrame = Frame(MainFrame, bd=2, padx=54, pady=8, bg="Ghost White", relief=RIDGE)
        TitFrame.pack(side=TOP)

        self.lblTit = Label(TitFrame, font=('arial',47,'bold'),text="Student DBMS  |  IMPR2611",bg="Ghost White")
        self.lblTit.grid()

        ButtonFrame = Frame(MainFrame, bd=2, width=800, height=50, padx=18, pady=10, relief=RIDGE, bg="Ghost White")
        ButtonFrame.pack(side=BOTTOM)

        DataFrame = Frame(MainFrame, bd=1, width=600, height=250, padx=20, pady=20, relief=RIDGE, bg="cadet blue")
        DataFrame.pack(side=BOTTOM)

        DataFrameLEFT = LabelFrame(DataFrame, bd=1, width=400, height=400, padx=20, relief=RIDGE, bg="ghost white", font=('arial',16,'bold'),text="Student Info\n")
        DataFrameLEFT.pack(side=LEFT)

        DataFrameRIGHT = LabelFrame(DataFrame, bd=1, width=300, height=150, padx=31,pady=3, relief=RIDGE, bg="ghost white",font=('arial',16,'bold'),text="Student Details\n")
        DataFrameRIGHT.pack(side=RIGHT)

        #===================================================Right Widget========================================================


        self.lblStdID = Label(DataFrameLEFT, font=('arial',14,'bold'),text="Student ID:",bg="Ghost White",padx=2,pady=2)
        self.lblStdID.grid(row=0, column=0, sticky=W)
        self.txtStdID = Entry(DataFrameLEFT, font=('arial',14,'bold'),textvariable=StdID,width=30)
        self.txtStdID.grid(row=0, column=1)

        self.lblFirstName = Label(DataFrameLEFT, font=('arial',14,'bold'),text="First Name:",bg="Ghost White",padx=2,pady=2)
        self.lblFirstName.grid(row=1, column=0, sticky=W)
        self.txtFirstName = Entry(DataFrameLEFT, font=('arial',14,'bold'),textvariable=FirstName,width=30)
        self.txtFirstName.grid(row=1, column=1)

        self.lblSurName = Label(DataFrameLEFT, font=('arial',14,'bold'),text="Last Name:",bg="Ghost White",padx=2,pady=2)
        self.lblSurName.grid(row=2, column=0, sticky=W)
        self.txtSurName = Entry(DataFrameLEFT, font=('arial',14,'bold'),textvariable=SurName,width=30)
        self.txtSurName.grid(row=2, column=1)

        self.lblDoB = Label(DataFrameLEFT, font=('arial',14,'bold'),text="DoB:",bg="Ghost White",padx=2,pady=2)
        self.lblDoB.grid(row=3, column=0, sticky=W)
        self.txtDoB = Entry(DataFrameLEFT, font=('arial',14,'bold'),textvariable=DoB,width=30)
        self.txtDoB.grid(row=3, column=1)

        self.lblAge = Label(DataFrameLEFT, font=('arial',14,'bold'),text="Age:",bg="Ghost White",padx=2,pady=2)
        self.lblAge.grid(row=4, column=0, sticky=W)
        self.txtAge = Entry(DataFrameLEFT, font=('arial',14,'bold'),textvariable=Age,width=30)
        self.txtAge.grid(row=4, column=1)

        self.lblGender = Label(DataFrameLEFT, font=('arial',14,'bold'),text="Gender:",bg="Ghost White",padx=2,pady=2)
        self.lblGender.grid(row=5, column=0, sticky=W)
        self.txtGender = Entry(DataFrameLEFT, font=('arial',14,'bold'),textvariable=Gender,width=30)
        self.txtGender.grid(row=5, column=1)

        self.lblAddress = Label(DataFrameLEFT, font=('arial',14,'bold'),text="Address:",bg="Ghost White",padx=2,pady=2)
        self.lblAddress.grid(row=6, column=0, sticky=W)
        self.txtAddress = Entry(DataFrameLEFT, font=('arial',14,'bold'),textvariable=Address,width=30)
        self.txtAddress.grid(row=6, column=1)

        self.lblMobile = Label(DataFrameLEFT, font=('arial',14,'bold'),text="Mobile:",bg="Ghost White",padx=2,pady=2)
        self.lblMobile.grid(row=7, column=0, sticky=W)
        self.txtMobile = Entry(DataFrameLEFT, font=('arial',14,'bold'),textvariable=Mobile,width=30)
        self.txtMobile.grid(row=7, column=1)

        #===================================================Left Widget========================================================

        scrollbar = Scrollbar(DataFrameRIGHT)
        scrollbar.grid(row=0,column=1, sticky='ns')

        studentlist = Listbox(DataFrameRIGHT, width=41, height=16, font=('arial',12,'bold'),yscrollcommand=scrollbar.set)
        studentlist.grid(row=0,column=0, padx=8)

        scrollbar.config(command = studentlist.yview)



        #===================================================Button Widget========================================================

        self.btnAddData = Button(ButtonFrame, text="Add New", font=('arial',14,'bold'),height=1,width=10,bd=4,command=addData)
        self.btnAddData.grid(row=0,column=0)

        self.btnDisplayDate = Button(ButtonFrame, text="Display", font=('arial',14,'bold'),height=1,width=10,bd=4,command=DisplayData)
        self.btnDisplayDate.grid(row=0,column=1)

        self.btnClearData = Button(ButtonFrame, text="Clear", font=('arial',14,'bold'),height=1,width=10,bd=4,command=clearData)
        self.btnClearData.grid(row=0,column=2)

        self.btnDeleteData = Button(ButtonFrame, text="Delete", font=('arial',14,'bold'),height=1,width=10,bd=4,command=DeleteData)
        self.btnDeleteData.grid(row=0,column=3)

        self.btnSearchData = Button(ButtonFrame, text="Search", font=('arial',14,'bold'),height=1,width=10,bd=4,command=SearchData)
        self.btnSearchData.grid(row=0,column=4)

        self.btnUpdateData = Button(ButtonFrame, text="Update", font=('arial',14,'bold'),height=1,width=10,bd=4,command=UpdateData)
        self.btnUpdateData.grid(row=0,column=5)

        self.btnExit = Button(ButtonFrame, text="Exit", font=('arial',14,'bold'),height=1,width=10,bd=4, command=iExit)
        self.btnExit.grid(row=0,column=6)
        

        
def main():
    root = Tk()
    application = Student(root)
    root.mainloop()
