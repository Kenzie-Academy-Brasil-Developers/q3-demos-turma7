import unittest
from app import app


class TestApi(unittest.TestCase):
    def test_rota_home(self):
        self.assertTrue(app.get("/"), 200)
        self.assertIn("[]", "this is my name []")
        self.assertAlmostEqual(5, 5)


# e2e, conftest
