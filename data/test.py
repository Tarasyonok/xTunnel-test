from requests import get, post, delete, put


def test():
    # test_jobs_api()
    # test_users_api_v2()
    test_jobs_api_v2()


def test_jobs_api():
    print('*------------------------------*')

    print('GET Jobs API V1')
    print(get('http://localhost:5000/api/jobs').json())
    print(get('http://localhost:5000/api/jobs/2').json())
    print(get('http://localhost:5000/api/jobs/999').json())
    print(get('http://localhost:5000/api/jobs/asd').json())

    print('POST Jobs API V1')
    print(post('http://localhost:5000/api/jobs', json={}).json())
    print(post('http://localhost:5000/api/jobs', json={'job': 'Destroy enemy base'}).json())
    print(post('http://localhost:5000/api/jobs', json={
        'team_leader': 3,
        'job': 'Destroy enemy base',
        'work_size': 10,
        'collaborators': '2, 3',
        'is_finished': 0,
    }).json())

    print('DELETE Jobs API V1')
    print(delete('http://localhost:5000/api/jobs/3').json())
    print(delete('http://localhost:5000/api/jobs/999').json())
    print(delete('http://localhost:5000/api/jobs/asd').json())

    print('PUT Jobs API V1')
    print(put('http://localhost:5000/api/jobs/asd', json={}).json())
    print(put('http://localhost:5000/api/jobs/999', json={}).json())
    print(put('http://localhost:5000/api/jobs/999',  json={
        'team_leader': 1,
        'job': 'test 2 put',
        'work_size': 10,
        'collaborators': '1, 2',
        'is_finished': 0,
    }).json())
    print(put('http://localhost:5000/api/jobs/5',  json={}).json())
    print(put('http://localhost:5000/api/jobs/5',  json={'title': 'test put'}).json())
    print(put('http://localhost:5000/api/jobs/5',  json={
        'team_leader': 1,
        'job': 'test 2 put',
        'work_size': 10,
        'collaborators': '1, 2',
        'is_finished': 0,
    }).json())

def test_users_api_v2():
    print('*------------------------------*')

    print('GET User API V2')
    print(get('http://localhost:5000/api/v2/users').json())
    print(get('http://localhost:5000/api/v2/users/2').json())
    print(get('http://localhost:5000/api/v2/users/999').json())
    print(get('http://localhost:5000/api/v2/users/asd').json())

    print('POST User API V2')
    print(post('http://localhost:5000/api/v2/users', json={}).json())
    print(post('http://localhost:5000/api/v2/users', json={'job': 'Destroy enemy base'}).json())
    print(post('http://localhost:5000/api/v2/users', json={
        'surname': 'test',
        'name': 'test',
        'age': 1,
        'position': 'test',
        'speciality': 'test',
        'address': 'test',
        'email': 'test@test',
        'city_from': 'test',
        'password': 'test',
    }).json())

    print('DELETE User API V2')
    print(delete('http://localhost:5000/api/v2/users/6').json())
    print(delete('http://localhost:5000/api/v2/users/999').json())
    print(delete('http://localhost:5000/api/v2/users/asd').json())


    print(post('http://localhost:5000/api/v2/users', json={
        'surname': 'test',
        'name': 'test',
        'age': 1,
        'position': 'test',
        'speciality': 'test',
        'address': 'test',
        'email': 'test@test',
        'city_from': 'test',
        'password': 'test',
    }).json())


    print('PUT User API V2')
    print(put('http://localhost:5000/api/v2/users/asd', json={}).json())
    print(put('http://localhost:5000/api/v2/users/999', json={}).json())
    print(put('http://localhost:5000/api/v2/users/999',  json={
        'surname': 'test',
        'name': 'test',
        'age': 1,
        'position': 'test',
        'speciality': 'test',
        'address': 'test',
        'email': 'test@test',
        'city_from': 'test',
        'password': 'test',
    }).json())
    print(put('http://localhost:5000/api/v2/users/6',  json={}).json())
    print(put('http://localhost:5000/api/v2/users/6',  json={'title': 'test put'}).json())
    print(put('http://localhost:5000/api/v2/users/6',  json={
        'surname': 'test',
        'name': 'test',
        'age': 1,
        'position': 'test',
        'speciality': 'test',
        'address': 'test',
        'email': 'test@test',
        'city_from': 'test',
        'password': 'test',
    }).json())


def test_jobs_api_v2():
    print('*------------------------------*')

    # print('GET Job API V2')
    # print(get('http://localhost:5000/api/v2/jobs').json())
    # print(get('http://localhost:5000/api/v2/jobs/2').json())
    # print(get('http://localhost:5000/api/v2/jobs/999').json())
    # print(get('http://localhost:5000/api/v2/jobs/asd').json())
    #
    # print('POST Job API V2')
    # print(post('http://localhost:5000/api/v2/jobs', json={}).json())
    # print(post('http://localhost:5000/api/v2/jobs', json={'job': 'Destroy enemy base'}).json())
    # print(post('http://localhost:5000/api/v2/jobs', json={
    #     'team_leader': 3,
    #     'job': 'Destroy enemy base',
    #     'work_size': 10,
    #     'collaborators': '2, 3',
    #     'is_finished': 0,
    # }).json())
    #
    # print('DELETE Job API V2')
    # print(delete('http://localhost:5000/api/v2/jobs/3').json())
    # print(delete('http://localhost:5000/api/v2/jobs/999').json())
    # print(delete('http://localhost:5000/api/v2/jobs/asd').json())
    #
    # print(post('http://localhost:5000/api/v2/jobs', json={
    #     'team_leader': 3,
    #     'job': 'Destroy enemy base',
    #     'work_size': 10,
    #     'collaborators': '2, 3',
    #     'is_finished': 0,
    # }).json())

    print('PUT Job API V2')
    print(put('http://localhost:5000/api/v2/jobs/asd', json={}).json())
    print(put('http://localhost:5000/api/v2/jobs/999', json={}).json())
    print(put('http://localhost:5000/api/v2/jobs/999',  json={
        'team_leader': 1,
        'job': 'test 2 put',
        'work_size': 10,
        'collaborators': '1, 2',
        'is_finished': 0,
    }).json())
    print(put('http://localhost:5000/api/v2/jobs/2',  json={}).json())
    print(put('http://localhost:5000/api/v2/jobs/2',  json={'title': 'test put'}).json())
    print(put('http://localhost:5000/api/v2/jobs/2',  json={
        'team_leader': 1,
        'job': 'test 2 put',
        'work_size': 10,
        'collaborators': '1, 2',
        'is_finished': 0,
    }).json())


test()