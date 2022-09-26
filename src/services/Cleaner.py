import json


# Class for transform and clean
class Cleaner:

    def __init__(self, content):
        self.content = content
        self.list = []
        self.person_dic = {}

    def get_content(self):
        return self.content

    def set_content(self, content):
        self.content = content

    def get_list(self):
        return self.list

    def set_list(self, list):
        self.list = list

    def get_person_dictionary(self):
        return self.person_dic

    def set_person_dictionary(self, person_dic):
        self.person_dic = person_dic

    def parse_list_content(self):
        try:
            json_list = json.loads(self.get_content())
            self.set_list(json_list["rows"][0]["cell"])
        except:
            self.set_list([])

    def clean_list(self, charset):
        data_list = self.get_list()

        for index, item in enumerate(data_list):
            if isinstance(item, str):
                data_list[index] = item.encode(
                    charset, "replace").decode().strip()

        self.set_list(data_list)

    def make_person_dictionary(self):
        try:
            person_dic = {}
            person_dic["last-names"] = self.get_list()[0]
            person_dic["names"] = self.get_list()[1]
            person_dic["full-name"] = self.get_list()[2]
            person_dic["birth-date"] = self.get_list()[3]
            person_dic["ci-type"] = self.get_list()[5]
            person_dic["mother-name"] = self.get_list()[6]
            person_dic["father-name"] = self.get_list()[7]
            person_dic["academic-degree"] = self.get_list()[13]
            person_dic["message"] = self.get_list()[16]
            person_dic["consulted-at"] = self.get_list()[17]

            self.set_person_dictionary(person_dic)
            print("person", person_dic)
        except:
            self.set_person_dictionary(
                {"status": "FAILED", "data": {"error": "There was an error formatting the person data"}})
