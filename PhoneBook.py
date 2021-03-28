from Tkinter import *
import sqlite3
from tkMessageBox import *
con=sqlite3.Connection('PhoneBook')
cur=con.cursor()
cur.execute("create table if not exists contactbook(CID integer PRIMARY KEY AUTOINCREMENT,Fname varchar2(30),Mname varchar2(30),Lname varchar2(30),Cname varchar2(30),Ad varchar2(50),city varchar2(20),Pc varchar(10),Web varchar(30),dob varchar(20),ptype varchar(20),pno number,etype varchar(20),eid varchar(50))")
roo=Tk()
roo.geometry("650x650")
Label(roo,text="Project Title:PhoneBook",font="times 25 bold").grid(row=1,column=1)
Label(roo,text="Project of Python and Database",font="times 20 bold",fg="blue").grid(row=2,column=1)
Label(roo,text="Developed By:Archit Gupta",font="times 20 bold",fg="red").grid(row=3,column=1)
Label(roo,text="------------------------------------------------").grid(row=4,column=1)
Label(roo,text="make a mouse movement over this screen to close").grid(row=5,column=1)
def screen(x=1):
    roo.destroy()
roo.bind('<Motion>',screen)
roo.mainloop()
root=Tk()
root.geometry('650x650')
img=PhotoImage(file="img.gif")
img=img.subsample(1,1)
Label(root,image=img).grid(row=1,column=1)
Label(root,text="First Name:",font="times 14 bold").grid(row=2,column=0)
a=Entry(root)
a.grid(row=2,column=1)
Label(root,text="Middle Name:",font="times 14 bold").grid(row=3,column=0)
a1=Entry(root)
a1.grid(row=3,column=1)
Label(root,text="Last Name:",font="times 14 bold").grid(row=4,column=0)
a2=Entry(root)
a2.grid(row=4,column=1)
Label(root,text="Company Name:",font="times 14 bold").grid(row=5,column=0)
a3=Entry(root)
a3.grid(row=5,column=1)
Label(root,text="Address:",font="times 14 bold").grid(row=6,column=0)
a4=Entry(root)
a4.grid(row=6,column=1)
Label(root,text="City:",font="times 14 bold").grid(row=7,column=0)
a5=Entry(root)
a5.grid(row=7,column=1)
Label(root,text="Pin Code:",font="times 14 bold").grid(row=8,column=0)
a6=Entry(root)
a6.grid(row=8,column=1)
Label(root,text="Website URL:",font="times 14 bold").grid(row=9,column=0)
a7=Entry(root)
a7.grid(row=9,column=1)
Label(root,text="Date Of Birth:",font="times 14 bold").grid(row=10,column=0)
a8=Entry(root)
a8.grid(row=10,column=1)

Label(root,text="Select Phone Type:",font="times 20 bold",fg="blue").grid(row=11,column=0)
v1=StringVar()
Radiobutton(root,text="Office",variable=v1,value="Office",tristatevalue="x").grid(row=11,column=1)
Radiobutton(root,text="Home",variable=v1,value="Home",tristatevalue="x").grid(row=11,column=2)
Radiobutton(root,text="Mobile",variable=v1,value="Mobile",tristatevalue="x").grid(row=11,column=3)
Label(root,text="Phone Number:",font="times 14 bold").grid(row=12,column=0)
c=Entry(root)
c.grid(row=12,column=1)

Label(root,text="Select Email Id Type:",font="times 20 bold",fg="blue").grid(row=13,column=0)
v2=StringVar()
Radiobutton(root,text="Office",variable=v2,value="Office",tristatevalue="x").grid(row=13,column=1)
Radiobutton(root,text="Personal",variable=v2,value="Personal",tristatevalue="x").grid(row=13,column=2)
Label(root,text="Email Id:",font="times 14 bold").grid(row=14,column=0)
e=Entry(root)
e.grid(row=14,column=1)
v1.set("Mobile")
v2.set("Office")
def save():
    
    if a.get()=='' and a1.get()=='' and a2.get()=='' and a3.get()=='' and a4.get()=='' and a5.get()=='' and a6.get()=='' and a7.get()=='' and a8.get()=='' and c.get()=='' and e.get()=='':
        def show():
            showerror('Error','Enter at least one value')
        show()
    else:
