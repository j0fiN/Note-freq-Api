import unittest
import requests


class MyTestCase(unittest.TestCase):
    def test_main(self):
        res = requests.request("GET", url="http://localhost:5000/api?note=D%231")
        print(eval(res.content))
        self.assertEqual(res.status_code, 200)


if __name__ == '__main__':
    unittest.main()
