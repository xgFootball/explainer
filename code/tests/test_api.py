import unittest
from unittest.mock import patch, Mock


from api import API

class TestApi(unittest.TestCase):

    def setUp(self):
        self.api = API()
        self.fake_resp_json = '{"test": "value"}'
        self.fake_un = 'user'
        self.fake_pwd = 'user'
        return
    
    def test_get_token_input(self):
        self.assertRaises(Exception, self.api.get_token)

    def test_plain_request_input(self):
        self.assertRaises(Exception, self.api.plain_request)

    @patch('api.requests')
    def test_plain_request_returns_dict(self, mock_request):

        mock_response = Mock()
        mock_response.text = self.fake_resp_json
        mock_request.get.return_value = mock_response
        res = self.api.plain_request('/fake_path')
        self.assertIsInstance(res, dict)

    @patch('api.requests')
    def test_get_token_returns_dict(self, mock_request):
        mock_response = Mock()
        mock_response.text = self.fake_resp_json
        mock_request.post.return_value = mock_response
        res = self.api.get_token(
            self.fake_un,
            self.fake_pwd
        )
        self.assertIsInstance(res, dict)

    @patch('api.requests')
    def test_plain_request_calls_get(self, mock_request):
        mock_response = Mock()
        mock_response.text = self.fake_resp_json
        mock_request.get.return_value = mock_response

        res = self.api.plain_request('/fake_path')
        mock_request.get.assert_called()

    @patch('api.requests')
    def test_get_token_calls_post(self, mock_request):
        mock_response = Mock()
        mock_response.text = self.fake_resp_json
        mock_request.post.return_value = mock_response

        res = self.api.get_token(
            self.fake_un,
            self.fake_pwd
        )
        mock_request.post.assert_called()

    @patch('api.requests')
    def test_plain_request_called_with_url(self, mock_request):
        mock_response = Mock()
        mock_response.text = self.fake_resp_json
        mock_request.get.return_value = mock_response

        url_path = '/fake_path'
        res = self.api.plain_request(url_path)
        mock_request.get.assert_called_with(
            self.api.base + url_path,
            verify=False
        )
 

    @patch('api.requests')
    def test_get_token_calls_post_with_un_pwd(self, mock_request):
        mock_response = Mock()
        mock_response.text = self.fake_resp_json
        mock_request.post.return_value = mock_response

        res = self.api.get_token(
            self.fake_un,
            self.fake_pwd
        )

        mock_request.post.assert_called_with(
            self.api.base + self.api.login_path,
            verify = False,
            json = {"email": self.fake_un, "password": self.fake_pwd}
        )
 

if __name__ == "__main__":
    unittest.main()


