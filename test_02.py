import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_Credence_002:

    @pytest.mark.skip
    def test_CredKart_Login_008(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        # Go to Url
        driver.get("https://automation.credence.in/login")
        driver.find_element(By.XPATH, "//input[@name='email']").send_keys("Credencetest@test.com")
        driver.find_element(By.CSS_SELECTOR, "input[id='password']").send_keys("Credence@1234")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        try:
            driver.find_element(By.XPATH, "//h2[normalize-space()='CredKart']")
            print("Login TestCase is Passed")
            driver.close()
            assert True
        except:
            print("Login TestCase is Failed")
            driver.close()
            assert False