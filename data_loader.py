import re


class DataLoader:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_data(self):
        with open(self.file_path, "r", encoding="utf-8") as file:
            data = file.read()
        return data

    def preprocess_data(self, data):
        # Basic preprocessing to split messages
        messages = data.split("\n")
        return messages

    def extract_links(self, messages):
        url_pattern = r"(https?://\S+)"
        links = [re.findall(url_pattern, msg) for msg in messages]
        return [link for sublist in links for link in sublist]



