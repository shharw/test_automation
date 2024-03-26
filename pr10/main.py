import requests
import allure

@allure.epic("Api testing")
class TestApi:
    base_url = 'https://reqres.in/api/users/'

    @allure.title("Get user")
    @allure.description("Getting user by id")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.feature("GET")
    def test_single_user(self):
        with allure.step("Step 1. Get base url"):
            url = f'{self.base_url}1'
        with allure.step("Step 2. Request"):
            res = requests.get(url)
        with allure.step("Step 3. Assert that status code should equal 200"):
            assert res.status_code == 200
        with allure.step("Step 4. Assert that content type should be application/json; charset=utf-8"):
            assert res.headers['Content-Type'] == 'application/json; charset=utf-8'
        with allure.step("Step 5. Convert response to json. Get data"):
            user = res.json()['data']
        with allure.step("Step 6. Assert that id exist"):
            assert 'id' in user
        with allure.step("Step 7. Assert that email exist"):
            assert 'email' in user

    @allure.title("Create user")
    @allure.description("Creating user")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.feature("POST")
    def test_create_user(self):
        with allure.step("Step 1. Get base url"):
            url = self.base_url
        with allure.step("Step 2. Set request payload"):
            data  = {
                "name": "test",
                "job": "test"
            }
        with allure.step("Step 3. Request"):
            res = requests.post(url, data)
        with allure.step("Step 4. Assert that status code should equal 201"):
            assert res.status_code == 201
        with allure.step("Step 5. Assert that content type should be application/json; charset=utf-8"):
            assert res.headers['Content-Type'] == 'application/json; charset=utf-8'
        with allure.step("Step 6. Convert response to json. Get data"):
            user = res.json()
        with allure.step("Step 7. Assert that user with new name exist"):
            assert data['name'] in user['name']
        with allure.step("Step 8. Assert that user with new job exist"):
            assert data['job'] in user['job']
    
    @allure.title("Update user")
    @allure.description("Updating user by id")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.feature("PUT")
    def test_update_user(self):
        with allure.step("Step 1. Get base url"):
            url = f'{self.base_url}2'
        with allure.step("Step 2. Set request payload"):
            data  = {
                "name": "test",
                "job": "test"
            }
        with allure.step("Step 3. Request"):
            res = requests.put(url, data)
        with allure.step("Step 4. Assert that status code should equal 200"):
            assert res.status_code == 200
        with allure.step("Step 5. Assert that content type should be application/json; charset=utf-8"):
            assert res.headers['Content-Type'] == 'application/json; charset=utf-8'
        with allure.step("Step 6. Convert response to json. Get data"):
            user = res.json()
        with allure.step("Step 7. Assert that name changed"):
            assert data['name'] in user['name']
        with allure.step("Step 8. Assert that job changed"):
            assert data['job'] in user['job']
    
    @allure.title("Delete user")
    @allure.description("Deleting user by id")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.feature("DELETE")
    def test_delete_user(self):
        with allure.step("Step 1. Get base url"):
            url = f'{self.base_url}2'
        with allure.step("Step 3. Request"):
            res = requests.delete(url)
        with allure.step("Step 4. Assert that status code should equal 204"):
            assert res.status_code == 204
        with allure.step("Step 5. Assert that response content empty"):
            assert res.content == b''
