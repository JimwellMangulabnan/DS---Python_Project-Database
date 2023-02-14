#import modules
from tkinter import *
import tkinter.messagebox
import sqlite3

#class for front End UI (user interface)
class Product:

    def __init__(self,root):

        p = Database()
        p.conn()

        self.root = root
        self.root.title("WAREHOUSE INVENTORY SALES PURCHASE MANAGEMENT SYSTEM")
        self.root.geometry("1325x690")
        self.root.config(bg="yellow")

        pId = StringVar()
        pName = StringVar()
        pPrice = StringVar()
        pQty = StringVar()
        pCompany = StringVar()
        pContact = StringVar()

        ''' Let's call the Database methods to perform database operations '''

        # function to close the frame
        def close():
            print("Product : close method called ")
            close = tkinter.messagebox.askyesno("WAREHOUSE INVENTORY SALES PURCHASE MANAGEMENT \
                                                SYSTEM ", "Really .... Do you want to close the system")
            if close > 0:
                root.destroy()
                print("Product : close method finished\n")
                return

        #function for clear / reset the widget
        def clear():
            print("Product : clear method called ")
            self.txtpId.delete(0, END)
            self.txtpName.delete(0, END)
            self.txtpPrice.delete(0, END)
            self.txtpQty.delete(0, END)
            self.txtpCompany.delete(0, END)
            self.txtpContact.delete(0, END)
            print("Product : clear method finished\n ")

        # function to save the product details in Database table
        def insert():
            print("Product : insert method called ")
            if (len(pId.get()) != 0):
                p.insert(pId.get(), pName.get(), pQty.get(), pPrice.get(),
                         pCompany.get(), pContact.get())
                productList.delete(0, END)
                productList.insert(END,pId.get(), pName.get(), pQty.get(), pPrice.get(),
                         pCompany.get(), pContact.get())

                showInProductList() #called showInProductList method
                #after inserting the data record to database table

            else:
                tkinter.messagebox.askyesno("WAREHOUSE INVENTORY SALES PURCHASE MANAGEMENT \
                                    SYSTEM ", "Really .... Enter Product id")
            print("Product : insert method finished\n ")

        #function responsible to show product table data to scroll product list
        def showInProductList():
            print("Product : showInProductList method called ")
            productList.delete(0, END)
            for row in p.show():
                productList.insert(END, row, str(""))
            print("Product : showInProductList method finished\n ")

        # add to scroll bar
        def productRec(event): # function to be called from scrollbar productList
            print("Product : productRec method called ")
            global pd

            searchPd = productList.curselection()[0]
            pd = productList.get(searchPd)

            self.txtpId.delete(0,END)
            self.txtpId.insert(END,pd[0])

            self.txtpName.delete(0, END)
            self.txtpName.insert(END, pd[1])

            self.txtpPrice.delete(0, END)
            self.txtpPrice.insert(END, pd[2])

            self.txtpQty.delete(0, END)
            self.txtpQty.insert(END, pd[3])

            self.txtpCompany.delete(0, END)
            self.txtpCompany.insert(END, pd[4])

            self.txtpContact.delete(0, END)
            self.txtpContact.insert(END, pd[5])

            print("Product : productRec method finished\n ")


        ''' Create the frame'''
        MainFrame = Frame(self.root,bg="red")
        MainFrame.grid()

        HeadFrame =Frame(MainFrame, bd=1, padx=50, pady=10,
                         bg='white',relief=RIDGE)
        HeadFrame.pack(side=TOP)

        self.ITitle = Label(HeadFrame, font=('arial', 50, 'bold'), fg='red',
                            text='Warehouse Inventory Sales Purchase ', bg='white')
        self.ITitle.grid()

        OperationFrame = Frame(MainFrame, bd=2, width=1300, height=60,
                               padx=50, pady=20,bg='white', relief=RIDGE)
        OperationFrame.pack(side=BOTTOM)

        BodyFrame = Frame(MainFrame, bd=2, width=1290, height=400,
                               padx=30, pady=20, bg='white', relief=RIDGE)
        BodyFrame.pack(side=BOTTOM)

        LeftBodyFrame = LabelFrame(BodyFrame, bd=2, width=600, height=380,
                          padx=20, pady=10, bg='yellow', relief=RIDGE, font=('arial', 15, 'bold'),
                              text= 'Product Item Details: ')
        LeftBodyFrame.pack(side=LEFT)

        RightBodyFrame = LabelFrame(BodyFrame, bd=2, width=400, height=380,
                                   padx=20, pady=10, bg='yellow', relief=RIDGE, font=('arial', 15, 'bold'),
                                   text='Product Item Information: ')
        RightBodyFrame.pack(side=RIGHT)

        ''' Add the Widgets to LeftBodyFrame'''

        self.labelpId=Label(LeftBodyFrame, font=('arial', 15, 'bold'),
                             text="Product Id : ", padx =2, pady=2, bg='white', fg = 'blue')
        self.labelpId.grid(row=0, column=0, sticky= W)

        self.txtpId = Entry(LeftBodyFrame, font=('arial', 20, 'bold'),
                            textvariable=pId, width=35)
        self.txtpId.grid(row=0, column=1, sticky= W)

        self.labelpName = Label(LeftBodyFrame, font=('arial', 15, 'bold'),
                              text="Product Name : ", padx=2, pady=2, bg='white', fg='blue')
        self.labelpName.grid(row=1, column=0, sticky=W)

        self.txtpName = Entry(LeftBodyFrame, font=('arial', 20, 'bold'),
                            textvariable=pName, width=35)
        self.txtpName.grid(row=1, column=1, sticky=W)

        self.labelpPrice = Label(LeftBodyFrame, font=('arial', 15, 'bold'),
                              text="Product Price : ", padx=2, pady=2, bg='white', fg='blue')
        self.labelpPrice.grid(row=2, column=0, sticky=W)

        self.txtpPrice = Entry(LeftBodyFrame, font=('arial', 20, 'bold'),
                            textvariable=pPrice, width=35)
        self.txtpPrice.grid(row=2, column=1, sticky=W)

        self.labelpQty = Label(LeftBodyFrame, font=('arial', 15, 'bold'),
                              text="Product Quantity : ", padx=2, pady=2, bg='white', fg='blue')
        self.labelpQty.grid(row=3, column=0, sticky=W)

        self.txtpQty = Entry(LeftBodyFrame, font=('arial', 20, 'bold'),
                            textvariable=pQty, width=35)
        self.txtpQty.grid(row=3, column=1, sticky=W)

        self.labelpCompany = Label(LeftBodyFrame, font=('arial', 15, 'bold'),
                              text="Mfg. Company : ", padx=2, pady=2, bg='white', fg='blue')
        self.labelpCompany.grid(row=4, column=0, sticky=W)

        self.txtpCompany = Entry(LeftBodyFrame, font=('arial', 20, 'bold'),
                            textvariable=pCompany, width=35)
        self.txtpCompany.grid(row=4, column=1, sticky=W)

        self.labelpContact = Label(LeftBodyFrame, font=('arial', 15, 'bold'),
                              text="Company Contact", padx=2, pady=2, bg='white', fg='blue')
        self.labelpContact.grid(row=5, column=0, sticky=W)

        self.txtpContact = Entry(LeftBodyFrame, font=('arial', 20, 'bold'),
                            textvariable=pContact, width=35)
        self.txtpContact.grid(row=5, column=1, sticky=W)

        self.labelpC1 = Label(LeftBodyFrame, padx=2, pady=2)
        self.labelpC1.grid(row=6, column=0, sticky=W)

        self.labelpC2 = Label(LeftBodyFrame, padx=2, pady=2)
        self.labelpC2.grid(row=7, column=0, sticky=W)

        self.labelpC3 = Label(LeftBodyFrame, padx=2, pady=2)
        self.labelpC3.grid(row=8, column=0, sticky=W)

        self.labelpC4 = Label(LeftBodyFrame, padx=2, pady=2)
        self.labelpC4.grid(row=9, column=0, sticky=W)

        ''' Add Scroll Bar'''
        scroll = Scrollbar(RightBodyFrame)
        scroll.grid(row= 0, column= 1, sticky='ns')
        productList = Listbox(RightBodyFrame, width=40, height=16, font=('arial', 12, 'bold'),
                yscrollcommand = scroll.set)


        productList.grid(row=0, column= 0, padx= 8)
        scroll.config(command=productList.yview)

        ''' Add the buttons to operation Frame'''
        self.buttonSaveData = Button(OperationFrame, text = 'Save',
                                 font= ('arial', 18, 'bold'), height =1, width = '10', bd =4, command =insert)
        self.buttonSaveData.grid(row = 0, column =0)

        self.buttonShowData = Button(OperationFrame, text='Show Data',
                                 font=('arial', 18, 'bold'), height=1, width='10', bd=4, command=showInProductList)
        self.buttonShowData.grid(row=0, column=1)

        self.buttonClear = Button(OperationFrame, text='Reset',
                                 font=('arial', 18, 'bold'), height=1, width='10', bd=4, command=clear)
        self.buttonClear.grid(row=0, column=2)

        self.buttonDelete = Button(OperationFrame, text='Delete',
                                 font=('arial', 18, 'bold'), height=1, width='10', bd=4)
        self.buttonDelete.grid(row=0, column=3)

        self.buttonSearch = Button(OperationFrame, text='Search',
                                 font=('arial', 18, 'bold'), height=1, width='10', bd=4)
        self.buttonSearch.grid(row=0, column=4)

        self.buttonUpdate = Button(OperationFrame, text='Update',
                                 font=('arial', 18, 'bold'), height=1, width='10', bd=4)
        self.buttonUpdate.grid(row=0, column=5)

        self.buttonClose = Button(OperationFrame, text='Close',
                                 font=('arial', 18, 'bold'), height=1, width='10', bd=4, command =close)
        self.buttonClose.grid(row=0, column=6)


