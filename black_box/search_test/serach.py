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
    url = "http://localhost:8000/"
    test_case_path = "F:\\code\\software_system_test\\Software_QA\\black_box\\" + "search_test\\search_test_case.txt"
    test_ouput_path = "F:\\code\\software_system_test\\Software_QA\\black_box\\" + "search_test\\search_test_output.md"
    driver = webdriver.Edge("D:\\edge_driver\\msedgedriver.exe") # 括号内填写msedgedriver.exe的路径
    cnt = 1
    with open(test_case_path, "r", encoding="utf_8" ) as fp_case:
        for table in fp_case:
            driver.get(url)
            leave_city = driver.find_element(by=By.XPATH, value='//*[@id="leave_city"]')
            arrive_city = driver.find_element(by=By.XPATH, value='//*[@id="arrive_city"]')
            leave_date = driver.find_element(by=By.XPATH, value='//*[@id="leave_date"]')

            User_Info = str.split(table, "|")
            leave_city.send_keys(User_Info[0])
            arrive_city.send_keys(User_Info[1])
            leave_date.send_keys(User_Info[2])

            send_box = driver.find_element(by=By.XPATH, value='/html/body/div/form/center/button')
            send_box.click()

            # login_info = driver.find_element(by=By.XPATH, value='/html/body/nav/div/ul/li[3]/a') #存在疑问 debug运行查看
            curr_url = driver.current_url

            with open(test_ouput_path, "a", encoding="utf-8") as fp_out:
                fp_out.write('|' + str(cnt) + '|' + User_Info[0] + '|' + User_Info[1] + '|' + User_Info[2] + '|')
                if curr_url == "http://localhost:8000/booksystem/result/": # 非日期错误
                    try:
                        result = driver.find_element(by=By.XPATH, value='//*[@id="result_by_price"]')
                        if "机场" in result.text:
                            fp_out.write("有航班信息" + '|\n')
                        else:
                            fp_out.write("没有航班" + '|\n')                    
                    except Exception:
                        pass
                else:
                    fp_out.write("日期错误" + '|\n')
            cnt = cnt + 1

    driver.close()

if __name__ == '__main__':
    main()