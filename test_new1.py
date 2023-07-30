import pytest
from selenium import webdriver


class Test_Credence_001:

    def test_sum_001(self):
        a = 5
        b = 2
        sum = a+b
        print('sum of a+b=', sum)
        if sum == 7:
            assert True
        else:
            assert False


    def test_credenceurl_002(self):
        driver = webdriver.Chrome()
        driver.get("https://credence.in/")
        if driver.title == "Credence":
            print('You are in correct url')
            driver.close()
            assert True
        else:
            print('You are in incorrect url')
            driver.close()
            assert False

    def test_sub_003(self):
        a = 10
        b = 3
        sub = a-b
        if sub == 7:
            print('substraction of a-b=' + str(sub))
            assert True

        else:
            assert False
