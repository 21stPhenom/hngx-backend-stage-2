import requests

# endpoint = "https://hngx-task-2-ui07.onrender.com/api"
endpoint = "http://127.0.0.1:8000/api/"


def send_request(method: str, user_id: int=None, name: str=None, data: dict=None):
    if method == 'get':
        if user_id == None and name == None:
            response = requests.get(endpoint)
            return response
        elif name == None and user_id != None:
            assert type(user_id) == int, '`user_id` must be an integer.'
            endpoint_with_id = f"{endpoint}{user_id}"
            response = requests.get(endpoint_with_id)
            return response
        elif user_id == None and name != None:
            assert type(name) == str, '`name` must be a string.'
            endpoint_with_name = f"{endpoint}{name}"
            response = requests.get(endpoint_with_name)

            return response
        
    elif method == 'post':
        assert data != None and type(data) == dict, "`data` must be a non-empty dictionary."
        response = requests.post(endpoint, data=data)
        return response
    
    elif method == 'put':
        # assert user_id != None and type(user_id) == int, "pass a valid user_id."
        # assert data != None and type(data) == dict, "`data` can not be empty."

        if user_id == None and name == None:
            raise ValueError('You must pass a `user_id` or `name`.')
        elif user_id != None and type(user_id) != int:
            raise ValueError('`user_id` must be an integer.')
        elif name != None and type(name) != str:
            raise ValueError('`name` must be a string')
        else:
            assert data != None and type(data) == dict, "`data` can not be empty."

        if name == None and user_id != None:
            assert type(user_id) == int, '`user_id` must be an integer.'
            endpoint_with_id = f"{endpoint}{user_id}"
            response = requests.put(endpoint_with_id, data)
            return response
        
        elif user_id == None and name != None:
            assert type(name) == str, '`name` must be a string.'
            endpoint_with_name = f"{endpoint}{name}"
            response = requests.put(endpoint_with_name)

            return response
        
    elif method == 'delete':
        if name == None and user_id != None:
            assert type(user_id) == int, '`user_id` must be an integer.'
            endpoint_with_id = f"{endpoint}{user_id}"
            response = requests.delete(endpoint_with_id)
            return response
        
        elif user_id == None and name != None:
            assert type(name) == str, '`name` must be a string.'
            endpoint_with_name = f"{endpoint}{name}"
            response = requests.delete(endpoint_with_name)
            return response

# endpoint_1 = send_request('get')
# endpoint_2 = send_request('get', user_id=12)
# endpoint_3 = send_request('get', user_id=8)
# endpoint_4 = send_request('post', data={'name': 'benjamin'})
# endpoint_5 = send_request('put', user_id=12, data={"name": "einstein"})
endpoint_6 = send_request('delete', name='kodecamp')


# print(endpoint_1.json())
# print(endpoint_2.json())
# print(endpoint_3.json())
# print(endpoint_4.json())
# print(endpoint_5.json())
print(endpoint_6.text)