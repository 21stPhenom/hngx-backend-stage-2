# hngx-backend-stage-2 CRUD API documentation
#### This API allows users to perform CRUD on a `person` resource.

> CRUD means Create, Read, Update, Delete. This API lets users create a `person` object and store it in the database, read a `person` object from the database, update a `person` in the database and delete a `person`.

---

### Table of Contents
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Testing](#testing)

### Usage
- In order to use this API, refer to the [setup process](./README.md) in the README file for proper setup instructions.
- Once you have completed the steps and your server is running on `http://127.0.0.1:8000/`, your good to go.

### API Endpoints
1. Create person:
    - Endpoint: `api/`
    - Method: `POST`
    - Body: `{"name": "enoch"}`
   
    - Response (with unique name):
        - Status code: `201`
    ```json
    {
        "id": 1,
        "name": "enoch"
    }
    ```

    - Response (if person with name 'enoch' already exists):
        - Status code: `400`
    ```json
    {
        "message": "Person with name `enoch` already exists."
    }
    ```
    > [!NOTE]
    > The value of `name` in the must be unique i.e it should not be a name that's already in the database. This also applies to the updating a person.

2. Get persons:
    - Endpoint: `api/`
    - Method: `GET`
    - Example: `GET http://127.0.0.1:8000/api/`
    
    - Response (success):
        - Status code: `200`
    ```json
    [
        {
            "id": 1,
            "name": "enoch"
        },
    ]
    ```
    
    - Response (not found):
        - Status code: `404`
    ```json
    {
        "detail": "Not found."
    }
    ```
3. Get specific person:
    - Endpoint: `api/user_id` or `api/name`
    - Method: `GET`
    - Example: `GET http://127.0.0.1:8000/api/1` or `GET http://127.0.0.1:8000/api/enoch`
  
    - Response (person found):
        - Status code: `200`
    ```json
    {
        "id": 1,
        "name": "enoch"
    }
    ```
    - Response (not found):
        - Status code: `404`
    ```json
    {
        "detail": "Not found."
    }
    ```

4. Update person:
    - Endpoint: `api/user_id` or `api/name`
    - Method: `PUT`
    - Body: `{"name": "isaac"}`
    - Example: `PUT http://127.0.0.1:8000/api/1` or `PUT http://127.0.0.1:8000/api/enoch`
  
    - Response (person updated):
        - Status code: `200`
    ```json
    {
        "id": 1,
        "name": "isaac"
    }
    ```

    - Response (if person with name 'enoch' already exists):
        - Status code: `400`
    ```json
    {
        "message": "Person with name `enoch` already exists."
    }
    ```

    - Response (person not found):
        - Status code: `404`
    ```json
    {
        "detail": "Not found."
    }
    ```

5. Delete person:
    - Endpoint: `api/user_id` or `api/name`
    - Method: `DELETE`
    - Example: `DELETE http://127.0.0.1:8000/api/1` or `DELETE http://127.0.0.1:8000/api/enoch`
    
    - Response:
        - Status code: `200`
    ```json
    {
        "message": "Person deleted"
    }
    ```

    - Response (person not found):
        - Status code: `404`
    ```json
    {
        "detail": "Not found."
    }
    ```
---
### Testing
- To test your API, run `tester.py` in your virtual environment.
```
python tester.py
```
- The script sends some requests to the endpoints on the server and prints the responses in JSON format