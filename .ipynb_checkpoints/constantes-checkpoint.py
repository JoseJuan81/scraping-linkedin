target_positions = ('mantenimiento', 'confiabilidad', 'operaciones', 'compras', 'logistica', 'logística', "reliability", "maintenance", "metalurgia", "metallurgical")

company_name = 'antapacay'

total_pages = 78

html_elements = {
        'login__input_email': '//input[@id="session_key"]',
        'login__input_pass': '//input[@id="session_password"]',
        'login__button': '//button[@data-id="sign-in-form__submit-btn"]',
        'employees_page': '//li[@class="reusable-search__result-container"]//a',
        'employees_name': '//li[@class="reusable-search__result-container"]//a//span[@aria-hidden="true"]',
        'employees_position': '//li[@class="reusable-search__result-container"]//div[@class="entity-result__primary-subtitle t-14 t-black t-normal"]',
}

urls = {
    'home':'https://www.linkedin.com',
    'searching_people': lambda page: f"https://www.linkedin.com/search/results/people/?currentCompany=%5B%223658000%22%5D&origin=COMPANY_PAGE_CANNED_SEARCH&page={page}&sid=vx7",
}
