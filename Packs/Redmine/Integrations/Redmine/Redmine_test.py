import pytest
from Redmine import Client
from requests.models import Response

@pytest.fixture
def redmine_client(url: str = 'url', verify_certificate: bool = True, proxy: bool = False, auth=('username', 'password')):
    return Client(url, verify_certificate, proxy, auth=auth)


''' COMMAND FUNCTIONS TESTS '''

def test_create_issue_command_without_file(mocker, redmine_client):
    """
    Given:
        - All relevant arguments for the command that is executed
    When:
        - redmine-issue-create command is executed
    Then:
        - The http request is called with the right arguments
    """
    from Redmine import create_issue_command
    http_request = mocker.patch.object(redmine_client, '_http_request')
    args = {'status_id': '1', 'priority_id': '1', 'subject': 'newSubject', 'project_id': '1'}
    create_issue_command(redmine_client, args=args)
    http_request.assert_called_with('POST', '/issues.json', params={'status_id': '1', 'priority_id': '1', 'project_id': '1'},
                                    json_data={'issue': {'subject': 'newSubject'}}, headers={'Content-Type': 'application/json'})


def test_create_issue_command_with_file(mocker, redmine_client):
    """
    Given:
        - All relevant arguments for the command that is executed
    When:
        - redmine-issue-create command is executed
    Then:
        - The http request is called with the right arguments
    """
    from Redmine import create_issue_command
    create_file_token_request_mock = mocker.patch.object(redmine_client, 'create_file_token_request')
    create_file_token_request_mock.return_value = {'upload': {'token': 'token123'}}
    http_request = mocker.patch.object(redmine_client, '_http_request')
    args = {'file_entry_id': '9@klmlqm', 'status_id': '1', 'priority_id': '1', 'subject': 'newSubject', 'project_id': '1'}
    create_issue_command(redmine_client, args=args)
    create_file_token_request_mock.assert_called_with({}, '9@klmlqm')
    http_request.assert_called_with('POST', '/issues.json',
                                    params={'status_id': '1', 'priority_id': '1', 'project_id': '1'},
                                    json_data={'issue': {'subject': 'newSubject', 'uploads': [{'token': 'token123'}]}},
                                    headers={'Content-Type': 'application/json'})

def test_create_issue_command_missing_status_id(redmine_client):
    """
    Given:
        - All relevant arguments for the command that is executed
    When:
        - redmine-issue-create command is executed
    Then:
        - The http request is called with the right arguments
    """
    from Redmine import create_issue_command
    from CommonServerPython import DemistoException
    args = {}
    with pytest.raises(DemistoException) as e:
        create_issue_command(redmine_client, args)
    assert e.value.message == 'One or more required arguments not specified: status_id, priority_id, subject, project_id'
    
def test_create_issue_command_failed_to_create_file_token(mocker, redmine_client):
    """
    Given:
        - All relevant arguments for the command that is executed
    When:
        - redmine-issue-create command is executed
    Then:
        - The http request is called with the right arguments
    """
    from Redmine import create_issue_command
    create_file_token_request_mock = mocker.patch.object(redmine_client, 'create_file_token_request')
    from CommonServerPython import DemistoException
    args = {'project_id': '2','status_id': '1', 'priority_id': '1', 'subject': 'newSubject', 'file_entry_id':'9@klmlqm'}
    create_file_token_request_mock.return_value = {}
    with pytest.raises(DemistoException) as e:
        create_issue_command(redmine_client, args)
    assert str(e.value) == "Could not upload file with entry id 9@klmlqm"
    
def test_update_issue_command(mocker, redmine_client):
    """
    Given:
        - All relevant arguments for the command that is executed without list id
    When:
        - redmine-issue-update command is executed
    Then:
        - The http request is called with the right arguments
    """
    from Redmine import update_issue_command
    http_request = mocker.patch.object(redmine_client, '_http_request')
    args = {'issue_id': '1', 'subject': 'changeFromCode', 'tracker_id': '1', 'watcher_user_ids': '[1]'}
    update_issue_command(redmine_client, args=args)
    http_request.assert_called_with('PUT', '/issues/1.json', json_data={'issue': {'subject': 'changeFromCode',
                                                                                  'tracker_id': '1', 'watcher_user_ids': '[1]'}}, headers={'Content-Type': 'application/json'})
def test_update_issue_command_invalid_tracker_id(redmine_client):
    from Redmine import update_issue_command
    from CommonServerPython import DemistoException
    args = {'issue_id': '1', 'subject': 'testSub', 'tracker_id': 'blb', 'watcher_user_ids': '[1]', 'status_id':'New'}
    with pytest.raises(DemistoException) as e:
        update_issue_command(redmine_client, args)
    assert e.value.message == "Tracker_id invalid, please make you used only predefined values"
    

