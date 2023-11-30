from selenium.webdriver.remote.webelement import WebElement

from Class.Html import HtmlSelectors, HtmlElements

class Employee(HtmlSelectors, HtmlElements):
    def __init__(self, web_element):
        super().__init__()
        self.web_element: WebElement = web_element

    def name(self) -> str:
        """
        Funcion para obtener el nombre del empleado
        """
        _name = self.get_element(
            css_selector=self.CONTACT_NAME,
            web_element=self.web_element)
        return _name.text if _name else "sin nombre"

    def page_profile(self) -> str:
        """
        Funcion para obtener la pagina del empleado
        """

        _page_profile = self.get_element(
            css_selector=self.CONTACT_PROFILE_PAGE,
            web_element=self.web_element)
        return _page_profile.get_attribute("href") if _page_profile else "sin pagina de perfil"

    def job_position(self) -> str:
        """
        Funcion para obtener el cargo del empleado
        """

        _job_position = self.get_element(
            css_selector=self.CONTACT_JOB_POSITION,
            web_element=self.web_element)
        return _job_position.text if _job_position else "sin cargo"
    
    def country(self) -> str:
        """
        Funcion para obtener el pais
        """

        _country = self.get_element(
            css_selector=self.CONTACT_COUNTRY,
            web_element=self.web_element)
        return _country.text if _country else "sin pais"