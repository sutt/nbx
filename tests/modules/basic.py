from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time

def basic_1():

    print("starting basic_1...")
    
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

    ### Open Both Notebook

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
            
            action = ActionChains(driver)
            action.send_keys("import random;random.randint(0,1e6)")
            action.perform()
            
            time.sleep(0.3)
            
        if cell_num == 4:
            
            action = ActionChains(driver)
            action.send_keys("nbx2.send_answer()")
            action.perform()
            
            time.sleep(0.3)


        action = ActionChains(driver)
        action.key_down(Keys.SHIFT)
        action.send_keys(Keys.ENTER)   
        
        action.key_up(Keys.SHIFT)
        action.perform()    
        
        time.sleep(0.3)

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
        
        if cell_num == 3:
            
            action = ActionChains(driver)
            action.send_keys("nbx2.receive_answer()")
            action.perform()
            
            time.sleep(0.3)


        action = ActionChains(driver)
        action.key_down(Keys.SHIFT)
        action.send_keys(Keys.ENTER)
        
        action.key_up(Keys.SHIFT)
        action.perform()    
        
        time.sleep(0.3)

    ### Tear Down

    time.sleep(10)

    teacher_driver.quit()
    student_driver.quit()