def test_update_issue_command_invalid_status_id(redmine_client):
    from Redmine import update_issue_command
    from CommonServerPython import DemistoException
    args = {'issue_id': '1', 'subject': 'testSub', 'tracker_id': 'Bug', 'watcher_user_ids': '[1]', 'status_id':'khbk',
            'priority_id':'high'}
    with pytest.raises(DemistoException) as e:
        update_issue_command(redmine_client, args)
    assert e.value.message == "Status_id invalid, please make you used only predefined values"

def test_update_issue_command_invalid_priority_id(redmine_client):
    from Redmine import update_issue_command
    from CommonServerPython import DemistoException
    args = {'issue_id': '1', 'subject': 'testSub', 'tracker_id': 'Bug', 'watcher_user_ids': '[1]', 'status_id':'New',
            'priority_id':'jbnl'}
    with pytest.raises(DemistoException) as e:
        update_issue_command(redmine_client, args)
    assert e.value.message == "Priority_id invalid, please make you used only predefined values"

def test_update_issue_command_invalid_custom_fields(redmine_client):
    from Redmine import update_issue_command
    from CommonServerPython import DemistoException
    args = {'custom_fields':'jnlnj', 'issue_id': '1', 'subject': 'testSub', 'tracker_id': 'Bug', 'watcher_user_ids': '[1]',
            'status_id':'New', 'priority_id':'High'}
    with pytest.raises(DemistoException) as e:
        update_issue_command(redmine_client, args)
    assert e.value.message == "Custom fields not in format, please follow the instructions"

def test_update_issue_command_no_token_created_for_file(mocker, redmine_client):
    """
    Given:
        - All relevant arguments for the command that is executed
    When:
        - redmine-issue-delete command is executed
    Then:
        - The http request is called with the right arguments
    """
    from Redmine import update_issue_command
    from CommonServerPython import DemistoException
    create_file_token_request_mock = mocker.patch.object(redmine_client, 'create_file_token_request')
    create_file_token_request_mock.return_value = {'token': 'token123'}
    args = {'status_id':'New','file_entry_id': 'a.png', 'issue_id': '1', 'subject': 'testSub', 'tracker_id': 'Bug', 'watcher_user_ids': '[1]'}
    with pytest.raises(DemistoException) as e:
        update_issue_command(redmine_client, args)
        create_file_token_request_mock.assert_called_with({}, 'a.png')
    assert e.value.message == "Failed to execute redmine-issue-update command. Couldn't create file token for the file you are trying to upload. with error: 'upload'"
    
def test_update_issue_command_with_file(mocker, redmine_client):
    """
    Given:
        - All relevant arguments for the command that is executed without list id
    When:
        - redmine-issue-update command is executed
    Then:
        - The http request is called with the right arguments
    """
    from Redmine import update_issue_command
    http_request = mocker.patch.object(redmine_client, '_http_request')
    create_file_token_request_mock = mocker.patch.object(redmine_client, 'create_file_token_request')
    create_file_token_request_mock.return_value = {'upload': {'token': 'token123'}}
    args = {'file_entry_id': 'a.png', 'issue_id': '1', 'subject': 'testSub', 'tracker_id': 'Bug', 'watcher_user_ids': '[1]'}
    update_issue_command(redmine_client, args=args)
    create_file_token_request_mock.assert_called_with({}, 'a.png')
    http_request.assert_called_with('PUT', '/issues/1.json', json_data={'issue': {'subject': 'testSub',
                                    'watcher_user_ids': '[1]', 'tracker_id': '1', 'uploads':
                                    [{'token': 'token123', 'filename': '', 'description': '', 'content_type': ''}]}},
                                    headers={'Content-Type': 'application/json', 'X-Redmine-API-Key': True},
                                    empty_valid_codes=[204], return_empty_response=True)

def test_get_issues_list_command(mocker, redmine_client):
    """
    Given:
        - All relevant arguments for the command that is executed with asset id
    When:
        - redmine-issue-list command is executed
    Then:
        - The http request is called with the right arguments
    """
    from Redmine import get_issues_list_command
    http_request = mocker.patch.object(redmine_client, '_http_request')
    args = {'sort': 'priority:desc', 'limit': '1'}
    get_issues_list_command(redmine_client, args)
    http_request.assert_called_with('GET', '/issues.json', params={'offset': 0, 'limit': 1, 'sort': 'priority:desc'},
                                    headers={'X-Redmine-API-Key': True})
    
