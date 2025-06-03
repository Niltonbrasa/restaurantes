from mcp_server.core_logic.tool_decorator import mcp_tool
import datetime
import uuid

# Mock database for orders (very simplified)
mock_orders_db = {}

@mcp_tool
def create_order(customer_data: dict, items: list):
    """
    Creates a new order with the given customer data and items.
    Returns mock data confirming order creation.
    Assumes customer_data contains at least 'phone'.
    Assumes items is a list of dicts, each with 'item_id' and 'quantity'.
    """
    if not customer_data or not customer_data.get("phone"):
        return {"success": False, "error": "Customer phone is required."}
    if not items:
        return {"success": False, "error": "Order must contain at least one item."}

    order_id = str(uuid.uuid4())
    total_amount = 0

    # In a real scenario, you would fetch item prices from the menu_items table/service
    # For mock purposes, let's assume a flat price or fetch from a simplified mock menu
    mock_item_prices = {"item_1": 10.99, "item_2": 11.99, "item_3": 3.99, "item_4": 1.99, "item_5": 7.99}

    for item in items:
        if not item.get("item_id") or not item.get("quantity"):
            return {"success": False, "error": "Each item must have 'item_id' and 'quantity'."}
        price = mock_item_prices.get(item["item_id"], 0) # Default to 0 if item not found for simplicity
        total_amount += price * item["quantity"]

    order_data = {
        "order_id": order_id,
        "customer_phone": customer_data.get("phone"),
        "customer_data_json": customer_data,
        "items_json": items,
        "total_amount": round(total_amount, 2),
        "status": "received", # Initial status
        "recommendations_used": customer_data.get("recommendations_used", []), # Example field
        "upsell_success": customer_data.get("upsell_success", False), # Example field
        "created_at": datetime.datetime.now().isoformat()
    }

    mock_orders_db[order_id] = order_data

    return {
        "success": True,
        "order_id": order_id,
        "message": "Order created successfully.",
        "order_details": order_data
    }

# Example usage (for testing purposes)
if __name__ == '__main__':
    sample_customer_data_1 = {"phone": "1234567890", "name": "John Doe"}
    sample_items_1 = [{"item_id": "item_1", "quantity": 1}, {"item_id": "item_3", "quantity": 2}]

    sample_customer_data_2 = {"phone": "0987654321", "name": "Jane Smith", "recommendations_used": ["combo_1"]}
    sample_items_2 = [{"item_id": "item_2", "quantity": 1}]

    result1 = create_order(sample_customer_data_1, sample_items_1)
    print("Order 1 creation result:", result1)

    result2 = create_order(sample_customer_data_2, sample_items_2)
    print("\nOrder 2 creation result:", result2)

    # Example of an order failing due to missing item_id
    invalid_items = [{"quantity": 1}]
    result_fail_item = create_order(sample_customer_data_1, invalid_items)
    print("\nInvalid item order result:", result_fail_item)

    # Example of an order failing due to missing phone
    invalid_customer = {}
    result_fail_customer = create_order(invalid_customer, sample_items_1)
    print("\nInvalid customer order result:", result_fail_customer)

    print("\nMock Orders DB:", mock_orders_db)
