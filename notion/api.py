import requests


class Notion(object):
    API_ENDPOINT = "https://api.notion.com/v1"
    DEFAULT_NOTION_VERSION = "2021-05-13"
    HEADERS = {
        "Authorization": "",
        "Content-Type": "applicaton/json",
        "Notion-Version": DEFAULT_NOTION_VERSION,
    }

    def __init__(self, auth):
        self.auth = auth
        self.prepare_credentials()
        self.prepare_sessions()

    def prepare_credentials(self):
        self.HEADERS["Authorization"] = f"Bearer {self.auth}"

    def prepare_sessions(self):
        self.session = requests.Session()
        self.session.headers.update(self.HEADERS)

    def retrieve_database(self, database_id):
        url = f"{self.API_ENDPOINT}/databases/{database_id}"
        req = self.session.get(url)
        return req.json()

    def query_database(self, database_id, data):
        url = f"{self.API_ENDPOINT}/databases/{database_id}/query"
        req = self.session.post(url, data=data)
        return req.json()

    def list_databases(self, params):
        url = f"{self.API_ENDPOINT}/databases"
        req = self.session.get(url, params=params)
        return req.json()

    def retrieve_page(self, page_id):
        url = f"{self.API_ENDPOINT}/pages/{page_id}"
        req = self.session.get(url)
        return req.json()

    def create_page(self, data):
        url = f"{self.API_ENDPOINT}/pages"
        req = self.session.post(url, data=data)
        return req.json()

    def update_page(self, page_id, data):
        url = f"{self.API_ENDPOINT}/pages/{page_id}"
        req = self.session.patch(url, data=data)
        return req.json()

    def retrieve_block(self, block_id, params):
        url = f"{self.API_ENDPOINT}/blocks/{block_id}/children"
        req = self.session.get(url, params=params)
        return req.json()

    def append_block(self, block_id, data):
        url = f"{self.API_ENDPOINT}/blocks/{block_id}/children"
        req = self.session.patch(url, data=data)
        return req.json()

    def retrieve_user(self, user_id):
        url = f"{self.API_ENDPOINT}/users/{user_id}"
        req = self.session.get(url)
        return req.json()

    def list_users(self):
        url = f"{self.API_ENDPOINT}/users"
        req = self.session.get(url)
        return req.json()

    def search(self, data):
        url = f"{self.API_ENDPOINT}/search"
        req = self.session.post(url, data=data)
        return req.json()