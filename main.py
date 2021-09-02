
from tkinter import *
weather_key = '4681e9fc94f46077b5d88b8286613e55'
import requests
import tkinter as tk
import tkinter.messagebox as mb
import smtplib
import mysql.connector
from PIL import ImageTk,Image

## connecting to the database using 'connect()' method
## it takes 3 required parameters 'host', 'user', 'password'
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="tanoj4294")
# creating database_cursor to perform SQL operation
db_cursor = db_connection.cursor(
    buffered=True)


# Using Toplevel widget to create a new window named Register Successful Window
class Login_Success_Window(tk.Toplevel):
    def __init__(self,parent):
        super().__init__()

        self.original_frame = parent
        self.geometry("1000x1300")
        self.title("Registration Successful")



        canvas = tk.Canvas(self, height=1000, width=1000)
        load = Image.open("cloud.jpg")
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)

        canvas.pack()

        frame = tk.Frame(self, bg="#F2E0F7", bd=10)
        frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.1, anchor='n')
        instructionFrame = tk.Frame(self, bg="#F2E0F7", bd=20)
        instructionFrame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.15, anchor='n')
        resultsFrame = tk.Frame(self, bg="#F2E0F7", bd=20)
        resultsFrame.place(relx=0.5, rely=0.35, relwidth=0.75, relheight=0.50, anchor='n')

        def convert_celcius(temp):
            celcius = round((temp - 32) * 5 / 9, 2)
            return (celcius)

        def format_response(weather):
            try:
                name = weather['name']
                country = weather['sys']['country']
                desc = weather['weather'][0]['description']
                temp = weather['main']['temp']
                celcius = convert_celcius(temp)
                feels = weather['main']['feels_like']
                feelsC = convert_celcius(feels)
                humidity = weather['main']['humidity']
                wind = weather['wind']['speed']


                final_str = '%s, %s \nConditions: %s \nTemperature: %s°F | %s°C\n Feels Like: %s°F | %s °C\n Humidity: %s\n Wind Speed: %sm/h' % (
                    name, country, desc, temp, celcius, feels, feelsC, humidity, wind)


            except:
                final_str = 'Please Enter Valid City Name!'

            return final_str


        def get_weather(city):

            url = 'https://api.openweathermap.org/data/2.5/weather'
            params = {'APPID': weather_key, 'q': city, 'units': 'imperial'}
            response = requests.get(url, params=params)
            weather = response.json()
            print(weather)
            format_response(weather)

            label['text'] = format_response(weather)

        bgColor = "white"



        instructionLabel = tk.Label(instructionFrame, bg=bgColor, font=24,
                                    text="Please enter your city or zip code and the \n2 letter country code to get the current weather!")
        instructionLabel.place(relwidth=1, relheight=1)



        input = tk.Entry(frame, bg=bgColor, font=40)
        input.place(relx=.025, relwidth=0.65, relheight=1)

        button = tk.Button(frame, text="Search", activebackground='#CBEEB6', font=24,
                           command=lambda: get_weather(input.get()))
        button.place(relx=0.7, relheight=1, relwidth=0.3)



        label = tk.Label(resultsFrame, bg=bgColor, font=1000)
        label.place(relwidth=0.700, relheight=0.700)
        # create OK button
        self.btn_register = tk.Button(self, text="exit", font=("Helvetica", 11), bg="white", fg="black",
                                      command=self.delete_login_success)

        self.btn_register.place(relx=0.8, rely=0.8, height=35, width=40)
        self.btn_calender = tk.Button(self, text="Calender", font=("Helvetica", 11), bg="Red",
                                      fg="Blue",
                                      command=self.show_calender)

        self.btn_calender.place(relx=0.6, rely=0.8, height=21, width=70)
    def delete_login_success(self):
        mb.showinfo('Information', "click ok to exit " )
        self.destroy()
        self.original_frame.show()






