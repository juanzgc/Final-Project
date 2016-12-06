from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("/Users/chasejamieson/Downloads/chromedriver")

def login(username, password):

    driver.get("https://www.bu.edu/link/bin/uiscgi_studentlink.pl/1480437400?ModuleName=menu.pl&NewMenu=Academics")
    driver.find_element_by_partial_link_text("Registration").click()
    driver.find_element_by_id("username").send_keys(username)
    driver.find_element_by_id("password").send_keys(password)
    driver.find_element_by_class_name("input-submit").click()
    driver.get("https://www.bu.edu/link/bin/uiscgi_studentlink.pl/1481039502?ModuleName=reg/option/_start.pl&ViewSem=Spring%202017&KeySem=20174")
    driver.find_element_by_partial_link_text("Register for Class").click()

def searchCourse(college, depart, course, section):

    seats = 0

    Select(driver.find_element_by_name("College")).select_by_visible_text(college)
    driver.find_element_by_name("Dept").send_keys(depart)
    driver.find_element_by_name("Course").send_keys(course)
    driver.find_element_by_name("Section").send_keys(section)
    driver.find_element_by_xpath("/html/body/table/tbody/tr[3]/td[2]/form/table/tbody/tr[2]/td[6]/input").click()

    if int(driver.find_element_by_xpath("/html/body/form/table/tbody/tr[2]/td[6]").text) > -1:
        seats = int(driver.find_element_by_xpath("/html/body/form/table/tbody/tr[2]/td[6]").text)
    elif int(driver.find_element_by_xpath("/html/body/form/table/tbody/tr[3]/td[6]").text) > -1:
        seats = int(driver.find_element_by_xpath("/html/body/form/table/tbody/tr[3]/td[6]").text)

    if seats > 0:
        print("Good news the class is open!")
    else:
        print("Sorry, the class is full.")

college = input("Enter College: ")
dept = input("Enter Department: ")
course = input("Enter Course: ")
section = input("Enter Section: ")
username = input("Enter Username: ")
password = input("Enter Password: ")
login(username, password)
searchCourse(college, dept, course, section)
yes = "Hello"