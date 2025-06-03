import unittest
from mcp_server.tools.customer_tools import get_customer_profile, get_order_history, mock_customer_profiles, mock_order_history

class TestCustomerTools(unittest.TestCase):

    def test_get_customer_profile_found(self):
        phone = "1234567890" # Known phone from mock data
        profile = get_customer_profile(phone)
        self.assertEqual(profile["phone"], phone)
        self.assertEqual(profile["name"], mock_customer_profiles[phone]["name"])

    def test_get_customer_profile_not_found(self):
        profile = get_customer_profile("unknown_phone")
        self.assertIn("error", profile)

    def test_get_order_history_found(self):
        phone = "1234567890" # Known phone
        history = get_order_history(phone)
        self.assertIsInstance(history, list)
        self.assertEqual(len(history), len(mock_order_history[phone]))
        if history: # Check sorting if history is not empty
            self.assertTrue(history[0]["created_at"] >= history[-1]["created_at"])


    def test_get_order_history_limit(self):
        phone = "1234567890" # Known phone
        history = get_order_history(phone, limit=1)
        self.assertEqual(len(history), 1)

    def test_get_order_history_not_found(self):
        history = get_order_history("unknown_phone")
        self.assertEqual(len(history), 0) # Should return empty list

if __name__ == '__main__':
    unittest.main()
