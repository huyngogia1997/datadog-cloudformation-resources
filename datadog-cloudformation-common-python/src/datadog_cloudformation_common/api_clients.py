from contextlib import contextmanager

from datadog_api_client.v1 import ApiClient, Configuration


@contextmanager
def v1_client(api_key: str, app_key: str, api_url: str, resource_name: str, resource_version: str) -> ApiClient:
    configuration = Configuration(
        host=api_url,
        api_key={
            "apiKeyAuth": api_key,
            "appKeyAuth": app_key,
        }
    )

    # TODO: configure user-agent

    with ApiClient(configuration) as api_client:
        yield api_client
