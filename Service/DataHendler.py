from hashlib import new
import requests


class DataHendler:
    def __init__(
        self,
    ):
        self.data = []

    def get_numbers_from_api(self, url_request):
        page_number = 1
        while True:
            request = requests.get(url_request + str(page_number))
            if request.json().get("numbers") != []:
                try:
                    self.data = self.data + request.json().get("numbers")
                    page_number += 1
                    print(page_number)
                except:
                    pass
            else:
                break
        return self.sort_list()

    def sort_list(
        self,
    ):
        ordered_list = [self.data[0]]
        for i in range(0, len(self.data)):
            if self.data[i] > ordered_list[-1]:
                ordered_list.append(self.data[i])
            else:
                position = 0
                while position < len(ordered_list):
                    if self.data[i] <= ordered_list[position]:
                        ordered_list.insert(position, self.data[i])
                        break
                    position += 1
        return ordered_list