# Using Toplevel widget to create a new window named RegisterWindow to register a new user
class RegisterWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.original_frame = parent
        self.geometry("1000x1300")
        self.title("Register")

        load = Image.open("lightning.jpg")
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)
        self.lblRegister = tk.Label(self, text="Register", font=("Helvetica", 20,"bold"), bg="#0B0B3B", fg="white")
        self.lblFName = tk.Label(self, text="Enter FirstName:", font=("Helvetica", 15), bg="#0B0B3B", fg="white")
        self.lblLName = tk.Label(self, text="Enter LastName:", font=("Helvetica", 15), bg="#0B0B3B", fg="white")
        self.lblLName = tk.Label(self, text="Enter LastName:", font=("Helvetica", 15), bg="#0B0B3B", fg="white")
        self.lblUId = tk.Label(self, text="Enter Emailid:", font=("Helvetica", 15), bg="#0B0B3B", fg="white")
        self.lblPwd = tk.Label(self, text="Enter Password:", font=("Helvetica", 15), bg="#0B0B3B", fg="white")
        self.lblContactNo = tk.Label(self, text="Enter Contact No:", font=("Helvetica", 15), bg="#0B0B3B", fg="white")
        self.lblCity = tk.Label(self, text="Enter City:", font=("Helvetica", 15), bg="#0B0B3B", fg="white")
        self.lblState = tk.Label(self, text="Enter State:", font=("Helvetica", 15), bg="#0B0B3B", fg="white")

        self.txtFName = tk.Entry(self)
        self.txtLName = tk.Entry(self)
        self.txtUId = tk.Entry(self)
        self.txtPwd = tk.Entry(self)
        self.txtContact = tk.Entry(self)
        self.txtCity = tk.Entry(self)
        self.txtState = tk.Entry(self)

        self.btn_register = tk.Button(self, text="Register", font=("Helvetica", 15,"bold"), bg="#0B0B3B", fg="white",
                                      command=self.register)
        self.btn_cancel = tk.Button(self, text="Back", font=("Helvetica", 15,"bold"), bg="#0B0B3B", fg="white",
                                    command=self.onClose)

        self.lblRegister.place(relx=0.467, rely=0.111, height=35, width=130)
        self.lblFName.place(relx=0.318, rely=0.2, height=21, width=150)
        self.lblLName.place(relx=0.319, rely=0.267, height=21, width=150)
        self.lblUId.place(relx=0.310, rely=0.333, height=21, width=150)
        self.lblPwd.place(relx=0.319, rely=0.4, height=21, width=150)
        self.lblContactNo.place(relx=0.310, rely=0.467, height=21, width=155)
        self.lblCity.place(relx=0.320, rely=0.533, height=21, width=150)
        self.lblState.place(relx=0.320, rely=0.6, height=21, width=150)
        self.txtFName.place(relx=0.490, rely=0.2, height=20, relwidth=0.223)
        self.txtLName.place(relx=0.490, rely=0.267, height=20, relwidth=0.223)
        self.txtUId.place(relx=0.490, rely=0.333, height=20, relwidth=0.223)
        self.txtPwd.place(relx=0.490, rely=0.4, height=20, relwidth=0.223)
        self.txtContact.place(relx=0.490, rely=0.467, height=20, relwidth=0.223)
        self.txtCity.place(relx=0.490, rely=0.533, height=20, relwidth=0.223)
        self.txtState.place(relx=0.490, rely=0.6, height=20, relwidth=0.223)
        self.btn_register.place(relx=0.500, rely=0.660, height=35, width=95)
        self.btn_cancel.place(relx=0.605, rely=0.660, height=35, width=95)

    def register(self):

        if db_connection.is_connected() == False:
            db_connection.connect()
        # executing cursor with execute method and pass SQL query
        db_cursor.execute("CREATE DATABASE IF NOT EXISTS User")  # Create a Database
        db_cursor.execute("use User")
        # creating required tables
        db_cursor.execute(
            "Create table if not exists USER(uid VARCHAR(30) NOT NULL  PRIMARY KEY,password VARCHAR(30),fname VARCHAR(30),lname VARCHAR(30),city VARCHAR(20),state VARCHAR(30),mobileno VARCHAR(10))")

        db_connection.commit()

        fname = self.txtFName.get()  # Retrieving entered first name
        lname = self.txtLName.get()  # Retrieving entered last name
        uid = self.txtUId.get()  # Retrieving entered user id
        pwd = self.txtPwd.get()  # Retrieving entered password
        contact_no = self.txtContact.get()  # Retrieving entered contact number
        city = self.txtCity.get()  # Retrieving entered city name
        state = self.txtState.get()  # Retrieving entered state name

        if fname == "":
            mb.showinfo('Information', "Please Enter Firstname")
            self.txtFName.focus_set()
            return
        if lname == "":
            mb.showinfo('Information', "Please Enter Lastname")
            self.txtLName.focus_set()
            return
        if uid == "":
            mb.showinfo('Information', "Please Enter User Id")
            self.txtUId.focus_set()
            return
        if pwd == "":
            mb.showinfo('Information', "Please Enter Password")
            self.txtPwd.focus_set()
            return

        if contact_no == "":
            mb.showinfo('Information', "Please Enter Contact Number")
            self.txtContact.focus_set()
            return
        if city == "":
            mb.showinfo('Information', "Please Enter City Name")
            self.txtCity.focus_set()
            return
        if state == "":
            mb.showinfo('Information', "Please Enter State Name")
            self.txtState.focus_set()
            return
        # Inserting record into database
        db_cursor.execute("use User")
        query = "INSERT INTO User(uid,password,fname,lname,city,state,mobileno) VALUES ('%s','%s','%s','%s','%s','%s','%s')" % (
        uid, pwd, fname, lname, city, state, contact_no)

        try:
            # implement sql Sentence
            db_cursor.execute(query)
            mb.showinfo('Information', "Data inserted Successfully")
            # Submit to database for execution
            db_connection.commit()
        except:
            mb.showinfo('Information', "Data insertion failed!!!")
            # Rollback in case there is any error
            db_connection.rollback()
            # Close database connection
            db_connection.close()

    def onClose(self):
        """"""
        self.destroy()
        self.original_frame.show()


class LoginApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Login")
        self.geometry("1000x1300")


        load = Image.open("background.png")
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)
        self.configure(bg="grey")
        self.lblHeading = tk.Label(self, text="Login", font=("Helvetica", 20,"bold"), bg="#4C0B5F", fg="white")
        self.lbluname = tk.Label(self, text="UserName:", font=("Helvetica", 13,"bold"), bg="#4C0B5F", fg="white")
        self.lblpsswd = tk.Label(self, text="Password:", font=("Helvetica", 13,"bold"), bg="#4C0B5F", fg="#FFFFFF" )
        self.txtuname = tk.Entry(self, width=90)
        self.txtpasswd = tk.Entry(self, width=90, show="*")
        self.btn_login = tk.Button(self, text="Login", font=("Helvetica", 15), bg="#4C0B5F", fg="white",
                                   command=self.login)
        self.btn_clear = tk.Button(self, text="Clear", font=("Helvetica", 15), bg="#4C0B5F", fg="white",
                                   command=self.clear_form)
        self.btn_register = tk.Button(self, text="NewUser!Register", font=("Helvetica", 15), bg="#4C0B5F", fg="white",
                                      command=self.open_registration_window)
        self.btn_exit = tk.Button(self, text="Exit", font=("Helvetica", 20,"bold"), bg="white", fg="#4C0B5F", command=self.exit)

        self.lblHeading.place(relx=0.41, rely=0.089, height=41, width=174)
        self.lbluname.place(relx=0.235, rely=0.289, height=47, width=132)
        self.lblpsswd.place(relx=0.242, rely=0.378, height=49, width=129)
        self.txtuname.place(relx=0.417, rely=0.289, height=22, relwidth=0.273)
        self.txtpasswd.place(relx=0.417, rely=0.388, height=20, relwidth=0.273)
        self.btn_login.place(relx=0.45, rely=0.489, height=30, width=60)
        self.btn_clear.place(relx=0.54, rely=0.489, height=30, width=80)
        self.btn_register.place(relx=0.695, rely=0.489, height=30, width=180)
        self.btn_exit.place(relx=0.75, rely=0.880, height=30, width=68)

    def open_registration_window(self):
        self.withdraw()
        window = RegisterWindow(self)
        window.grab_set()

    def open_login_success_window(self):
        self.withdraw()
        window = Login_Success_Window(self)
        window.grab_set()

    def show(self):
        """"""
        self.update()
        self.deiconify()

    def login(self):
        if db_connection.is_connected() == False:
            db_connection.connect()
        # executing cursor with execute method and pass SQL query
        db_cursor.execute("CREATE DATABASE IF NOT EXISTS User")  # Create a Database
        db_cursor.execute("use User")  # Interact with Database
        # creating required tables
        db_cursor.execute(
            "create table if not exists USER(uid VARCHAR(30) NOT NULL  PRIMARY KEY,password VARCHAR(30),fname VARCHAR(30),lname VARCHAR(30),city VARCHAR(20),state VARCHAR(30),mobileno VARCHAR(10))")
        db_connection.commit()
        username = str(self.txtuname.get())  # Retrieving entered username


        sender_email = "weatherapplication404@gmail.com"
        receiver_email = username

        password ="Weather@123"
        message = "HEY, YOU HAVE SUCCESFULLY REGISTERED FOR WEATHER APPLICATION "

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        print("login succesful")
        server.sendmail(sender_email, receiver_email, message)
        print("email has been send to", receiver_email)
        try:

            username = str(self.txtuname.get())  # Retrieving entered username
            passwd = str(self.txtpasswd.get())  # Retrieving entered password
            if username == "":
                mb.showinfo('Information', "Please Enter Username")
                self.txtuname.focus_set()
                return
            if passwd == "":
                mb.showinfo('Information', "Please Enter Password")
                self.txtpasswd.focus_set()
                return

            print(username)
            print(passwd)
            query = "SELECT * FROM User WHERE uid = '" + username + "' AND password = '" + passwd + "'"
            print(query)
            # implement sql Sentence
            db_cursor.execute(query)
            rowcount = db_cursor.rowcount
            print(rowcount)
            if db_cursor.rowcount == 1:
                mb.showinfo('Information', "Login Successfully")
                self.open_login_success_window()
            else:
                mb.showinfo('Information', "Login failed,Invalid Username or Password.Try again!!!")
        except:
            # Closing Connection
            db_connection.disconnect()

    def clear_form(self):
        self.txtuname.delete(0, tk.END)
        self.txtpasswd.delete(0, tk.END)
        self.txtuname.focus_set()

    def exit(self):
        MsgBox = mb.askquestion('Exit Application', 'Are you sure you want to exit the application',
                                icon='warning')
        if MsgBox == 'yes':
            self.destroy()


if __name__ == "__main__":
    app = LoginApp()
    app.mainloop()