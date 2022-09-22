from lib2to3.pgen2.token import EQUAL
from tkinter import *
import serial.tools.list_ports

while True:
    ports = serial.tools.list_ports.comports()
    serialInst = serial.Serial()

    portList = []

    # passing through all the ports that is connected to the computer
    for port in ports:
        portList.append(str(port))
    # automatic Select Arduino if found
    for x in range(0,len(portList)):
        if "Arduino Uno" in portList[x]:
            portvar = portList[x].split(' ', 1)[0]
            print("\nComputer selected")
            print(portList[x])
    
    # check if Computer Select port or not
    try:
        portvar
    except NameError: # If not selected
        print("Computer did not select port\n")
        print("The available Ports are :")
        # passing through all the ports that is connected to the computer then printing them
        for port in portList:
            print(port)
        #input selected port
        val = input("\nselect port: COM")
        #user select one of the existed port then printing the selected one
        for x in range(0,len(portList)):
            if portList[x].startswith("COM" + str(val)):
                portvar = "COM" + str(val)
                print("\nYou selected")
                print(portList[x])
    else:   #If Selected Then initializing serial port
        serialInst.baudrate = 9600
        serialInst.port = portvar
        serialInst.open()
        break

    # insure user Selected the port manually
    try:
        portvar
    except NameError:
        print("You selected non existing Port it Seems")
    else:   #initializing serial port
        serialInst.baudrate = 9600
        serialInst.port = portvar
        serialInst.open()
        break


#Create the main window of the app
WindowFrame = Tk()

#change app Text title
WindowFrame.title("Simple Calculator")

#inserting Ertry widge
Screen = Entry(WindowFrame, width=35, borderwidth=3)
Screen.grid(row=0,column=0,columnspan=3,padx=10,pady=10)


#the founction of the buttons
def button_clicked(parameter):
    current = Screen.get()
    Screen.delete(0,END)
    Screen.insert(0,str(current) + str(parameter))

#Founction of clearing the screen
def button_clear():
    Screen.delete(0,END)

#Function of adding two numbers
def button_add():
    global FirstNumber
    FirstNumber = int(Screen.get())
    global operation
    operation = "add"
    Screen.delete(0,END)

#Function of divide two numbers
def button_div():
    global FirstNumber
    FirstNumber = int(Screen.get())
    global operation
    operation = "div"
    Screen.delete(0,END)

#Function of subtract two numbers
def button_sub():
    global FirstNumber
    FirstNumber = int(Screen.get())
    global operation
    operation = "sub"
    Screen.delete(0,END)

#Function of multiply two numbers
def button_mul():
    global FirstNumber
    FirstNumber = int(Screen.get())
    global operation
    operation = "mul"
    Screen.delete(0,END)

#Function of printing the result
def button_equal():
    if operation == "add":
        theResult = FirstNumber + int(Screen.get())
    elif operation == "sub":
        theResult = FirstNumber - int(Screen.get())
    elif operation == "mul":
        theResult = FirstNumber * int(Screen.get())
    elif operation == "div":
        theResult = FirstNumber / int(Screen.get())
    Screen.delete(0,END)
    Screen.insert(0,theResult)
    serialInst.write(str(theResult).encode())

#inserting buttons
Button_1 = Button(WindowFrame, text="1", padx=30, pady=20, command=lambda: button_clicked(1))
Button_2 = Button(WindowFrame, text="2", padx=30, pady=20, command=lambda: button_clicked(2))
Button_3 = Button(WindowFrame, text="3", padx=30, pady=20, command=lambda: button_clicked(3))
Button_4 = Button(WindowFrame, text="4", padx=30, pady=20, command=lambda: button_clicked(4))
Button_5 = Button(WindowFrame, text="5", padx=30, pady=20, command=lambda: button_clicked(5))
Button_6 = Button(WindowFrame, text="6", padx=30, pady=20, command=lambda: button_clicked(6))
Button_7 = Button(WindowFrame, text="7", padx=30, pady=20, command=lambda: button_clicked(7))
Button_8 = Button(WindowFrame, text="8", padx=30, pady=20, command=lambda: button_clicked(8))
Button_9 = Button(WindowFrame, text="9", padx=30, pady=20, command=lambda: button_clicked(9))
Button_0 = Button(WindowFrame, text="0", padx=30, pady=20, command=lambda: button_clicked(0))
Button_equal = Button(WindowFrame, text="=", padx=30, pady=51, command=button_equal)
Button_clear = Button(WindowFrame, text="C", padx=69, pady=20, command=button_clear)
Button_add = Button(WindowFrame, text="+", padx=29, pady=20, command=button_add)
Button_sub = Button(WindowFrame, text="-", padx=30, pady=20, command=button_sub)
Button_mul = Button(WindowFrame, text="X", padx=30, pady=20, command=button_mul)
Button_div = Button(WindowFrame, text="÷", padx=30, pady=20, command=button_div)

#putting the buttons in the WindowFrame
Button_1.grid(row=3, column=0)
Button_2.grid(row=3, column=1)
Button_3.grid(row=3, column=2)

Button_4.grid(row=2, column=0)
Button_5.grid(row=2, column=1)
Button_6.grid(row=2, column=2)

Button_7.grid(row=1, column=0)
Button_8.grid(row=1, column=1)
Button_9.grid(row=1, column=2)

Button_0.grid(row=4, column=0)
Button_add.grid(row=5, column=0)
Button_sub.grid(row=6, column=0)
Button_mul.grid(row=5, column=1)
Button_div.grid(row=6, column=1)
Button_clear.grid(row=4, column=1,columnspan=2)
Button_equal.grid(row=5, column=2, rowspan=2)

#Run App for Infinty time
WindowFrame.mainloop()