##        cur.execute("insert into contactbook(Fname,Mname,Lname,Cname,Ad,city,Pc,Web,dob) values(?,?,?,?,?,?,?,?,?)",(a.get(),a1.get(),a2.get(),a3.get(),a4.get(),a5.get(),a6.get(),a7.get(),a8.get()))
        if v1.get()=="Office" and v2.get()=="Office":
            cur.execute("insert into contactbook(Fname,Mname,Lname,Cname,Ad,city,Pc,Web,dob,ptype,pno,etype,eid) values(?,?,?,?,?,?,?,?,?,?,?,?,?)",(a.get(),a1.get(),a2.get(),a3.get(),a4.get(),a5.get(),a6.get(),a7.get(),a8.get(),"Office",c.get(),"Office",e.get()))
##        b="Office"
        if v1.get()=="Home" and v2.get()=="Office":
##        b="Home"
            cur.execute("insert into contactbook(Fname,Mname,Lname,Cname,Ad,city,Pc,Web,dob,ptype,pno,etype,eid) values(?,?,?,?,?,?,?,?,?,?,?,?,?)",(a.get(),a1.get(),a2.get(),a3.get(),a4.get(),a5.get(),a6.get(),a7.get(),a8.get(),"Home",c.get(),"Office",e.get()))
        if v1.get()=="Mobile" and v2.get()=="Office":
##        b="Mobile"
            cur.execute("insert into contactbook(Fname,Mname,Lname,Cname,Ad,city,Pc,Web,dob,ptype,pno,etype,eid) values(?,?,?,?,?,?,?,?,?,?,?,?,?)",(a.get(),a1.get(),a2.get(),a3.get(),a4.get(),a5.get(),a6.get(),a7.get(),a8.get(),"Mobile",c.get(),"Office",e.get()))
##    cur.execute("insert into phonebook values(?,?)",(b,c.get()))
        if v1.get()=="Office" and v2.get()=="Personal":
            cur.execute("insert into contactbook(Fname,Mname,Lname,Cname,Ad,city,Pc,Web,dob,ptype,pno,etype,eid) values(?,?,?,?,?,?,?,?,?,?,?,?,?)",(a.get(),a1.get(),a2.get(),a3.get(),a4.get(),a5.get(),a6.get(),a7.get(),a8.get(),"Office",c.get(),"Personal",e.get()))
##        d="Office"
        if v1.get()=="Home" and v2.get()=="Personal":
            cur.execute("insert into contactbook(Fname,Mname,Lname,Cname,Ad,city,Pc,Web,dob,ptype,pno,etype,eid) values(?,?,?,?,?,?,?,?,?,?,?,?,?)",(a.get(),a1.get(),a2.get(),a3.get(),a4.get(),a5.get(),a6.get(),a7.get(),a8.get(),"Home",c.get(),"Personal",e.get()))
        if v1.get()=="Mobile" and v2.get()=="Personal":
            cur.execute("insert into contactbook(Fname,Mname,Lname,Cname,Ad,city,Pc,Web,dob,ptype,pno,etype,eid) values(?,?,?,?,?,?,?,?,?,?,?,?,?)",(a.get(),a1.get(),a2.get(),a3.get(),a4.get(),a5.get(),a6.get(),a7.get(),a8.get(),"Mobile",c.get(),"Personal",e.get()))
##        d="Personal"
        con.commit()
        def show1():
            showinfo('Saved','Contact successfully saved')
        show1()
        a.delete(0,END)
        a1.delete(0,END)
        a2.delete(0,END)
        a3.delete(0,END)
        a4.delete(0,END)
        a5.delete(0,END)
        a6.delete(0,END)
        a7.delete(0,END)
        a8.delete(0,END)
        v1.set("Mobile")
        v2.set("Office")
        c.delete(0,END)
        e.delete(0,END)
