#! py -3.9
# -*- coding: UTF-8 -*-

from base64 import encode
from encodings import utf_8
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def main():
    driver = webdriver.Edge("D:\edge_driver\msedgedriver.exe") # 括号内填写msedgedriver.exe的路径
    cnt = 1
    with open("F:\\code\python\\regisrer_test\\register_test_case.txt", "r", encoding="utf_8" ) as fp_case:
        for table in fp_case:
            driver.get("http://localhost:8000/booksystem/register/")
            UserName = driver.find_element(by=By.XPATH, value='//*[@id="id_username"]')
            Email_Address = driver.find_element(by=By.XPATH, value='//*[@id="id_email"]')
            Password = driver.find_element(by=By.XPATH, value='//*[@id="id_password"]')

            # 填写注册信息
            User_Info = str.split(table, "|")
            UserName.send_keys(User_Info[0])
            Email_Address.send_keys(User_Info[1])
            Password.send_keys(User_Info[2])

            # 点击注册按钮
            send_box = driver.find_element(by=By.XPATH, value='/html/body/div/div/div/div/div[1]/form/div[4]/div/button')
            send_box.click()

            login_info = driver.find_element(by=By.XPATH, value='/html/body/nav/div/ul/li[3]/a') #存在疑问 debug运行查看

            with open("F:\\code\\python\\regisrer_test\\register_test_output.md", "a", encoding="utf-8") as fp_out:
                fp_out.write('|' + str(cnt) + '|')
                if "登录" in login_info.text:
                    try:
                        username_back = driver.find_element(by=By.XPATH, value='/html/body/div/div/div/div/div[1]/form/div[1]/div[1]/span/ul/li')
                        fp_out.write(username_back.text + '|')                    
                    except Exception:
                        fp_out.write('|')
                    try:
                        email_back    = driver.find_element(by=By.XPATH, value='/html/body/div/div/div/div/div[1]/form/div[2]/div[1]/span/ul/li')
                        fp_out.write(email_back.text + '|')
                    except Exception:
                        fp_out.write('|')
                    try:
                        password_back = driver.find_element(by=By.XPATH, value='/html/body/div/div/div/div/div[1]/form/div[3]/div[1]/span/ul/li')
                        fp_out.write(password_back + '|')
                    except Exception:
                        fp_out.write('|')
                    fp_out.write('Failure|\n')
                else:
                    welcome = driver.find_element(by=By.XPATH, value='/html/body/nav/div/ul/li[3]/a')
                    if User_Info[0] in welcome.text:
                        fp_out.write('|||' + welcome.text + '|\n')
            cnt = cnt + 1

    driver.close()

if __name__ == '__main__':
    main()