from services.SecapScraper import SecapScraper
from services.Cleaner import Cleaner
from flask import current_app


# controller to get person data
def get_person_data(param, to):

    try:
        # create url to consult
        full_url = f"{current_app.config['SCRAP_URL']}?num_doc={param}"

        # Extract person data with url and request timeout
        scraper = SecapScraper(full_url, to)
        scraper.extract_web_content()
        web_content = scraper.get_web_content()
        
        if web_content["success"]:
            # Transform person data
            cleaner = Cleaner(web_content["message"])
            cleaner.parse_list_content()
            cleaner.clean_list("latin-1")
            cleaner.make_person_dictionary()
            
            return cleaner.get_person_dictionary()
        else:
            return {
                "status": "FAILED",
                # "data": {"error": "Something was wrong, cannot get web content"}
                "data": {"error": web_content["message"]}
            }
    except:
        return {
            "status": "FAILED",
            "data": {"error": "Cannot get person data"}
        }
    # except Exception as err:
    #     return {
    #         "status": "FAILED",
    #         "data": {"error": err.args}
    #     }
