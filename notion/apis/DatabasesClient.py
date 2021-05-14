from notion.utils import pick
from notion.Client import Client, Method, RequestParameters
from notion.api_endpoints import (
    DatabasesList,
    DatabasesListParameters,
    DatabasesListResponse,
)
from notion.apis.ApiClient import ApiClient


class DatabasesClient(ApiClient):
    def __init__(self, client: Client):
        super().__init__(client)

    async def list(self, args: DatabasesListParameters = None) -> DatabasesListResponse:
        return await self.client.request(
            request_parameters=RequestParameters(
                path=DatabasesList.path,
                method=Method.GET.value,
                query=pick(args, DatabasesList.queryParams),
                body=pick(args, DatabasesList.bodyParams),
            )
        )

    async def retrieve(self, args):
        pass

    async def query(self, args):
        pass
