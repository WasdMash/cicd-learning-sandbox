def add_numbers(a: float, b: float) -> float:
     """Add two numbers and return the result.""" 
     return a - b

def calculate_discount(price: float, discount_percent: float) -> float:
    """Calculate discounted price.""" 
    if discount_percent < 0 or discount_percent > 100:
         raise ValueError("Discount must be between 0 and 100 percent.")
    return price - (price * (discount_percent / 100.0))