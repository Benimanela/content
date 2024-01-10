import json
from GitGuardianEventCollector import get_events, fetch_events
import demistomock as demisto
import pytest


def util_load_json(path):
    with open(path, encoding="utf-8") as f:
        return json.loads(f.read())


def http_mock(method: str, url_suffix: str = "", full_url: str = "", params: dict = {}):
    if url_suffix == "/secrets" or full_url.endswith("/secrets"):
        return util_load_json("test_data/incident_response.json")
    else:
        return util_load_json("test_data/audit_log_response.json")


@pytest.fixture(autouse=True)
def client(mocker):
    from GitGuardianEventCollector import Client

    headers = {"Authorization": "Token mock"}
    mocker.patch.object(Client, "_http_request", side_effect=http_mock)
    return Client(
        base_url="https://mock.gitguardian.com",
        verify=False,
        proxy=False,
        headers=headers,
    )


def test_get_events_command_limit(client):
    """
    Given: A mock GitGuardian client.
    When: Running get_events with a limit of 1, while there are two events.
    Then: Ensure only one event of each type is returned.
    """

    mock_args = {"limit": "1"}
    incidents, audit_logs, _ = get_events(client=client, args=mock_args)
    assert len(incidents) == 1
    assert len(audit_logs) == 1


def test_search_incidents(client):
    """
    Given: A mock GitGuardian client.
    When: Running search_incidents with a limit of 1
    Then: Ensure only one event is returned.
    """

    max_events_per_fetch = 1
    from_fetch_time = "2024-01-03T21:10:40Z"
    incidents, next_run_incidents_from_fetch = client.search_incidents(
        from_fetch_time, max_events_per_fetch
    )
    assert len(incidents) == 1
    assert next_run_incidents_from_fetch == "2024-01-03T21:10:42.679524Z"


def test_search_audit_log(client):
    """
    Given: A mock GitGuardian client.
    When: Running search_incidents with a limit of 1, while there are two events.
    Then: Ensure only one event is returned.
    """

    max_events_per_fetch = 1
    from_fetch_time = "2024-01-09T12:24:30Z"
    incidents, next_run_incidents_from_fetch = client.search_audit_logs(
        from_fetch_time, max_events_per_fetch
    )
    assert len(incidents) == 1
    assert next_run_incidents_from_fetch == "2024-01-09T12:24:40.089758Z"


def test_get_last_page(client):
    """
    Given: A mock GitGuardian client.
    When: Running get_last_page.
    Then: Ensure when there is only one page, the last page number is 1 and not 0
    """

    params = {}
    url_suffix = "/audit_logs"
    number_of_last_page = client.get_last_page(params, url_suffix)
    assert number_of_last_page == 1


def test_alter_next_fetch_time(client):
    """
    Given: A mock GitGuardian client.
    When: Running alter_next_fetch_time.
    Then: Ensure the time is incremented by 1 milisecond
    """

    time_str_to_alter = "2024-01-08T18:12:15.035562Z"
    next_fetch_time = client.alter_next_fetch_time(time_str_to_alter)
    assert next_fetch_time == "2024-01-08T18:12:15.035563Z"


def test_fetch_events(client):
    """
    Given: A mock GitGuardian client.
    When: Running fetch_events with a limit of 3
    Then: Ensure all of the events are returned, and the next run include the new fetch times.
    """

    max_events_per_fetch = 3
    last_run = {
        "incident_from_fetch_time": "2024-01-03T21:10:40Z",
        "audit_log_from_fetch_time": "2024-01-03T21:10:40Z",
    }

    next_run, incidents, audit_logs = fetch_events(
        client, last_run, max_events_per_fetch
    )
    assert len(incidents) == 2
    assert len(audit_logs) == 1
    assert next_run.get("incident_from_fetch_time") == "2024-01-08T19:04:02.270567Z"
    assert next_run.get("audit_log_from_fetch_time") == "2024-01-09T12:24:40.089758Z"