##        cur.execute("select * from contactbook")
##        print cur.fetchall()
##        root1.mainloop()
##    print cur.fetchall()



def search():
    root2=Tk()
    root2.geometry('800x800')
    Label(root2,text="Search your Contact here!",font="times 18 bold",bg="blue").grid(row=1,column=1)
    Label(root2,text="Enter the name").grid(row=2,column=0)
    f=Entry(root2)
    f.grid(row=2,column=1)
##    cur.execute("Select * from contactbook")
##    print cur.fetchall()
    def submit(x):
        cur.execute("select Fname"+" from contactbook where Fname Like (?)",('%'+f.get()+'%',))
##        print cur.fetchall()
##        cur.execute("select * from contactbook where Fname=(?)",(g,))
##        cur.execute("Select * from contactbook")
        gh=cur.fetchall()
        lb=Listbox(root2,width="80",height="80")
        lb.grid(row=4,column=1)
##        for i in range(len(gh)):
##            lb.insert(END,gh[i])
        i=0
        j=0
        while(i<len(gh)):
            j=0
            while(j<len(gh[i])):
                lb.insert(END,gh[i][j])
##                fgh=gh[i][1]+gh[i][2]+""+gh[i][3]
##                print fgh
##                j=j+1
##                lb.insert(END,fgh)
                  
                j=j+1
            i=i+1
##        print g
##        print f.get()
##        asa=lb.curselection()
##        print asa
        def listbox(x):
            sa=lb.curselection()
            ss=lb.get(sa)
            cur.execute('select * from contactbook where Fname=(?)',(ss,))
##            print cur.fetchall()
            rec=cur.fetchall()
            root3=Tk()
            root3.geometry("650x650")
            asd=[1]
            asd[0]=[rec[0][0]]
            cur.execute("select * from contactbook where CID = (?)",asd[0])
            aa=cur.fetchall()
            Label(root3,text="FIRST NAME:").grid(row=1,column=0)
            Label(root3,text=rec[0][1]).grid(row=1,column=1)
            Label(root3,text="MIDDLE NAME:").grid(row=2,column=0)
            Label(root3,text=rec[0][2]).grid(row=2,column=1)
            Label(root3,text="LAST NAME:").grid(row=3,column=0)
            Label(root3,text=rec[0][3]).grid(row=3,column=1)
            Label(root3,text="COMPANY NAME:").grid(row=4,column=0)
            Label(root3,text=rec[0][4]).grid(row=4,column=1)
            Label(root3,text="ADDRESS:").grid(row=5,column=0)
            Label(root3,text=rec[0][5]).grid(row=5,column=1)
            Label(root3,text="CITY:").grid(row=6,column=0)
            Label(root3,text=rec[0][6]).grid(row=6,column=1)
            Label(root3,text="PIN CODE:").grid(row=7,column=0)
            Label(root3,text=rec[0][7]).grid(row=7,column=1)
            Label(root3,text="WEBSITE URL:").grid(row=8,column=0)
            Label(root3,text=rec[0][8]).grid(row=8,column=1)
            Label(root3,text="DATE OF BIRTH:").grid(row=9,column=0)
            Label(root3,text=rec[0][9]).grid(row=9,column=1)
            Label(root3,text="PHONE TYPE:").grid(row=10,column=0)
            Label(root3,text=rec[0][10]).grid(row=10,column=1)
            Label(root3,text="PHONE NUMBER:").grid(row=11,column=0)
            Label(root3,text=rec[0][11]).grid(row=11,column=1)
            Label(root3,text="EMAIL ID TYPE:").grid(row=12,column=0)
            Label(root3,text=rec[0][12]).grid(row=12,column=1)
            Label(root3,text="EMAIL ID:").grid(row=13,column=0)
            Label(root3,text=rec[0][13]).grid(row=13,column=1)
            def close1(x=1):
                root3.destroy()
            Button(root3,text="Close",command=close1).grid(row=15,column=1)
            root3.mainloop()
        lb.bind('<<ListboxSelect>>',listbox)
        def delete():
            sa=lb.curselection()
            ss=lb.get(sa)
            cur.execute("select * from contactbook where Fname=(?)",(ss,))
            sd=cur.fetchall()
            cur.execute('delete from contactbook where Fname=(?) and CID=(?)',(sd[0][1],sd[0][0]))
            lb.delete(sa)
            con.commit()
            def show2():
                showinfo('Delete','Contact successfully deleted')
        Button(root2,text="Delete",command=delete).grid(row=2,column=2)
        
    root2.bind('<Key>',submit)
    root2.mainloop()
