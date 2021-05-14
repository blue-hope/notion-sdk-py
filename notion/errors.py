class RequestTimeoutError(Exception):
    code = "notionhq_client_request_timeout"

    def __init__(self, message="Request to Notion API has timed out"):
        super(message)
        self.name = "RequestTimeoutError"

    @staticmethod
    def is_request_timeout_error(e: Exception) -> bool:
        return (
            isinstance(e, Exception)
            and e.name == "RequestTimeoutError"
            and "code" in e
            and e["code"] == RequestTimeoutError.code
        )


def build_request_error(e: Exception):
    if is_timeout_error(e):
        return RequestTimeoutError()
    if is_http_error(e):
        api_error_response_body = parse_api_error_response_body(e.response.body)


def is_timeout_error(e: Exception) -> bool:
    return (
        isinstance(e, Exception)
        and e.name == "TimeoutError"
        and "event" in e
        and type(e["event"]) == "string"
        and isinstance(e["request"], dict)
        and isinstance(e["timings"], dict)
    )


def is_http_error(e: Exception) -> bool:
    return (
        isinstance(e, Exception)
        and e.name == "HTTPError"
        and "request" in e
        and "response" in e
        and "timings" in e
        and isinstance(e["request"], dict)
        and isinstance(e["response"], dict)
        and isinstance(e["timings"], dict)
    )
