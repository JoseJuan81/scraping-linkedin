from selenium.webdriver.common.by import By
from constantes import html_elements, urls, total_pages, company_name, interested_position


def get_login(driver):
    driver.get(urls['home'])

    secret_file = open('secret.txt', 'r')
    lineas = secret_file.readlines()
    user = lineas[0].strip()
    password = lineas[1].strip()
    secret_file.close()

    input_user = driver.find_element(By.XPATH, html_elements['login__input_email'])
    input_pass = driver.find_element(By.XPATH, html_elements['login__input_pass'])

    input_user.send_keys(user)
    input_pass.send_keys(password)

    boton = driver.find_element(By.XPATH, html_elements['login__button'])
    boton.click()

def go_to__search_page(driver, page=1):
    search_url__base = urls['searching_people'](page)
    driver.get(search_url__base)

def scraping_page(driver):

    for i in range(1, total_pages):
        page = i
        go_to__search_page(driver, page) 

        lista_empleados__nombres = driver.find_elements(By.XPATH, html_elements['employees_name']) 
        lista_empleados__cargo = driver.find_elements(By.XPATH, html_elements['employees_position'])

        for web_nombre, web_cargo in zip(lista_empleados__nombres, lista_empleados__cargo):
            
            nombre = web_nombre.text 
            cargo = web_cargo.text 

            # if cargo in interested_position:
            
            if 'mantenimiento' in cargo:
                mantenimiento_file.write(f"{nombre}, {cargo}\n")
                print(nombre, cargo)

            if 'confiabilidad' in cargo:
                confiabilidad_file.write(f"{nombre}, {cargo}\n")

            if 'operaciones' in cargo:
                operaciones_file.write(f"{nombre}, {cargo}\n")