def test_get_issues_list_command_invalid_status(mocker, redmine_client):
    """
    Given:
        - All relevant arguments for the command that is executed with asset id
    When:
        - redmine-issue-list command is executed
    Then:
        - The http request is called with the right arguments
    """
    from Redmine import get_issues_list_command
    from CommonServerPython import DemistoException
    with pytest.raises(DemistoException) as e:
        get_issues_list_command(redmine_client, {'status_id':'hhjuhkk'})
    assert e.value.message == "Invalid status ID, please use only predefined values"

    
def test_get_issue_by_id_command(mocker, redmine_client):
    """
    Given:
        - All relevant arguments for the command that is executed without asset id
    When:
        - redmine-issue-show command is executed
    Then:
        - The http request is called with the right arguments
    """
    from Redmine import get_issue_by_id_command
    http_request = mocker.patch.object(redmine_client, '_http_request')
    args = {'issue_id': '1', 'include': 'watchers,attachments'}
    get_issue_by_id_command(redmine_client, args)
    http_request.assert_called_with('GET', '/issues/1.json', params={'include': 'watchers,attachments'},
                                    headers={'Content-Type': 'application/json', 'X-Redmine-API-Key': True})
    
def test_get_issue_by_id_command_invalid_include_argument(mocker, redmine_client):
    """
    Given:
        - All relevant arguments for the command that is executed
    When:
        - redmine-issue-show command is executed
    Then:
        - No issue id raises a DemistoException
    """
    from Redmine import get_issue_by_id_command
    from CommonServerPython import DemistoException
    args = {'sort': 'priority:desc', 'limit': '1', 'include':'beikbfqi'}
    with pytest.raises(DemistoException) as e:
        get_issue_by_id_command(redmine_client, args)
    assert e.value.message == "You can only include the following values: 'changesets', 'children', 'attachments', 'journals', 'relations', 'watchers', 'allowed_statuses'}, separated with comma"

def test_delete_issue_by_id_command(mocker, redmine_client):
    """
    Given:
        - All relevant arguments for the command that is executed
    When:
        - redmine-issue-delete command is executed
    Then:
        - The http request is called with the right arguments
    """
    from Redmine import delete_issue_by_id_command
    http_request = mocker.patch.object(redmine_client, '_http_request')
    args = {'issue_id': '41'}
    delete_issue_by_id_command(redmine_client, args)
    http_request.assert_called_with('DELETE', '/issues/41.json', headers={'Content-Type': 'application/json',
                                    'X-Redmine-API-Key': True}, empty_valid_codes=[200, 204, 201], return_empty_response=True)

def test_add_issue_watcher_command(mocker, redmine_client):
    """
    Given:
        - All relevant arguments for the command that is executed
    When:
        - redmine-issue-watcher-add command is executed
    Then:
        - The http request is called with the right arguments
    """
    from Redmine import add_issue_watcher_command
    http_request = mocker.patch.object(redmine_client, '_http_request')
    args = {'issue_id': '1', 'watcher_id': '1'}
    add_issue_watcher_command(redmine_client, args)
    http_request.assert_called_with('POST', '/issues/1/watchers.json', params={'user_id': '1'},
                                    headers={'Content-Type': 'application/json', 'X-Redmine-API-Key': True},
                                    empty_valid_codes=[200, 204, 201], return_empty_response=True)
   
def test_remove_issue_watcher_command(mocker, redmine_client):
    """
    Given:
        - All relevant arguments for the command that is executed
    When:
        - redmine-issue-watcher-remove command is executed
    Then:
        - The http request is called with the right arguments
    """
    from Redmine import remove_issue_watcher_command
    http_request = mocker.patch.object(redmine_client, '_http_request')
    args = {'issue_id': '1', 'watcher_id': '1'}
    remove_issue_watcher_command(redmine_client, args)
    http_request.assert_called_with('DELETE', '/issues/1/watchers/1.json', headers={'Content-Type': 'application/json',
                                                                                    'X-Redmine-API-Key': True},
                                    empty_valid_codes=[200, 204, 201], return_empty_response=True)
    
def test_remove_issue_watcher_command_invalid_status_id(mocker, redmine_client):
    """
    Given:
        - All relevant arguments for the command that is executed
    When:
        - redmine-issue-watcher-remove command is executed
    Then:
        - No issue id raises a DemistoException
    """
    from Redmine import remove_issue_watcher_command
    from CommonServerPython import DemistoException
    args = {'issue_id': '1', 'watcher_id': '-20'}
    http_request = mocker.patch.object(redmine_client, '_http_request')
    http_request.side_effect = DemistoException("Invalid ID for one or more fields that request IDs. Please make sure all IDs are correct.")
    with pytest.raises(DemistoException) as e:
        remove_issue_watcher_command(redmine_client, args)
    assert e.value.message == "Invalid ID for one or more fields that request IDs. Please make sure all IDs are correct."

