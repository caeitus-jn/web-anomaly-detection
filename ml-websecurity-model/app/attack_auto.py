from selenium import webdriver
from selenium.webdriver.common.by import By
import string, random, time


driver = webdriver.Chrome()


def a_or_b():
    return random.randint(1,2)

def a_or_b_or_c():
    return random.randint(1,2,3)

def sqli():
    starter = [
        "' OR ",
        "' AND ",
        "\" OR ",
        "\" AND ",
        "'; ",
        "'-- ",
        "'# ",
        "') OR (",
        "') AND ('1'='1",
    ]

    logical = [
        "1=1",
        "1=0",
        "'1'='1'",
        "'admin'",
        "'password'",
        "EXISTS(SELECT * FROM users)",
    ]

    operators = [
        "UNION SELECT",
        "ORDER BY 1--",
        "GROUP BY 1--",
        "LIMIT 1",
        "DROP TABLE users",
        "INSERT INTO users",
    ]

    closers = [
        ";--",
        "--",
        "#",
        "",
    ]
    return

def xss():
    return


for i in range(1000):
    driver.get("http://localhost:5000/authenticate")
    type = a_or_b_or_c()
    
    # SQLi
    if a_or_b() == 1:
        # Username payload
        if type == 1:
            username = ""
            password = ""
        # Password payload
        if type == 2:
            username 
            password
        # Combined payload
        if type == 3:
            username 
            password

    # XSS        
    else:
        username
        password


    driver.find_element(By.NAME, "username").send_keys(username)
    driver.find_element(By.NAME, "password").send_keys(password)
    driver.find_element(By.XPATH, "//input[@type='submit']").click()

    time.sleep(0.2)

driver.quit()
    