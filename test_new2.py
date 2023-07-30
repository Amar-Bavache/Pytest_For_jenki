import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Test_Credence_002:


    def test_credkartlogin_001(self):
        driver = webdriver.Chrome()
        driver.get("https://automation.credence.in/login")
        driver.find_element(By.XPATH, "//input[@name='email']").send_keys("Credencetest@test.com")
        driver.find_element(By.CSS_SELECTOR, "input[id='password']").send_keys("Credence@1234")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        try:
            driver.find_element(By.XPATH, "//h2[normalize-space()='CredKart']")
            print("Login is Successfull")
            driver.close()
            assert True
        except:
            print(
                "Login is Failed"
            )
            driver.close()
            assert False




    def test_checkout_003(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        # Go to Url
        driver.get("https://automation.credence.in/login")
        driver.find_element(By.XPATH, "//input[@name='email']").send_keys("Credencetest@test.com")
        driver.find_element(By.CSS_SELECTOR, "input[id='password']").send_keys("Credence@123")
        # Click Login button
        driver.find_element(By.XPATH, "//button[@type='submit']").click()

        # Click on Product--Macbook
        driver.find_element(By.XPATH, "/html/body/div/div[2]/div[3]/div/div/a[2]/h3").click()
        # Click on add to cart
        driver.find_element(By.XPATH, "//input[@value='Add to Cart']").click()
        # Proceed to Checkout
        driver.find_element(By.XPATH, "//a[@class='btn btn-success btn-lg']").click()
        driver.implicitly_wait(10)
        # Enter First_Name
        driver.find_element(By.XPATH, "//input[@id='first_name']").send_keys("Credence")
        # Enter Last_Name
        driver.find_element(By.XPATH, "//input[@id='last_name']").send_keys("Pune")
        # Enter Phone
        driver.find_element(By.XPATH, "//input[@id='phone']").send_keys("9091929355")
        # Enter Address
        driver.find_element(By.XPATH, "//textarea[@id='address']").send_keys("Dhankawdi, Pune")
        # Enter Zip
        driver.find_element(By.XPATH, "//input[@id='zip']").send_keys("411013")
        # Select state
        state = Select(driver.find_element(By.XPATH, "//select[@id='state']"))
        state.select_by_visible_text("Pune")
        # Enter  Owner name
        driver.find_element(By.XPATH, "//input[@id='owner']").send_keys("Tushar")
        # Enter CVV
        driver.find_element(By.XPATH, "//input[@id='cvv']").send_keys("043")

        # Select Year
        year = Select(driver.find_element(By.XPATH, "//select[@id='exp_year']"))
        year.select_by_index(2)

        # Select Month
        month = Select(driver.find_element(By.XPATH, "//select[@id='exp_month']"))
        month.select_by_index(2)

        # Enter card number\
        # 5281 0370 4891 6168
        driver.find_element(By.XPATH, "//input[@id='cardNumber']").send_keys("5281")
        driver.find_element(By.XPATH, "//input[@id='cardNumber']").send_keys("0370")
        driver.find_element(By.XPATH, "//input[@id='cardNumber']").send_keys("4891")
        driver.find_element(By.XPATH, "//input[@id='cardNumber']").send_keys("6168")
        # Click on Checkout button
        driver.find_element(By.XPATH, "//button[@id='confirm-purchase']").click()

        print(driver.find_element(By.XPATH, "/html/body/div/div[1]/p[1]").text)

        driver.close()