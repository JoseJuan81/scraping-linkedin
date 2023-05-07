from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import os
import helper as h
from constantes import html_elements, urls, total_pages, company_name, selected_positions, wrong_positions

### Ruta absoluta para guardar archivos con data recopilada
working_dir = os.getcwd()  # Get the current working directory (cwd)
data_dir = 'data'
abs_path = os.path.join(working_dir, data_dir)

### Crear el webdriver de Chrome
opts = Options()
driver = webdriver.Chrome(ChromeDriverManager().install(), options=opts)

### FUNCIONES
def get_login(driver):
    """
    FUNCIÓN PARA INICIAR SESIÓN EN LINKEDIN
    """
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
    """
    FUNCIÓN PARA IR A PÁGINA DE PERSONAL DE LA EMPRESA SELECCIONADA
    """
    search_url__base = urls['searching_people'](page)
    driver.get(search_url__base)
    
def group_by_position(all_employees):
    """
    FUNCIÓN PARA AGRUPAR EMPLEADOS POR CARGOS
    """
    acc = {}
    
    for employee in all_employees:
        position = employee['key_position']
        if position in acc:
            acc[position].append(employee)
        else:
            acc[position] = [employee]
            
    return acc

def build_employees_object(employees_data, selected_positions, wrong_positions, page):
    """
    FUNCIÓN PARA CREAR ARREGLO DE OBJETO DE EMPLEADOS CON LAS PROPIEDA DEFINIDAS
    NOMBRE, CARGO, ENLACE A PÁGINA Y POSICIÓN CLAVE
    ADICIONALMENTE SE FILTRAN LOS EMPLEADOS TOMANDO EN CUENTA LOS CARGOS DE INTERÉS
    """
    acc = []

    for full_name, link, employee_position  in employees_data:
        for position in selected_positions:
            if position.lower() in employee_position.lower():
                wrong = 0
                
                for wrong_position in wrong_positions:
                    if wrong_position in employee_position.lower():
                        wrong += 1
                
                if wrong == 0:
                    data = {
                        'name': full_name,
                        'position': employee_position,
                        'link': link,
                        'page': page,
                        'key_position': position,
                    }
                    acc.append(data)

    return acc

def get_data_from_WebElement(data, operator='text'):
    """
    FUNCIÓN GENÉRICA PARA EXTRAE INFORMACIÓN DE LOS WEBELEMENTS OBTENIDOS
    """
    acc = []
    
    if operator == 'get_attribute':
        for d in data:
            acc.append(d.get_attribute("href"))
    elif operator == 'text':
        for d in data:
            acc.append(d.text)
            
    return acc

def extract_employees_from_web(driver):
    """
    FUNCIÓN PARA OBTENER INFORMACIÓN DE LA PÁGINA WEB
    """
    
    employees_name_list = driver.find_elements(By.XPATH, html_elements['employees_name'])
    employees_name = get_data_from_WebElement(employees_name_list)
    
    employees_page_list = driver.find_elements(By.XPATH, html_elements['employees_page'])
    employees_page = get_data_from_WebElement(employees_page_list, 'get_attribute')
    
    employees_position_list = driver.find_elements(By.XPATH, html_elements['employees_position'])
    employees_position = get_data_from_WebElement(employees_position_list)
    
    return list(zip(employees_name, employees_page, employees_position))

def scraping_page(driver):
    """
    FUNCIÓN PARA OBTENER TODO EL PERSONAL DE LA EMPRESA SELECCIONADA y CLASIFICARLO POR CARGOS
    """
    acc = []
    for i in range(1, total_pages + 1):
        
        page = i
        go_to__search_page(driver, page) 
        employees_data = extract_employees_from_web(driver)        
        employees_list_props = build_employees_object(employees_data, selected_positions, wrong_positions, page)
        
        if employees_list_props != []:
            acc += employees_list_props

    return acc

def creating_files(employees_grouped_by_position):
    
    base_path = os.getcwd()
    saving_dir = os.path.join(base_path, "data", company_name)
    
    if not os.path.exists(saving_dir):
        os.makedirs(saving_dir)

    for position in employees_grouped_by_position:
        
        saving_path = f"{position}_{company_name}.txt"
        save = os.path.join(saving_dir, saving_path)
        data = employees_grouped_by_position[position]
        
        with open(save, "w", encoding="utf-8") as file:
            for d in data:
                name = f'name: {d["name"]}'
                position = f'position: {d["position"]}'
                link = f'link: {d["link"]}'
                page = f'page: {d["page"]}'
                key_position = f'key_position: {d["key_position"]}'
                
                txt = f"{name}\n{position}\n{link}\n{page}\n{key_position}\n\n"
                file.write(txt)


get_login()
employees = scraping_page(driver)
employees_filtered = group_by_position(employees)
creating_files(employees_filtered)
    
