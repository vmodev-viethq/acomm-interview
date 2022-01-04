from . import client

msg_successful = 'Frog can jump'
msg_unccessful = 'Frog cannot jump'


def test_jump_successful_1(client):
    body = {
        "leave_lists": [1, 2, 3, 4, 5],
        "river_length": 5
    }
    res = client.post('/', json=body)
    result = res.get_json()
    jump_at = 4
    assert result['msg'] == msg_successful
    assert result['jump_at'] == jump_at


def test_jump_successful_2(client):
    body = {
        "leave_lists": [1, 3, 1, 4, 2, 3, 5, 4],
        "river_length": 5
    }
    res = client.post('/', json=body)
    result = res.get_json()
    jump_at = 6
    assert result['msg'] == msg_successful
    assert result['jump_at'] == jump_at


def test_jump_unsuccessful_1(client):
    body = {
        "leave_lists": [1, 3, 1, 4, 2, 3, 4],
        "river_length": 5
    }
    res = client.post('/', json=body)
    result = res.get_json()
    jump_at = -1
    assert result['msg'] == msg_unccessful
    assert result['jump_at'] == jump_at


def test_jump_unsuccessful_2(client):
    body = {
        "leave_lists": [1, 1, 1, 1],
        "river_length": 4
    }
    res = client.post('/', json=body)
    result = res.get_json()
    jump_at = -1
    assert result['msg'] == msg_unccessful
    assert result['jump_at'] == jump_at


def test_invalid_leave_lists_1(client):
    body = {
        "leave_lists": 1,
        "river_length": 5
    }
    res = client.post('/', json=body)
    result = res.get_json()
    assert res.status_code == 400
    assert 'Not a valid list.' in result['message']['leave_lists']


def test_invalid_leave_lists_2(client):
    body = {
        'leave_lists': [1, 2, 8],
        'river_length': 3
    }
    res = client.post('/', json=body)
    result = res.get_json()
    assert res.status_code == 400
    assert 'Leave position cannot exceed river length' in result['message']['leave_lists']


def test_invalid_river_length_1(client):
    body = {
        'leave_lists': [1, 2, 8],
        'river_length': 100001
    }
    res = client.post('/', json=body)
    result = res.get_json()
    assert res.status_code == 400
    assert 'Value must be less than 100000' in result['message']['river_length']


def test_invalid_river_length_2(client):
    body = {
        'leave_lists': [1, 2, 8],
        'river_length': -1
    }
    res = client.post('/', json=body)
    result = res.get_json()
    assert res.status_code == 400
    assert 'Value must be more than 0' in result['message']['river_length']
