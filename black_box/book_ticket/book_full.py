#! py -3.9
# -*- coding: UTF-8 -*-

from ast import BoolOp
from base64 import encode
from encodings import utf_8
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import uuid

def main():
    url = "http://localhost:8000/booksystem/register/"
    target = "book_full"
    # test_case_path =  "F:\\code\\software_system_test\\Software_QA\\black_box\\" + target + "\\" + target + "_test_case.txt"
    test_output_path = "F:\\code\\software_system_test\\Software_QA\\black_box\\book_ticket\\" + target + "_test_output.md"
    driver = webdriver.Edge("D:\\edge_driver\\msedgedriver.exe")

    for i in range(100):
        driver.get(url)

        # 获取注册元素
        UserName = driver.find_element(by=By.XPATH, value='//*[@id="id_username"]')
        Email_Address = driver.find_element(by=By.XPATH, value='//*[@id="id_email"]')
        Password = driver.find_element(by=By.XPATH, value='//*[@id="id_password"]')

        # 填写注册信息
        UserName.send_keys(str(uuid.uuid4())[0:6])
        Email_Address.send_keys("user@email.cn")
        Password.send_keys("123456")

        # 点击注册按钮
        send_box = driver.find_element(by=By.XPATH, value='/html/body/div/div/div/div/div[1]/form/div[4]/div/button')
        send_box.click()

        # 获取航班查询元素
        leave_city = driver.find_element(by=By.XPATH, value='//*[@id="leave_city"]')
        arrive_city = driver.find_element(by=By.XPATH, value='//*[@id="arrive_city"]')
        leave_date = driver.find_element(by=By.XPATH, value='//*[@id="leave_date"]')

        # 填写航班信息
        leave_city.send_keys("长沙")
        arrive_city.send_keys("上海")
        leave_date.send_keys("0020220421")

        # 点击重新搜索按钮
        search_box = driver.find_element(by=By.XPATH, value='/html/body/div/div[1]/div/form/div[4]/div/input')
        search_box.click()

        # 点击订票按钮
        book_box = driver.find_element(by=By.XPATH, value='//*[@id="result_by_price"]/div[1]/div/div[4]/p/a')
        book_box.click()
        
        # 再次点击
        with open(test_output_path, "a", encoding="utf-8") as fp_out:
            # 获取剩余座位数量
            remain_seat = driver.find_element(by=By.XPATH, value='//*[@id="remain_seats"]')
            pre_remain = int(remain_seat.text)
            fp_out.write('|' + str(i) + '|' + remain_seat.text + '|')

            # 点击确定按钮
            confirm_box = driver.find_element(by=By.XPATH, value='//*[@id="book_btns"]/form/input')
            confirm_box.click()
            
            # 判断是否购买成功
            remain_seat = driver.find_element(by=By.XPATH, value='//*[@id="remain_seats"]')
            cur_remain = int(remain_seat.text)
            if pre_remain - cur_remain == 0:
                fp_out.write("OK" + '|\n')
            else:
                fp_out.write("Error|\n")
            
            # # 再次点击确定按钮
            # confirm_box = driver.find_element(by=By.XPATH, value='//*[@id="book_btns"]/form/input')
            # confirm_box.click()

            # # 判断是否重复购买
            # already_buy = driver.find_element(by=By.XPATH, value='//*[@id="info_body"]/p')
            # if "订购过" in already_buy.text:
            #     fp_out.write("N|\n")
            # else:
            #     fp_out.write("**Y**|\n")

    driver.close()

if __name__ == '__main__':
    main()