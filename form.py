from tkinter import *
def getvals():
  pass
  print(uservalue.get())
  print(passvalue.get())
root=Tk()

#start enter value tab
root.geometry("644x900")

user=Label(root, text="username")
password=Label(root, text="Password")
user.grid()
password.grid(row=1)
uservalue=StringVar()
passvalue=StringVar()

userentry=Entry(root, textvariable = uservalue)
passentry=Entry(root, textvariable = passvalue)

Button(text="Submit", command=getvals).grid()

root.mainloop()


