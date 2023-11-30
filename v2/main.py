from Class.Scraper import Scraper

if __name__ == "__main__":
    scraper = Scraper()
    scraper.start()
    scraper.get_employees()
    #scraper.save_employees_in_notion()
    scraper.end()