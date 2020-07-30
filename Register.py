from tkinter import *
import sqlite3



def myfunc():
    

    

    root1 = Tk()

    root1.title('Register')

    root1.configure(width = 1500, height = 800)

    canvas = Canvas(root1,width=1500, height=800, bg='sky blue')

    canvas.place(x=0,y=0)


    #database
    
    '''
    #create database to connect one

    conn = sqlite3.connect('regi.db')
    #create cursor
    c = conn.cursor()
    #create table
    c.execute("""CREATE TABLE details(

        Employee_name text,
        Employee_id int,
        Contact int,
        DOJ text,
        Department text,
        Password text
        )""")
        

    conn.commit()
    c.close()
    '''
    

    def update():

        conn = sqlite3.connect('regi.db')

        c = conn.cursor()

        #record_id = e_del.get()

        
    #query to update 
        c.execute("""update details set
            Employee_name = :first,
            Employee_id = :id,
            Contact = :contact,
            DOJ = :doj,
            Department = :dept

            where oid = :oid""",
                  
            {
             'first': e2_editor.get(),
             'id' : e3_editor.get(),
             'contact':e4_editor.get(),
             'doj' : e5_editor.get(),
             'dept' : e6_editor.get(),
             'oid': e_del.get()

            })      


        conn.commit()

        conn.close()
        
    #closes the editor window after updation
        editor.destroy()

        


    def edit():
        global editor   #making it global so that we can use it on other function
        
        editor = Tk()

        editor.title('update a record')

        editor.configure(width = 1500, height = 800)

        canvas = Canvas(editor,width=1500, height=800, bg='sky blue')

        canvas.place(x=0,y=0)


        conn = sqlite3.connect('regi.db')
        
        c = conn.cursor()

        record_id = e_del.get()
        c.execute("select * from details where oid = " + record_id)
        records = c.fetchall()
            


        #commit changes
        conn.commit()
        #close connection
        conn.close()


    #CREATE TEXT BOX LABELS    

        lbl1 = Label(editor, text = 'Update details', font = 'Times 22', bg = 'yellow', fg = 'blue')
        lbl1.place(x=400,y=100)

        lbl2 = Label(editor, text = 'Enter Employee Name:', font = 'Times 15')
        lbl2.place(x=300,y=200)

        lbl3 = Label(editor, text = 'Enter Employee Id:', font = 'Times 15')
        lbl3.place(x=300,y=275)

        lbl4 = Label(editor, text = 'Mobile No:', font = 'Times 15')
        lbl4.place(x=300,y=350)

        lbl5 = Label(editor, text = 'Date Of Joining:', font = 'Times 15')
        lbl5.place(x=300,y=425)

        lbl6 = Label(editor, text = 'Department:', font = 'Times 15')
        lbl6.place(x=300,y=500)

    #CREATE GLOBAL VARIABLE FOR TEXT BOX NAME

        global e2_editor
        global e3_editor
        global e4_editor
        global e5_editor
        global e6_editor



    #CREATE TEXT BOXES

        e2_editor = Entry(editor)
        e2_editor.place(x=500, y=200)

        e3_editor = Entry(editor)
        e3_editor.place(x=500, y=275)

        e4_editor = Entry(editor)
        e4_editor.place(x=500, y=350)

        e5_editor = Entry(editor)
        e5_editor.place(x=500, y=425)

        e6_editor = Entry(editor)
        e6_editor.place(x=500, y=500)


        for record in records:

            e2_editor.insert(0,record[0])
            e3_editor.insert(0,record[1])
            e4_editor.insert(0,record[2])
            e5_editor.insert(0,record[3])
            e6_editor.insert(0,record[4])

    #CREATE A BUTTON TO SAVE EDITED TEXT
            
        save_btn = Button(editor, text = 'Save Record', command = update, font = 'Times 14',bg = 'red')
        save_btn.place(x=425, y=575) 
        

    #create function to delete a record

    def delete():

        #create database to connect one
        conn = sqlite3.connect('regi.db')
        #create cursor
        c = conn.cursor()

        #delete a record

        c.execute("delete from details where oid = " + e_del.get())
        
        #clear the text boxes
        e_del.delete(0, END)



        #commit changes
        conn.commit()
        #close connection
        conn.close()


        
    #create submit function for data base

    def submit():

        
        

       #create database to connect one
        conn = sqlite3.connect('regi.db')
        #create cursor
        c = conn.cursor()
        
        #insert into table
        c.execute("INSERT INTO details VALUES(:e2,:e3,:e4,:e5,:e6,:Password)",

                  {
                      'e2':e2.get(),
                      'e3':e3.get(),
                      'e4':e4.get(),
                      'e5':e5.get(),
                      'e6':e6.get(),
                      'Password': e_pass.get()
                   })

           


        #commit changes
        conn.commit()
        #close connection
        conn.close()


        
        

        #clear the text boxes
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
        e5.delete(0,END)
        e6.delete(0,END)
        e_pass.delete(0,END)
        
        lbl_reg = Label(root1, text = 'details registered sucessfully', font = 'Times 18', fg = 'red')
        lbl_reg.place(x=300 , y=625)    

    def query():

        #create database to connect one
        conn = sqlite3.connect('regi.db')
        #create cursor
        c = conn.cursor()

        #QUERY THE DATA BASE
        c.execute('select *,oid from details')
        
        records = c.fetchall()
        print(records)

        #loop through result
        
        print_records = ''
        
        for record in records:
            print_records += str(record[0]) +'\t' + str(record[6])+' '+'\n'
            
        lblx = Label(root1, text = print_records, font = 'Times 15',fg = 'red')
        lblx.place(x=900,y=100)
        
        #commit changes
        conn.commit()
        #close connection
        conn.close()
        
        


    #creating 6 labels

    lbl1 = Label(root1, text = 'REGISTER', relief ='solid',font = 'Times 22', bg = 'yellow', fg = 'blue')
    lbl1.place(x=400,y=100)

    lbl2 = Label(root1, text = 'Enter Employee Name:', font = 'Times 15')
    lbl2.place(x=300,y=200)

    lbl3 = Label(root1, text = 'Enter Employee Id:', font = 'Times 15')
    lbl3.place(x=300,y=275)

    lbl4 = Label(root1, text = 'Mobile No:', font = 'Times 15')
    lbl4.place(x=300,y=350)

    lbl5 = Label(root1, text = 'Date Of Joining:', font = 'Times 15')
    lbl5.place(x=300,y=425)

    lbl6 = Label(root1, text = 'Department:', font = 'Times 15')
    lbl6.place(x=300,y=500)

    lbl_del = Label(root1, text = 'Select Id :', font = 'Times 15')
    lbl_del.place(x=850,y=425)

    lbl_pass = Label(root1, text = 'Password:', font = 'Times 15')
    lbl_pass.place(x=850,y=625)
     

    # creating entry boxes

    e2 = Entry(root1)
    e2.place(x=500, y=200)

    e3 = Entry(root1)
    e3.place(x=500, y=275)

    e4 = Entry(root1)
    e4.place(x=500, y=350)

    e5 = Entry(root1)
    e5.place(x=500, y=425)

    e6 = Entry(root1)
    e6.place(x=500, y=500)
    print(e6,"????????")

    e_del = Entry(root1)
    e_del.place(x=1000, y=425)

    e_pass = Entry(root1)
    print(e_pass,">>>>>>>>>>>>")
    e_pass.place(x=1000, y=625)



    # creating buttons


    btn3 = Button(root1, text = 'Submit', command = submit, font = 'Times 14',bg = 'red')
    btn3.place(x=425, y=575)

    #create query button

    btn4 = Button(root1, text = 'show records', command = query, font = 'Times 14',bg = 'red')
    btn4.place(x=1000, y=350)

    #create delete button

    btn_del = Button(root1, text = 'Delete record', command = delete, font = 'Times 14',bg = 'red')
    btn_del.place(x=1000, y=480, width=120)

    #create update button
    edit_btn = Button(root1, text = 'edit record', command = edit, font = 'Times 14',bg = 'red')
    edit_btn.place(x=1000, y=575, width=120)


    root1.mainloop()
    return
    
    

