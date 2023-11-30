from typing import Union
from selenium.webdriver.remote.webelement import WebElement
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class HtmlSelectors:
    def __init__(self) -> None:
        self.LOGIN_INPUT_EMAIL: str = "input#session_key"
        self.LOGIN_INPUT_PASS: str = "input#session_password"
        self.LOGIN_BUTTON: str = "button[data-id='sign-in-form__submit-btn']"
        self.CONTACTS: str = "li.reusable-search__result-container"
        self.CONTACT_PROFILE_PAGE: str = "span.entity-result__title-text a[data-test-app-aware-link]"
        self.CONTACT_NAME: str = f"{self.CONTACT_PROFILE_PAGE} span span"
        self.CONTACT_JOB_POSITION: str = "div.entity-result__primary-subtitle"
        self.CONTACT_COUNTRY: str = "div.entity-result__secondary-subtitle"
        self.PAGINATION: str = "ul.artdeco-pagination__pages--number li button"
        self.BODY: str = "body[dir]"

    def next_pagination_button_selector(self, page) -> str:
        """
        Funcion que retorna el selector css para obtener el boton de
        paginacion
        """
        selector = f'button[aria-label="Página {page}"]'
        return selector

class HtmlElements:
    def scroll_down(self) -> None:
        """
        Funcion para hacer scroll a la pantalla para que aparezcan
        los botones de la paginacion
        """

        body = self.get_element(css_selector=self.BODY)
        body.send_keys(Keys.END)

    def get_elements(self, css_selector: str = "", web_element: Union[webdriver, WebElement, None] = None) -> Union[list[WebElement], list]:
        """
        Funcion para obtener elementos html usando CSS_SELECTOR
        """

        driver = web_element if web_element else self.driver
        try:
            elements = driver.find_elements(By.CSS_SELECTOR, css_selector)
            return elements
        except Exception as err:
            print("Error al obtener los elementos con el css_selector")
            print(err)
            print("Error al obtener los elementos con el css_selector")
            return []

    def get_element(self, css_selector: str = "", web_element: Union[webdriver, WebElement, None] = None) -> Union[WebElement, str]:
        """
        Funcion para obtener elementos html usando CSS_SELECTOR
        """

        driver = web_element if web_element else self.driver
        try:
            element = driver.find_element(By.CSS_SELECTOR, css_selector)
            return element
        except Exception as err:
            print("Error al obtener el elemento con el css_selector")
            print(err)
            print("Error al obtener el elemento con el css_selector")
            return ""