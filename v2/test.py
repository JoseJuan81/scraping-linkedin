import pytest
from Class.Scraper import Scraper

URL_LOGIN = 'https://www.linkedin.com'

@pytest.fixture(scope="module")
def start():
    scraper = Scraper()
    scraper.start()
    yield scraper

def test_pagination(start):
    scraper = start
    scraper.get_pagination()

    assert len(scraper.pagination) >= 5

def test_get_employees(start):
    scraper = start
    employees = scraper.get_elements(css_selector=scraper.CONTACTS)

    assert len(employees) >= 7

def test_get_last_page(start):
    scraper = start
    page = scraper.get_pagination()

    assert page == 100

def test_get_next_page(start):
    scraper = start
    button = scraper.get_next_page_button(next_page=2)

    assert button.text == "2"

def test_get_employees(start):
    scraper = start
    scraper.get_employees()

    first = scraper.employees[0]
    assert first["name"] == "Claudia Arbe Peña-Vásquez"
    assert first["page_profile"] == "https://www.linkedin.com/in/claudia-arbe-pe%C3%B1a-v%C3%A1squez-6818bb5a?miniProfileUrn=urn%3Ali%3Afs_miniProfile%3AACoAAAyXiQEBg1xDOQNVe9Qi_bjCRQ-aCERrdTQ"
    assert first["job_position"] == "Executive Management Assistant en Southern Peaks Mining Ltd"
    assert first["country"] == "Peru"
    assert first["company_name"] == "Sp"

    eleven = scraper.employees[10]
    assert eleven["name"] == "Diego Estrada Benavides"
    assert eleven["page_profile"] == "https://www.linkedin.com/in/diego-estrada-benavides-9b9984109?miniProfileUrn=urn%3Ali%3Afs_miniProfile%3AACoAABtf5J0B43BHkYeiZG-8-Jlmz2dBQ21gXWM"
    assert eleven["job_position"] == "Ingeniero Ambiental | Especialista en recursos hídricos | Sector Minero energético"
    assert eleven["country"] == "Peru"
    assert eleven["company_name"] == "Sp"

