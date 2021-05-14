from notion.apis.ApiClient import ApiClient


class UsersClient(ApiClient):
    def __init__(self, client):
        super().__init__(client)

    async def retrieve(self, args):
        pass

    async def list(self, args):
        pass
