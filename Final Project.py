from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from tkinter import *



class LoginFrame(Frame):
    def __init__(self, master):
        super().__init__(master)

        root.title("Please enter your Username and Password")       # Makes the title of the frame
        root.geometry("400x200")            # Makes the size of the frame
        root.attributes("-topmost", True)  # Puts the GUI Window above all other Windows
        self.label_1 = Label(self, text="Username")
        self.label_2 = Label(self, text="Password")         # Names your label
        self.label_3 = Label(self, text="College")          #
        self.label_4 = Label(self, text="Dept")
        self.label_5 = Label(self, text="Course")
        self.label_6 = Label(self, text="Section")

        self.entry_1 = Entry(self)
        self.entry_2 = Entry(self, show="*")
        self.entry_3 = Entry(self)
        self.entry_4 = Entry(self)
        self.entry_5 = Entry(self)
        self.entry_6 = Entry(self)

        self.label_1.grid(row=0, sticky=E)
        self.label_2.grid(row=1, sticky=E)
        self.label_3.grid(row=2, sticky=E)
        self.label_4.grid(row=3, sticky=E)
        self.label_5.grid(row=4, sticky=E)
        self.label_6.grid(row=5, sticky=E)
        self.entry_1.grid(row=0, column=1)
        self.entry_2.grid(row=1, column=1)
        self.entry_3.grid(row=2, column=1)
        self.entry_4.grid(row=3, column=1)
        self.entry_5.grid(row=4, column=1)
        self.entry_6.grid(row=5, column=1)

        self.logbtn = Button(self, text="Login", command=self._login_btn_clickked)
        self.logbtn.grid(columnspan=2)

        self.pack()



    def _login_btn_clickked(self):

        username = self.entry_1.get()
        password = self.entry_2.get()

        self.driver = webdriver.Chrome()                                # This depends on your browser, and whether
                                                                        # or not you have the web driver installed

        self.driver.get("https://www.bu.edu/link/bin/uiscgi_studentlink.pl/1480436841?ModuleName=menu.pl&NewMenu=Academics")    # Opens the academics studentlink in chrome

        continue_link = self.driver.find_element_by_partial_link_text('Registration').click()   # clicks registration
        find_username = self.driver.find_element_by_id("username")  # Finds username textbox in html
        find_username.send_keys(username)   # Enters your username in the textbox
        find_password = self.driver.find_element_by_id("password")  # Finds the password textbox
        find_password.send_keys(password)   # Enters the password into the textbox
        find_password.send_keys(Keys.ENTER) # Simulates hitting enter
        self.driver.get("https://www.bu.edu/link/bin/uiscgi_studentlink.pl/1481040756?ModuleName=reg/option/_start.pl&ViewSem=Spring%202017&KeySem=20174")  # Opens next or current semester registration
        Plan_link = self.driver.find_element_by_partial_link_text("Plan").click()   # Clicks the planner
        Add_link = self.driver.find_element_by_partial_link_text("Add").click() # Clicks add class to planner
        lf.search() # Calls the search function


    def search(self):
        college = self.entry_3.get().upper()
        dept = self.entry_4.get()
        course = self.entry_5.get()
        section = self.entry_6.get()

        select = Select(self.driver.find_element_by_name("College"))    # Finds the drop down box
        select.select_by_visible_text(college)  # selects a certain college
        self.driver.find_element_by_name("Dept").send_keys(dept)    # Enters department into the department textbox
        self.driver.find_element_by_name("Course").send_keys(course)    # Enters course into the course textbox
        self.driver.find_element_by_name("Section").send_keys(section)  # Enters the section into the section textbox
        button = self.driver.find_element_by_xpath("//input[@type='button']")   # Finds the go button
        button.click()  # Clicks the go button

        try:
            if int(self.driver.find_element_by_xpath("/html/body/form/table/tbody/tr[2]/td[6]").text) > -1: #  Checks the possible html formats to find the one that returns an integer and converts the number into an int
                seats = int(self.driver.find_element_by_xpath("/html/body/form/table/tbody/tr[2]/td[6]").text)
        except ValueError:
            if int(self.driver.find_element_by_xpath("/html/body/form/table/tbody/tr[3]/td[6]").text) > -1:
                seats = int(self.driver.find_element_by_xpath("/html/body/form/table/tbody/tr[3]/td[6]").text)
        except ValueError:
            if int(self.driver.find_element_by_xpath("/html/body/form/table/tbody/tr[4]/td[6]").text) > -1:
                seats = int(self.driver.find_element_by_xpath("/html/body/form/table/tbody/tr[4]/td[6]").text)
        except ValueError:
            print("Unfortunately there was an error, please try again")

        if seats > 0:   # Compares the seat number to see if its greater than 0 or not
            print("Good news the class is open!")
        elif seats == 0:
            print("Unfortunately that class is full")

        self.driver.quit()  # Quits the browser
        quit()  # Quits the program


root = Tk()
lf = LoginFrame(root)
root.mainloop()

