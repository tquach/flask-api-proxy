import unittest
import flask_proxy
import requests


class FlaskApiProxy(unittest.TestCase):

    def setUp(self):
        flask_proxy.app.config['TESTING'] = True
        self.app = flask_proxy.app.test_client()

    def test_should_route_to_index(self):
        rv = self.app.get('/?tequila=42')
        assert rv.status == requests.codes.ok
        assert rv is not None
        assert rv.request.args['tequila'] == '42'

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
