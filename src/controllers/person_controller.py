from classes.SecapScraper import SecapScraper
from classes.Cleaner import Cleaner
from flask import current_app


# controller to get person data
def get_person_data(param, to):

    try:
        # create url to consult
        full_url = current_app.config["SCRAP_URL"] + "?num_doc=" + param

        # Extract person data with url and request timeout
        scraper = SecapScraper(full_url, to)
        scraper.extract_web_content()
        web_content = scraper.get_web_content()

        # Transform person data
        cleaner = Cleaner(web_content)
        cleaner.parse_list_content()
        cleaner.clean_list("latin-1")
        cleaner.make_person_dictionary()

        return cleaner.get_person_dictionary()
    except Exception:
        return {"status": "FAILED", "data": {"error": "Cannot get person data"}}
