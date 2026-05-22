def calculate_discount(cart_total, user_tier):
    base_rate = 0.05 if user_tier == "gold" else 0.02
    seasonal_boost = 0.1 if is_holiday() else 0
    final_rate = base_rate + (base_rate * seasonal_boost)
    return cart_total * (1 - final_rate)