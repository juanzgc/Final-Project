from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from tkinter import *
import tkinter.messagebox as tm


class LoginFrame(Frame):
    def __init__(self, master):
        super().__init__(master)

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

        self.driver = webdriver.Chrome()
        self.driver.get("https://www.bu.edu/link/bin/uiscgi_studentlink.pl/1480436841?ModuleName=menu.pl&NewMenu=Academics")

        continue_link = self.driver.find_element_by_partial_link_text('Registration').click()
        find_username = self.driver.find_element_by_id("username")
        find_username.send_keys(username)
        find_password = self.driver.find_element_by_id("password")
        find_password.send_keys(password)
        find_password.send_keys(Keys.ENTER)
        self.driver.get("https://www.bu.edu/link/bin/uiscgi_studentlink.pl/1481040756?ModuleName=reg/option/_start.pl&ViewSem=Spring%202017&KeySem=20174")  # Changes depending on class
        Plan_link = self.driver.find_element_by_partial_link_text("Plan").click()
        Add_link = self.driver.find_element_by_partial_link_text("Add").click()

    def search(self, College, Dept, Course, Section):

        select = Select(self.driver.find_element_by_name("College"))
        select.select_by_visible_text(College)
        self.driver.find_element_by_name("Dept").send_keys(Dept)
        self.driver.find_element_by_name("Course").send_keys(Course)
        self.driver.find_element_by_name("Section").send_keys(Section)
        button = self.driver.find_element_by_xpath("//input[@type='button']")
        button.click()

        if int(self.driver.find_element_by_xpath("/html/body/form/table/tbody/tr[2]/td[6]").text) > -1:
            seats = int(self.driver.find_element_by_xpath("/html/body/form/table/tbody/tr[2]/td[6]").text)
        elif int(self.driver.find_element_by_xpath("/html/body/form/table/tbody/tr[3]/td[6]").text) > -1:
            seats = int(self.driver.find_element_by_xpath("/html/body/form/table/tbody/tr[3]/td[6]").text)
        elif int(self.driver.find_element_by_xpath("/html/body/form/table/tbody/tr[4]/td[6]").text) > -1:
            seats = int(self.driver.find_element_by_xpath("/html/body/form/table/tbody/tr[4]/td[6]").text)

        if seats>0:
            print("Good news the class is open!")
        else:
            print("It is closed")

root = Tk()
lf = LoginFrame(root)
root.mainloop()
lf.search("ENG", "ek", "128", "a1")

