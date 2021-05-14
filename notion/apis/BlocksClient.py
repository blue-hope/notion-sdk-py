from notion.apis.ApiClient import ApiClient


class BlocksClient(ApiClient):
    def __init__(self, client):
        super().__init__(client)

    @property
    def children(self):
        return ChildrenClient(self.client)


class ChildrenClient(ApiClient):
    def __init__(self, client):
        super().__init__(client)

    async def append(self, args):
        pass

    async def list(self, args):
        pass
