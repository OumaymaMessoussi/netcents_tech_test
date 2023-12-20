import unittest
from flask_testing import TestCase
from main import app


class TestGetLargestTransactionEndpoint(TestCase):
    def create_app(self):
        app.config["TESTING"] = True
        return app

    def test_get_largest_transaction(self):
        response = self.client.get("/api/largest_transaction")
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertIn("hash", data)
        self.assertIn("total", data)
        self.assertIn("fees", data)
        self.assertIn("inputs", data)
        self.assertIn("outputs", data)


if __name__ == "__main__":
    unittest.main()
