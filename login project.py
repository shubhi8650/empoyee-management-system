
from tkinter import *
from Register import myfunc

import sqlite3
def log_out():

        
    #from Register import *

    root = Tk()
    root.title('login_page')

    root.configure(width = 1500,height = 800)
    
    canvas = Canvas(root,width=1500, height=800, bg='sky blue')

    canvas.place(x=0,y=0)



    #creating 4 label
    lbl1 = Label(root, text = 'EMPLOYEE MANAGEMENT SYSTEM', relief ='solid', font = 'Times 22', bg = 'yellow', fg = 'blue')
    lbl1.place(x=425,y=100)

    lbl2 = Label(root, text = 'Enter employee id:', font = 'Times 15')
    lbl2.place(x=500,y=200)

    lbl3 = Label(root, text = 'Enter Password:', font = 'Times 15')
    lbl3.place(x=500,y=275)

    lbl3 = Label(root, text = 'Are you a new Employee?', font = 'Times 15')
    lbl3.place(x=550,y=400)

    #creating 2 entry box:

    e2 = Entry(root)
    e2.place(x=700, y=275)

    e3 = Entry(root)
    e3.place(x=700, y=200)

    # creating 2 button

    def Register():

        pass

    btn3 = Button(root, text = 'Register', command = myfunc, font = 'Times 14',bg = 'red')
    btn3.place(x=780, y=400)

    def Login():
        #create database to connect one
            conn = sqlite3.connect('regi.db')
            #create cursor
            c = conn.cursor()
            
            c.execute("select Password from details where Employee_id = "+ e3.get())
            records = c.fetchone()
            #rec = ''.join(records)  also we can opt this methord to concert tuple into strings
            print(str(records[0]))
            print(e2.get())
            

            if (e2.get() == str(records[0])):

                def new_page():

                    voot = Tk()

                    voot.title('login_page')

                    voot.configure(width = 1500,height = 800)

                    canvas = Canvas(voot,width=1500, height=800, bg='sky blue')

                    canvas.place(x=0,y=0)

                    lbl1 = Label(voot, text = 'YOU ARE SUCESSFULLY LOGGED IN', relief ='solid', font = 'Times 32', bg = 'yellow', fg = 'black')
                    lbl1.place(x=380,y=100)

                   

                    # creating a logout button    

                    btn_logout = Button(voot, text = 'log out', command = log_out, font = 'Times 14',bg = 'grey', width = 20)
                    btn_logout.place(x=500, y=400)

                    voot.mainloop()
                    
                new_page()   

            else:

                print('not match')

             


            #commit changes
            conn.commit()
            #close connection
            conn.close()

    btn4 = Button(root, text = 'Login', command = Login, font = 'Times 14',bg = 'grey')
    btn4.place(x=625, y=335)

    root.mainloop()
log_out()
