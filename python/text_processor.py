import json


class Text:
    def __init__(self):
        with open("text_save", "w+", encoding="utf-8") as file:
            pass

    def save_json(self, data, file_name="text_save.txt"):
        with open(file_name, "w", encoding="utf-8") as file:
            json.dump(data, file)



if __name__ == '__main__':
    data = {
        'asd': 'asfas',
        'asd1': 'asfas',
        'asd2': 'asfas',
        'asd3': 'asfas',
        'asd4': 'asfas',
        'asd5': 'asfas',
        'asd5dв': 'asfas',
    }
    cl = Text()
    cl.save_json(data)