#Back End Database operations
class Database:
    def conn(self):
        print("Database : connection method called")
        con = sqlite3.connect("inventory.db")
        cur = con.cursor()
        query = "create table if not exist product(pid integer primary key,\
        pname text, price text, qty text, company text, contact text)"
        cur.execute(query)
        con.commit()
        con.close()
        print("Database : connection method finished\n")

    def insert(self, pid, name, price, qty, company, contact):
        print("Database : insert method called")
        con = sqlite3.connect("inventory.db")
        cur = con.cursor()
        query = "insert into product values(?,?,?,?,?,?)"
        cur.execute(query, (pid, name, price, qty, company, contact))
        con.commit()
        con.close()
        print("Database : insert method finished\n")

    def show(self):
        print("Database : show method called")
        con = sqlite3.connect("inventory.db")
        cur = con.cursor()
        query = "select * from product"
        cur.execute(query)
        rows = cur.fetchall()
        con.close()
        print("Database : show method finished\n")
        return rows

    def delete(self, pid):
        print("Database : delete method called", pid)
        con = sqlite3.connect("inventory.db")
        cur = con.cursor()
        cur.execute("delete from product where pid=?", (pid,))
        con.commit()
        con.close()
        print(pid,"Database : delete method finished\n")

    def search(self, pid="",name="", price="", qty="", company="", contact=""):
        print("Database : search method called", pid)
        con = sqlite3.connect("inventory.db")
        cur = con.cursor()
        cur.execute("select * from product where pid=? or pname=? or \
                    price=? or qty=? or company=? or contact=?")
        row = cur.fetchall()
        con.close()
        print(pid, "Database : select method finished\n")
        return row

    def update(self, pid="",name="", price="", qty="", company="", contact=""):
        print("Database : update method called", pid)
        con = sqlite3.connect("inventory.db")
        cur = con.cursor()
        cur.execute("update product set pid=? or pname=? or \
                    price=? or qty=? or company=? or contact=? where pid =?",
                    (pid, name, price, qty, company, contact, pid))
        con.commit()
        con.close()
        print(pid, "Database : update method finished\n")

if __name__ =='__main__':
    root=Tk()
    application = Product(root)
    root.mainloop()


