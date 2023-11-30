import os

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement

from Class.Html import HtmlSelectors, HtmlElements
from Class.Employee import Employee
from Class.Helpers import Helpers

load_dotenv()
USER_EMAIL = os.getenv("USER_EMAIL")
USER_PASS = os.getenv("USER_PASS")

URL_LOGIN = 'https://www.linkedin.com'

class Scraper(HtmlSelectors, HtmlElements, Helpers):
    def __init__(self):
        super().__init__()
        self.drive: webdriver = None
        self.employees: list = []
        self.employees_elements: list[WebElement] = []
        self.company_name: str = ""
        self.pagination: list = []
        self.employees_page: str = ""

    def start(self) -> None:
        """
        Funcion para iniciar proceso de scraping
        """

        self.start_browser()
        self.go_to_page(url=URL_LOGIN)
        self.login()
        self.employees_page = self.request_url()
        self.company_name = self.request_company_name()
        self.go_to_page(url=self.employees_page)

    def request_url(self) -> str:
        """
        Funcion para solicitar al usuario la url de la que se obtendran
        los contactos
        """

        response = None
        while not response:
            res = input("\nIntroduzca la url para extraer los datos\n")
            if res:
                response = res
        
        return response
    
    def request_company_name(self) -> str:
        """
        Funcion para solicitar al usuario el nombre de la compania
        a scrapear
        """

        response = None
        while not response:
            res = input("\nIntroduzca el nombre de la compania\n")
            if res:
                response = res
        
        return response
    
    def login(self) -> None:
        """
        Funcion para iniciar sesion en LinkedIn
        """

        input_user = self.get_element(self.LOGIN_INPUT_EMAIL)
        input_pass = self.get_element(self.LOGIN_INPUT_PASS)

        input_user.send_keys(USER_EMAIL)
        input_pass.send_keys(USER_PASS)

        btn = self.get_element(self.LOGIN_BUTTON)
        btn.click()
        input("Agrega el codigo de verificacion si es necesario y presiona enter\n")

    def go_to_page(self, url: str = "") -> None:
        """
        Funcion para ir a una determinada pagina
        """

        self.driver.get(url)

    def start_browser(self) -> None:
        """
        Funcion para iniciar navegador de Selenium
        """

        self.driver = webdriver.Chrome()
        self.driver.set_window_size(1400, 1000)
        self.driver.implicitly_wait(8)

    def get_employees(self) -> None:
        """
        Funcion para obtener los empleados de la compania
        """

        page = 1
        url = self.get_full_employee_page(page=page)
        self.go_to_page(url=url)

        total_pages = self.get_pagination()

        while page <= total_pages:
            print("\n")
            print(f"Pagina: {page}")

            self.employees_elements = self.get_elements(css_selector=self.CONTACTS)

            print(f"{len(self.employees_elements)} empleados...")

            self.iterate_on_employees()
            self.save_data(data=self.employees, file_name=self.company_name)

            if page < total_pages:
                self.get_next_page_button(next_page=page + 1)

            page += 1

    def get_next_page_button(self, next_page: int = 0) -> WebElement:
        """
        Funcion para obtener el siguiente boton de la paginacion
        que sera presionado
        """

        self.scroll_down()
        super().wait(1, 2)
        css_selector = super().next_pagination_button_selector(next_page)
        button = super().get_element(css_selector=css_selector)

        if button:
            button.click()
        else:
            url = self.get_full_employee_page(next_page)
            self.go_to_page(url=url)

    def get_full_employee_page(self, page: int = 1) -> None:
        """
        Funcion para construir la url con la paginacion correspondiente
        """

        return f"{self.employees_page}&page={page}"

    def get_pagination(self) -> int:
        """
        Funcion para obtener los botones de la paginacion y retornar
        el numero total de paginas
        """

        self.scroll_down()
        self.pagination = self.get_elements(css_selector=self.PAGINATION)
        last_page_element = self.pagination[-1]
        last_page = int(last_page_element.text)
        return last_page

    def iterate_on_employees(self) -> None:
        """
        Funcion para iterar sobre el arreglo de empleados obtenidos
        """

        for employee_element in self.employees_elements:
            people = Employee(employee_element)
            print(f"Nombre del empleado: {people.name()}")

            employee_data = dict([
                ("name", people.name()),
                ("page_profile", people.page_profile()),
                ("job_position", people.job_position()),
                ("country", people.country()),
                ("company_name", self.company_name.title())
            ])

            # guardar en Notion
            self.employees.append(employee_data)

    def save_employees_in_notion(self) -> None:
        """
        Funcion para guardar datos obtenidos en una base de datos
        de notion
        """

        pass

    def end(self) -> None:
        """
        Funcion para finalizar proceso de scraping
        """

        print("&&"*40)
        print("FIN")
        print("&&"*40)