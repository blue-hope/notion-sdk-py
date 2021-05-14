from notion.Client import Client


class ApiClient:
    def __init__(self, client: Client):
        self.client = client
