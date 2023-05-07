# scraping-linkedin
python script to get contacts from severals companies using my premium linkedin account

### How to use
You need to create a 'secret.txt' at the root of the directory and add your LinkedIn email and password like this:
    my@email.com
    my_pass_123456

### Description in constantes.py
This file has many important information for the script to work fine:
`selected_positions` = The target company positions to get employees
`wrong_position` = The position I am not interested in. ej: i want to get Mechanical maintenance but not Electrical maintenance. "maintenance" is in selected_position and "electrical" is in wrong_position
`total_pages` = is the total employees pages that belongs to the targeted company. The value depends on each company
`main,ul,li...` = the XPATH used to get the WebElements from the web
