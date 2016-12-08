from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from tkinter import *


class LoginFrame(Frame):
    def __init__(self, master):
        super().__init__(master)

        root.title("Please enter your Username and Password")
        root.geometry("350x100")
        root.attributes("-topmost", True)                   # Puts the GUI Window above all other Windows
        self.label_1 = Label(self, text="Username")
        self.label_2 = Label(self, text="Password")

        self.entry_1 = Entry(self)
        self.entry_2 = Entry(self, show="*")

        self.label_1.grid(row=0, sticky=E)
        self.label_2.grid(row=1, sticky=E)
        self.entry_1.grid(row=0, column=1)
        self.entry_2.grid(row=1, column=1)


        self.logbtn = Button(self, text="Login", command = self._login_btn_clickked)
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
        lf.search("CAS", "MA", "225", "B1") # Calls the search function


    def search(self, College, Dept, Course, Section):

        select = Select(self.driver.find_element_by_name("College"))    # Finds the drop down box
        select.select_by_visible_text(College)  # selects a certain college
        self.driver.find_element_by_name("Dept").send_keys(Dept)    # Enters department into the department textbox
        self.driver.find_element_by_name("Course").send_keys(Course)    # Enters course into the course textbox
        self.driver.find_element_by_name("Section").send_keys(Section)  # Enters the section into the section textbox
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
            print("Unfortunately there was an error")

        if seats > 0:   # Compares the seat number to see if its greater than 0 or not
            print("Good news the class is open!")
        else:
            print("Unfortunately that class is full")

        self.driver.quit()  # Quits the browser
        quit()  # Quites the program


root = Tk()
lf = LoginFrame(root)
root.mainloop()

