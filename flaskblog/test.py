try:
    from run import app
    from flaskblog import db, mail
    import os
    import unittest
    import requests
    from flaskblog.users.forms import RegistrationForm, LoginForm
except Exception as e:
    print("Some modules are missing {}".format(e))


TEST_DB = 'user.db'


url = "http://127.0.0.1:5000/"
data = {
        'username': "abc",
        'email': "abc@smail.com",
        'password': 'abc',
        'confirm_password': 'abc'
    }

update_acc = {
        'email': "abc@smail.com",
        'password': 'abc',
        'picture': 'default.jpg'
    }
reset = {
        'email': 'abc@smail.com'
}

reset_data = {
        'password': 'abc',
        'confirm_password': 'abc'
}


class FlaskTest(unittest.TestCase):
    from flaskblog.users.routes import register

    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
        self.app = app.test_client()

        mail.init_app(app)
        self.assertEqual(app.debug, False)

    # executed after each test
    def tearDown(self):
        pass

    # # check response is 200
    # def test_home(self):
    #     tester = app.test_client(self)
    #     resp = tester.get("/home")
    #     self.assertEqual(resp.status_code, 200)
    #
    # # check if content return is application/html
    # def test_home_content(self):
    #     tester = app.test_client(self)
    #     resp = tester.get("/home")
    #     self.assertEqual(resp.content_type, "text/html; charset=utf-8")
    #
    # def test_about(self):
    #     tester = app.test_client(self)
    #     resp = tester.get("/about")
    #     self.assertEqual(resp.status_code, 200)
    #
    # # check if content return is application/html
    # def test_about_content(self):
    #     tester = app.test_client(self)
    #     resp = tester.get("/about")
    #     self.assertEqual(resp.content_type, "text/html; charset=utf-8")
    #
    # def test_post(self):
    #     tester = app.test_client(self)
    #     resp = tester.get("/post")
    #     self.assertEqual(resp.content_type, 'text/html; charset=utf-8')
# users apis
    def test_register_page(self):
        r = requests.get(f'{url}/register')
        self.assertEqual(r.status_code, 200)

    def test_login_page(self):
        r = requests.get(f'{url}/login')
        self.assertEqual(r.status_code, 200)

    def test_register(self):
        res = requests.post(f'{url}/register', json=data)
        self.assertEqual(res.status_code, 200)

    def test_login(self):
        res = requests.post(f'{url}/login', json=data)
        self.assertEqual(res.status_code, 200)

    def test_logout(self):
        res = requests.get(f'{url}/home')
        self.assertEqual(res.status_code, 200)

    def test_account(self):
        res = requests.get(f'{url}/account')
        self.assertEqual(res.status_code, 200)

    def test_update_account(self):
        res = requests.post(f'{url}/account', json=update_acc)
        self.assertEqual(res.status_code, 200)

# posts apis
    def test_post(self):
        res = requests.get(f'{url}/post/new', json=update_acc)
        self.assertEqual(res.status_code, 200)


if __name__ == '__main__':
    unittest.main()