def test_get_project_list_command(mocker, redmine_client):
    """
    Given:
        - All relevant arguments for the command that is executed
    When:
        - redmine-project-list command is executed
    Then:
        - The http request is called with the right arguments
    """
    from Redmine import get_project_list_command
    http_request = mocker.patch.object(redmine_client, '_http_request')
    args = {'include': 'time_entry_activities'}
    get_project_list_command(redmine_client, args)
    http_request.assert_called_with('GET', '/projects.json', params={'include': 'time_entry_activities'},
                                    headers={'X-Redmine-API-Key': True})

def test_get_project_list_command_invalid_include(redmine_client):
    """
    Given:
        - All relevant arguments for the command that is executed
    When:
        - redmine-issue-watcher-remove command is executed
    Then:
        - No issue id raises a DemistoException
    """
    from Redmine import get_project_list_command
    from CommonServerPython import DemistoException
    args = {'include': 'time_entry_activities,jissue_categories'}
    with pytest.raises(DemistoException) as e:
        get_project_list_command(redmine_client, args)
    assert e.value.message == "The 'include' argument should only contain values from trackers/issue_categories/enabled_modules/time_entry_activities/issue_custom_fields, separated by commas. These values are not in options ['jissue_categories']"

def test_get_custom_fields_command(mocker, redmine_client):
    """
    Given:
        - All relevant arguments for the command that is executed
    When:
        - redmine-custom-field-list command is executed
    Then:
        - The http request is called with the right arguments
    """
    from Redmine import get_custom_fields_command
    http_request = mocker.patch.object(redmine_client, '_http_request')
    get_custom_fields_command(redmine_client, {})
    http_request.assert_called_with('GET', '/custom_fields.json', headers={'X-Redmine-API-Key': True})
    
def test_get_users_command(mocker, redmine_client):
    """
    Given:
        - All relevant arguments for the command that is executed
    When:
        - redmine-user-id-list command is executed
    Then:
        - The http request is called with the right arguments
    """
    from Redmine import get_users_command
    http_request = mocker.patch.object(redmine_client, '_http_request')
    get_users_command(redmine_client, {'status': 'Active'})
    http_request.assert_called_with('GET', '/users.json', params={'status': '1'}, headers={'X-Redmine-API-Key': True})

def test_get_users_command_status_invalid(mocker, redmine_client):
    """
    Given:
        - All relevant arguments for the command that is executed
    When:
        - redmine-user-id-list command is executed
    Then:
        - The http request is called with the right arguments
    """
    from Redmine import get_users_command
    from CommonServerPython import DemistoException
    with pytest.raises(DemistoException) as e:
        get_users_command(redmine_client, {'status': 'hbvkbk'})
    assert e.value.message == "Invalid status value- please use the predefined options only"

''' HELPER FUNCTIONS TESTS '''

@pytest.mark.parametrize('page_size, page_number, expected_output',
                         [(1, 10, '#### Showing 1 results from page 10:\n')])
def test_create_paging_header(page_size, page_number, expected_output):
    """
    Given:
        - All relevant arguments for the command that is executed
    When:
        - redmine-user-id-list command is executed
    Then:
        - The http request is called with the right arguments
    """
    from Redmine import create_paging_header
    assert create_paging_header(page_size, page_number) == expected_output
    
@pytest.mark.parametrize('args, expected_output',
                         [({'page_number':'2','page_size':'20'}, '20, 20, 2')])
def test_adjust_paging_to_request(args, expected_output):
    """
    Given:
        - All relevant arguments for the command that is executed
    When:
        - adjust_paging_to_request function is executed
    Then:
        - The http request is called with the right arguments
    """
    expected_output = expected_output.split(', ')
    from Redmine import adjust_paging_to_request
    assert adjust_paging_to_request(args) == (int(expected_output[0]), int(expected_output[1]), int(expected_output[2]))
    
@pytest.mark.parametrize('header_name, expected_output',
                         [('id', '#### Showing 1 results from page 10:\n')])
def test_map_header(header_name, expected_output):
    """
    Given:
        - All relevant arguments for the command that is executed
    When:
        - map_header command is executed
    Then:
        - The header is being converted
    """
    from Redmine import map_header
    assert map_header(header_name) == 'ID'

def test_convert_args_to_request_format():
    """
    Given:
        - All relevant arguments for the command that is executed
    When:
        - convert_args_to_request_format command is executed
    Then:
        - The key or value is being converted
    """
    from Redmine import convert_args_to_request_format
    convert_args_to_request_format({'watcher_user_ids':'1,2,3'})