

import allure
from selenium import webdriver
import pytest

class Test_Credence_001:

    def test_sum_001(self):
        a = 3
        b = 7
        sum = a + b
        print("Sum of a and b is :" + str(sum))
        if sum == 10:
            assert True
        else:
            assert False

    def test_CredenceUrl_002(self):
        driver = webdriver.Chrome()
        driver.get("https://credence.in/")
        if driver.title == "Credence":
            print("You are at credence.in")
            assert True
            driver.close()
        else:
            print("You are at Wrong url")
            driver.close()
            assert False

    @pytest.mark.xfail
    def test_sub_003(self):
        a = 3
        b = 7
        sub = a - b
        print("Subtraction of a from b is :" + str(sub))
        if sub == -4:
            assert True
        else:
            assert False