##    Button(root2,text="Submit",command=submit).grid(row=3,column=1)
##    a="Jaypee"


def edit():
    root4=Tk()
    root4.geometry('800x800')
    Label(root4,text="Search your Contact here for edit!",font="times 18 bold",bg="blue").grid(row=1,column=1)
##    Label(root2,text="Enter the name").grid(row=2,column=0)
    f=Entry(root4)
    f.grid(row=4,column=1)
####    cur.execute("Select * from contactbook")
####    print cur.fetchall()
    def submit(x):
        cur.execute("select Fname"+" from contactbook where Fname Like (?)",('%'+f.get()+'%',))
####        print cur.fetchall()
####        cur.execute("select * from contactbook where Fname=(?)",(g,))
####        cur.execute("Select * from contactbook")
        gh=cur.fetchall()
        lb=Listbox(root4,width="80",height="80")
        lb.grid(row=5,column=1)        
####        tg=map(str, Listbox.curselection())
####        print tg
        i=0
        j=0
        while(i<len(gh)):
            j=0
            while(j<len(gh[i])):
                lb.insert(END,gh[i][j])
####                fgh=gh[i][1]+gh[i][2]+""+gh[i][3]
####                print fgh
##                j=j+1
##                lb.insert(END,fgh)
##                  
                j=j+1
            i=i+1
####        print g
####        print f.get()
####        asa=lb.curselection()
####        print asa
        def listbox(x):
            sa=lb.curselection()
            ss=lb.get(sa)
            cur.execute('select * from contactbook where Fname=(?)',(ss,))
####            print cur.fetchall()
            rec=cur.fetchall()
