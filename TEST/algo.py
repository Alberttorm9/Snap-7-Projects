import stripe

def create_customer(email, name=None, description=None):
    """Create a new customer in Stripe.

    Args:
        email (str): The customer's email address. Required.
        name (str, optional): The customer's name. Defaults to None.
        description (str, optional): A description of the customer. Defaults to None.

    Returns:
        stripe.Customer: The created customer object.
    """
    stripe.api_key = "sk_test_4eC39HqLyjWDarjtT1zdp7dc"

    customer = stripe.Customer.create(
        email=email,
        name=name,
        description=description,
    )

    return customer

customer = create_customer(
    email="jane@example.com",
    name="Jane Doe",
    description="Customer for Example Corp.",
)

print(customer)