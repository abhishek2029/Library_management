from tkinter import *
from PIL import ImageTk,Image
import pymysql
from tkinter import messagebox
from AddNewBook import *
from DeleteABook import *
from AvailableBooks import *
from IssueABook import *
from ReturnABook import *

# Add your own database name and password here

mypass = ""
mydatabase="db"

con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()

root = Tk()
root.title("Library")
root.minsize(width=1400,height=800)
root.geometry("1400x800")

# Take n>0.25 & n<5
same=True
n=0.50

# Adding a background image
background=Image.open("lib.jpg")
[imageSizeWidth, imageSizeHeight] = background.size 

newImageSizeWidth = int(imageSizeWidth*n)
if same:
    newImageSizeHeight = int(imageSizeHeight*n) 
else:
    newImageSizeHeight = int(imageSizeHeight/n) 
    
background= background.resize((newImageSizeWidth,newImageSizeHeight),Image.ANTIALIAS)
img = ImageTk.PhotoImage(background)

Canvas1 = Canvas(root)

Canvas1.create_image(800,840,image = img)      
Canvas1.config(bg="white",width = newImageSizeWidth, height = newImageSizeHeight)
Canvas1.pack(expand=True,fill=BOTH)

headingFrame1 = Frame(root,bg="white",bd=1)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.4,relheight=0.16)

headingLabel = Label(headingFrame1, text="Welcome to \n Your BookStore", bg='#d4b4b7', fg='black', font=('Times New Roman',20))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

btn1 = Button(root,text="Add a New Book",bg='grey', fg='white', command=addBook)
btn1.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)
    
btn2 = Button(root,text="Delete a Book",bg='grey', fg='white', command=delete)
btn2.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)
    
btn3 = Button(root,text="Check the available books",bg='grey', fg='white', command=View)
btn3.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)
    
btn4 = Button(root,text="Issue Book to Student",bg='grey', fg='white', command = issueBook)
btn4.place(relx=0.28,rely=0.7, relwidth=0.45,relheight=0.1)
    
btn5 = Button(root,text="Return Book",bg='grey', fg='white', command = returnBook)
btn5.place(relx=0.28,rely=0.8, relwidth=0.45,relheight=0.1)

root.mainloop()