##            print rec
            root6=Tk()
            root6.geometry("650x650")
            Label(root6,text="FIRST NAME:").grid(row=1,column=0)
            Label(root6,text=rec[0][1]).grid(row=1,column=1)
            fn=Entry(root6)
            fn.grid(row=1,column=2)
            Label(root6,text="MIDDLE NAME:").grid(row=2,column=0)
            Label(root6,text=rec[0][2]).grid(row=2,column=1)
            mn=Entry(root6)
            mn.grid(row=2,column=2)
            Label(root6,text="LAST NAME:").grid(row=3,column=0)
            Label(root6,text=rec[0][3]).grid(row=3,column=1)
            ln=Entry(root6)
            ln.grid(row=3,column=2)
            Label(root6,text="COMPANY NAME:").grid(row=4,column=0)
            Label(root6,text=rec[0][4]).grid(row=4,column=1)
            cn=Entry(root6)
            cn.grid(row=4,column=2)
            Label(root6,text="ADDRESS:").grid(row=5,column=0)
            Label(root6,text=rec[0][5]).grid(row=5,column=1)
            add=Entry(root6)
            add.grid(row=5,column=2)
            Label(root6,text="CITY:").grid(row=6,column=0)
            Label(root6,text=rec[0][6]).grid(row=6,column=1)
            ci=Entry(root6)
            ci.grid(row=6,column=2)
            Label(root6,text="PIN CODE:").grid(row=7,column=0)
            Label(root6,text=rec[0][7]).grid(row=7,column=1)
            pc=Entry(root6)
            pc.grid(row=7,column=2)
            Label(root6,text="WEBSITE URL:").grid(row=8,column=0)
            Label(root6,text=rec[0][8]).grid(row=8,column=1)
            wu=Entry(root6)
            wu.grid(row=8,column=2)
            Label(root6,text="DATE OF BIRTH:").grid(row=9,column=0)
            Label(root6,text=rec[0][9]).grid(row=9,column=1)
            dob=Entry(root6)
            dob.grid(row=9,column=2)
            Label(root6,text="PHONE TYPE:").grid(row=10,column=0)
            Label(root6,text=rec[0][10]).grid(row=10,column=1)
            pt=Entry(root6)
            pt.grid(row=10,column=2)
            Label(root6,text="PHONE NUMBER:").grid(row=11,column=0)
            Label(root6,text=rec[0][11]).grid(row=11,column=1)
            pn=Entry(root6)
            pn.grid(row=11,column=2)
            Label(root6,text="EMAIL ID TYPE:").grid(row=12,column=0)
            Label(root6,text=rec[0][12]).grid(row=12,column=1)
            et=Entry(root6)
            et.grid(row=12,column=2)
            Label(root6,text="EMAIL ID:").grid(row=13,column=0)
            Label(root6,text=rec[0][13]).grid(row=13,column=1)
            ei=Entry(root6)
            ei.grid(row=13,column=2)
            def edit1():
                if fn.get()!='':
                    cur.execute("update contactbook set Fname=(?) where CID=(?)",(fn.get(),rec[0][0]))
                if mn.get()!='':
                    cur.execute("update contactbook set Mname=(?) where CID=(?)",(mn.get(),rec[0][0]))
                if ln.get()!='':
                    cur.execute("update contactbook set Lname=(?) where CID=(?)",(ln.get(),rec[0][0]))
                if cn.get()!='':
                    cur.execute("update contactbook set Cname=(?) where CID=(?)",(cn.get(),rec[0][0]))
                if add.get()!='':
                    cur.execute("update contactbook set Ad=(?) where CID=(?)",(add.get(),rec[0][0]))
                if ci.get()!='':
                    cur.execute("update contactbook set city=(?) where CID=(?)",(ci.get(),rec[0][0]))
                if pc.get()!='':
                    cur.execute("update contactbook set Pc=(?) where CID=(?)",(pc.get(),rec[0][0]))
                if wu.get()!='':
                    cur.execute("update contactbook set Web=(?) where CID=(?)",(wu.get(),rec[0][0]))
                if dob.get()!='':
                    cur.execute("update contactbook set dob=(?) where CID=(?)",(dob.get(),rec[0][0]))
                if pt.get()!='':
                    cur.execute("update contactbook set ptype=(?) where CID=(?)",(pt.get(),rec[0][0]))
                if pn.get()!='':
                    cur.execute("update contactbook set pno=(?) where CID=(?)",(pn.get(),rec[0][0]))
                if et.get()!='':
                    cur.execute("update contactbook set etype=(?) where CID=(?)",(et.get(),rec[0][0]))
                if ei.get()!='':
                    cur.execute("update contactbook set eid=(?) where CID=(?)",(ei.get(),rec[0][0]))
                con.commit()
                def show3():
                    showinfo('Saved','Contact updated successfully')
                show3()
                fn.delete(0,END)
                mn.delete(0,END)
                ln.delete(0,END)
                cn.delete(0,END)
                add.delete(0,END)
                ci.delete(0,END)
                pc.delete(0,END)
                wu.delete(0,END)
                dob.delete(0,END)
                pt.delete(0,END)
                pn.delete(0,END)
                et.delete(0,END)
                ei.delete(0,END)
                
            def close3():
                root6.destroy()
            Button(root6,text="Edit",command=edit1).grid(row=15,column=1)
            Button(root6,text="Close",command=close3).grid(row=15,column=2)
            root6.mainloop()
        lb.bind('<<ListboxSelect>>',listbox)
    root4.bind('<Key>',submit)
    root4.mainloop()
    
    
Button(root,text='Save',command=save).grid(row=15,column=0)
Button(root,text='Search',command=search).grid(row=15,column=1)
Button(root,text='Edit',command=edit).grid(row=15,column=2)
Button(root,text='Close',command=root.destroy).grid(row=15,column=3)

root.mainloop()
