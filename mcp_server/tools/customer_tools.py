from mcp_server.core_logic.tool_decorator import mcp_tool
import datetime

# Mock database for customer profiles and order history
mock_customer_profiles = {
    "1234567890": {
        "phone": "1234567890",
        "name": "John Doe",
        "preferences_json": {"favorite_category": "burgers", "spice_level": "medium"},
        "order_frequency": "weekly",
        "avg_ticket": 25.50,
        "lifetime_value": 350.75,
        "last_order_date": (datetime.date.today() - datetime.timedelta(days=7)).isoformat(),
        "satisfaction_score": 4.5,
        "created_at": (datetime.date.today() - datetime.timedelta(days=90)).isoformat(),
        "updated_at": (datetime.date.today() - datetime.timedelta(days=7)).isoformat(),
    },
    "0987654321": {
        "phone": "0987654321",
        "name": "Jane Smith",
        "preferences_json": {"favorite_category": "salads", "drinks": ["water", "iced tea"]},
        "order_frequency": "monthly",
        "avg_ticket": 15.00,
        "lifetime_value": 150.00,
        "last_order_date": (datetime.date.today() - datetime.timedelta(days=30)).isoformat(),
        "satisfaction_score": 4.0,
        "created_at": (datetime.date.today() - datetime.timedelta(days=180)).isoformat(),
        "updated_at": (datetime.date.today() - datetime.timedelta(days=30)).isoformat(),
    }
}

mock_order_history = {
    "1234567890": [
        {"order_id": "order_123", "customer_phone": "1234567890", "items_json": [{"item_id": "item_1", "quantity": 1}, {"item_id": "item_3", "quantity": 1}], "total_amount": 14.98, "status": "delivered", "created_at": (datetime.datetime.now() - datetime.timedelta(days=7)).isoformat()},
        {"order_id": "order_120", "customer_phone": "1234567890", "items_json": [{"item_id": "item_2", "quantity": 2}], "total_amount": 23.98, "status": "delivered", "created_at": (datetime.datetime.now() - datetime.timedelta(days=14)).isoformat()},
    ],
    "0987654321": [
        {"order_id": "order_111", "customer_phone": "0987654321", "items_json": [{"item_id": "item_5", "quantity": 1}, {"item_id": "item_4", "quantity": 1}], "total_amount": 9.98, "status": "delivered", "created_at": (datetime.datetime.now() - datetime.timedelta(days=30)).isoformat()},
    ]
}

@mcp_tool
def get_customer_profile(phone: str):
    """
    Retrieves the profile for a given customer phone number.
    Returns mock data.
    """
    profile = mock_customer_profiles.get(phone)
    if profile:
        return profile
    return {"phone": phone, "error": "Customer profile not found"}

@mcp_tool
def get_order_history(phone: str, limit: int = 10):
    """
    Retrieves the order history for a given customer phone number.
    Returns mock data.
    """
    history = mock_order_history.get(phone, [])
    return sorted(history, key=lambda x: x["created_at"], reverse=True)[:limit]

# Example usage (for testing purposes)
if __name__ == '__main__':
    print("Profile for 1234567890:", get_customer_profile("1234567890"))
    print("\nProfile for unknown_phone:", get_customer_profile("unknown_phone"))
    print("\nOrder history for 1234567890:", get_order_history("1234567890"))
    print("\nOrder history for 0987654321 (limit 1):", get_order_history("0987654321", limit=1))
    print("\nOrder history for unknown_phone:", get_order_history("unknown_phone"))
