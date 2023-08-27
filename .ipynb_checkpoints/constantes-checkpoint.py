selected_positions = ('mantenimiento', 'confiabilidad', 'operaciones', 'compras', 'logistica', 'logística', "reliability", "maintenance", "metalurgia", "metallurgical", "planeamiento", "planner", "supply")

wrong_positions = ('electricista', 'electrical', 'instrumentacion', 'instrumentación', 'instrumentation', 'electrico', 'eléctrico', 'practicante', 'ambiental')

company_name = 'corona'

total_pages = 26

main = '//main[@aria-label="Resultados de búsqueda"]'
ul = '//ul[@class="reusable-search__entity-result-list list-style-none"]'
li = '//li[@class="reusable-search__result-container"]'
input_email = '//input[@id="session_key"]'
input_pass = '//input[@id="session_password"]'
login_button = '//button[@data-id="sign-in-form__submit-btn"]'

employee_div = '//div[@class="entity-result__content entity-result__divider pt3 pb3 t-12 t-black--light"]'
employee_name = '//span[@dir="ltr"]//span[@aria-hidden="true"]'
employee_position = '//div[@class="entity-result__primary-subtitle t-14 t-black t-normal"]'
employee_link = '//span[@class="entity-result__title-line entity-result__title-line--2-lines "]//a'

html_elements = {
        'login__input_email': input_email,
        'login__input_pass': input_pass,
        'login__button': login_button,
        'employees_page': main + ul + li + employee_div + employee_link,
        'employees_name': main + ul + li + employee_div + employee_name,
        'employees_position': main + ul + li + employee_position,
        'employees_li': main + ul + li
}


urls = {
    'home':'https://www.linkedin.com',
    'searching_people': lambda page: f"https://www.linkedin.com/search/results/people/?currentCompany=%5B%2235504118%22%5D&origin=COMPANY_PAGE_CANNED_SEARCH&page={page}&sid=~j2",
}