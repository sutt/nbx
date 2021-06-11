from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time

from .common import *

def basic_1(ERR_MSGS=[], TEST_FAILS=False, b_no_tear_down=False):

    d_outputs = {}
    
    print(f"starting basic_1...teardown: {b_no_tear_down}")
    
    ### Launch Notebook

    teacher_driver = webdriver.Chrome()
    student_driver = webdriver.Chrome()

    teacher_url = 'http://localhost:9200/tree?'
    student_url = 'http://localhost:9201/tree?'

    teacher_driver.get(teacher_url)
    student_driver.get(student_url)

    time.sleep(2)

    nb_name = "book1.ipynb"

    for driver in (teacher_driver, student_driver):
        
        links = driver.find_elements_by_class_name(
                            "item_link"
                        )

        ind_book = [ i 
                    for i, link in enumerate(links) 
                    if link.text == nb_name
                ][0]

        print(ind_book)

        nb_link = links[ind_book]

        nb_link.click()
        driver.quit()

    time.sleep(1)

    ### Open Both Notebooks

    teacher_driver = webdriver.Chrome()
    student_driver = webdriver.Chrome()

    teacher_url = "http://localhost:9200/notebooks/" + nb_name
    student_url = "http://localhost:9201/notebooks/" + nb_name

    teacher_driver.get(teacher_url)
    student_driver.get(student_url)

    ### Teacher::send_answer()

    driver = teacher_driver

    for i_action, cell_num in enumerate((0,1,2,3,4)):
        
        class_name = "code_cell"
        elems = driver.find_elements_by_class_name(class_name)
        
        cell = elems[cell_num]

        inner_class = "input_area"
        inner = cell.find_element_by_class_name(inner_class)
        inner.click()
        
        time.sleep(0.1)
        
        if cell_num == 3:
            
            outputs_0 = get_cell_outputs(cell)

            action = ActionChains(driver)
            action.send_keys("import random;random.randint(0,1e6)")
            action.perform()
            
            time.sleep(0.3)
            
        if cell_num == 4:
            
            action = ActionChains(driver)
            action.send_keys("nbx.send_answer()")
            action.perform()
            
            time.sleep(0.3)


        action = ActionChains(driver)
        action.key_down(Keys.SHIFT)
        action.send_keys(Keys.ENTER)   
        
        action.key_up(Keys.SHIFT)
        action.perform()    
        
        time.sleep(0.3)

        if cell_num == 3:

            outputs_1 = get_cell_outputs(cell)
                                    
            if outputs_0 == outputs_1:
                ERR_MSGS.append("BAD JUPYTER ACTION: teacher nb test cell not executed")
                TEST_FAILS = True

    time.sleep(3)

    ### Student::receive_answer()

    driver = student_driver

    for i_action, cell_num in enumerate((0,1,2,3)):
        
        class_name = "code_cell"
        elems = driver.find_elements_by_class_name(class_name)
        
        cell = elems[cell_num]

        inner_class = "input_area"
        inner = cell.find_element_by_class_name(inner_class)
        inner.click()
        
        time.sleep(0.1)
        
        if i_action == 3:
            
            action = ActionChains(driver)
            action.send_keys("nbx.receive_answer()")
            action.perform()
            
            time.sleep(0.3)
                    

        action = ActionChains(driver)
        action.key_down(Keys.SHIFT)
        action.send_keys(Keys.ENTER)
        
        action.key_up(Keys.SHIFT)
        action.perform()    
        
        time.sleep(0.3)

        if i_action == 3:
            
            # allow student nb reload enough to finish before checking answer cell
            time.sleep(10)

            attempts = 0
            success = False
            while(attempts < 3):
                try:
                    class_name = "code_cell"
                    elems = driver.find_elements_by_class_name(class_name)
                    cell = elems[cell_num]
                    outputs_3 = get_cell_outputs(cell)

                    if outputs_3 != outputs_1:
                        ERR_MSGS.append(f"RECEIVED OUTPUT DOES NOT MATCH SENT: sent:\n{outputs_1}\nreceived:\n{outputs_3}")
                        TEST_FAILS = True

                    success = True
                    break

                except:
                    attempts += 1
                    time.sleep(1)
            
            if not(success): print("FAILED to load cells on refreshed notebook")

    ### Tear Down

    time.sleep(10)

    if not(b_no_tear_down):
        teacher_driver.quit()
        student_driver.quit()

    return ERR_MSGS, TEST_FAILS, d_outputs