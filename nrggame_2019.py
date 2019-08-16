# -*- coding: utf-8 -*-
from selenium import webdriver
import time
import gmail_nrg_code as nrg_code

print("© 2019 zeveos .  ALL RIGHTS RESERVED.")
print("Created just 4 fun :D")
print("\r")

print("May the Force be with you.")
print("Patience you must have, my young padawan.")
driver = webdriver.Edge()
driver.get("https://game.energy.ch/")
# assert "Energy" in driver.title
answers = [
    "One Republic",
    "1300",
    "gewinnen",
    "XTRA-Circle",
    "Twitter",
    "E-Mail",
    "2014",
    "450 Tonnen",
    "70 Meter",
    "Die sechste",
    "Lo & Leduc",
    "im Radio, auf der Website und über Social Media",
    "40’000",
    "Energy Air findet trotzdem statt",
    "Im Privatjet",
    "Stade de Suisse, Bern",
    "Bastian Baker",
    "60",
    "Um 17 Uhr",
    "250",
    "Alvaro Soler",
    "14",
    "...der unter freiem Himmel stattfindet.",
    "Averdeck",
    "Sein Mami",
    "Eine komplett weisse Garderobe",
    "BSC Young Boys",
    "7. September 2019",
]


def press_answer(quest_nr):
    for answer in answers:
        try:
            labelname = "//label[@for=" + "'" + answer + "'"
            elem1 = driver.find_elements_by_xpath(labelname)[0]
            elem1.click()
            elem2 = driver.find_elements_by_xpath("//button[@id='next-question']")[0]
            elem2.click()
            print(answer)
        except:
            pass
    return quest_nr


question_Nr = 0
counter = 0
input("Press to enter script")
print("Enter Phone Nr: (do not enter starting '0'! Example: 798765432")
tel_nr = int(input("+41"))

while True:
    while question_Nr < 10:
        press_answer(question_Nr)
        question_Nr += 1
    else:
        try:
            elem2 = driver.find_elements_by_xpath("//div[@class='circle col-xs-4 col-sm-3 col-md-4 col-lg-3']")[7]
            elem2.click()
            try:
                elem1 = driver.find_elements_by_xpath("//button[@class='btn btn-primary game-button btn-lg']")[0]
                elem1.click()
            except:
                pass
        except:
            try:
                try:
                    elem3 = driver.find_elements_by_xpath("//input[@placeholder='Handynummer']")[0]
                    elem3.send_keys(tel_nr)
                    elem1 = driver.find_elements_by_xpath("//button[@class='btn btn-primary game-button btn-lg']")[0]
                    elem1.click()
                    found_mail = False
                    while found_mail is False:
                        sms_code = nrg_code.main()
                        if sms_code is not None:
                            found_mail = True
                            print(sms_code + "....................................................")
                            code_numb_list = []
                            for numb in sms_code:
                                code_numb_list.append(numb)
                            driver.find_elements_by_xpath("//input[@id='1']")[0].send_keys(code_numb_list[0])
                            driver.find_elements_by_xpath("//input[@id='2']")[0].send_keys(code_numb_list[1])
                            driver.find_elements_by_xpath("//input[@id='3']")[0].send_keys(code_numb_list[2])
                            driver.find_elements_by_xpath("//input[@id='4']")[0].send_keys(code_numb_list[3])
                            elem1 = \
                                driver.find_elements_by_xpath(
                                    "//button[@class='btn btn-primary game-button btn-lg btn-declined']")[0]
                            elem1.click()
                        else:
                            time.sleep(5)
                except:
                    pass
                elem1 = driver.find_elements_by_xpath("//button[@class='btn btn-primary game-button btn-lg']")[0]
                elem1.click()
            except:
                pass
            question_Nr = 0
    counter += 1
    print("COUNT:", counter)
    if counter == 100:
        driver.close()
        driver = webdriver.Edge()
        driver.get("https://game.energy.ch/")
        assert "Energy" in driver.title
        counter = 0
