from unittest import TestCase
from parameterized import parameterized

from po模式v4.page.page_login import PageLogin

data = [
    ('11', '22', '1', '错误验证'),
    ('wp', '22', '123', '错误密码'),
    ('11', '22', '123', '错误账号'),
    ('wp', 'wp', '123', '登录成功')
]


class TestLogin(TestCase):
    page = None

    @classmethod
    def setUpClass(cls):
        cls.page = PageLogin()
    @classmethod
    def tearDownClass(cls):
        cls.page.driver.quit()

    @parameterized.expand(data)
    def test_login(self, username, password, code, expect):
        self.page.page_input_msg(username, password, code)
        result = self.page.page_get_msg()
        self.assertEqual(result, expect)
