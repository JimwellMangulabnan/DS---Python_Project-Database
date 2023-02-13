#import modules
from tkinter import *
import tkinter.messagebox
import sqlite3

#class for front End UI (user interface)
class Product:

    def __init__(self,root):

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

        RightBodyFrame = LabelFrame(BodyFrame, bd=2, width=300, height=380,
                                   padx=20, pady=10, bg='yellow', relief=RIDGE, font=('arial', 15, 'bold'),
                                   text='Product Item Information: ')
        RightBodyFrame.pack(side=RIGHT)

        ''' Add the Widgets to LeftBodyFrame'''

        self.labelpId=Label(LeftBodyFrame, font=('arial', 15, 'bold'),
                             text="Product Id : ", padx =2, bg='white', fg = 'blue')
        self.labelpId.grid(row=0, column=0, sticky= W)

        self.txtpId = Entry(LeftBodyFrame, font=('arial', 20, 'bold'),
                            textvariable=pId, width=35)
        self.txtpId.grid(row=0, column=1, sticky= W)

        self.labelpName = Label(LeftBodyFrame, font=('arial', 15, 'bold'),
                              text="Product Name : ", padx=2, bg='white', fg='blue')
        self.labelpName.grid(row=1, column=0, sticky=W)

        self.labelpPrice = Label(LeftBodyFrame, font=('arial', 15, 'bold'),
                              text="Product Price : ", padx=2, bg='white', fg='blue')
        self.labelpPrice.grid(row=2, column=0, sticky=W)

        self.labelpQty = Label(LeftBodyFrame, font=('arial', 15, 'bold'),
                              text="Product Quantity : ", padx=2, bg='white', fg='blue')
        self.labelpQty.grid(row=3, column=0, sticky=W)

        self.labelpCompany = Label(LeftBodyFrame, font=('arial', 15, 'bold'),
                              text="Mfg. Company : ", padx=2, bg='white', fg='blue')
        self.labelpCompany.grid(row=4, column=0, sticky=W)

        self.labelpContact = Label(LeftBodyFrame, font=('arial', 15, 'bold'),
                              text="Company Contact", padx=2, bg='white', fg='blue')
        self.labelpContact.grid(row=5, column=0, sticky=W)




if __name__ =='__main__':
    root=Tk()
    application = Product(root)
    root.mainloop()
