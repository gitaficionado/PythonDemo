from datetime import datetime
from zoneinfo import ZoneInfo

'''
def is_holiday():
    # Minimal stub: replace with real holiday logic as needed
    return False
'''

def is_holiday(user_timezone):
    now = datetime.now(ZoneInfo(user_timezone))
    today = now.date()

    return today.month == 12 and today.day == 25


def calculate_discount(cart_total, user_tier, user_timezone):
    base_rate = 0.05 if (user_tier or "").lower() == "gold" else 0
    seasonal_boost = 0.1 if is_holiday(user_timezone) else 0

    final_rate = base_rate * (1 + seasonal_boost)
    final_rate = min(final_rate, 1.0)

    return round(cart_total * (1 - final_rate), 2)

''''
def calculate_discount(cart_total, user_tier):
    base_rate = 0.05 if user_tier == "gold" else 0.02
    seasonal_boost = 0.1 if is_holiday() else 0
    final_rate = base_rate + (base_rate * seasonal_boost)
    return cart_total * (1 - final_rate)
'''

if __name__ == "__main__":
    # Simple runnable example
    sample_total = 100.0
    sample_tier = "gold"
    discounted = calculate_discount(sample_total, sample_tier)
    print(f"Original total: {sample_total}")
    print(f"User tier: {sample_tier}")
    print(f"Discounted total: {discounted}")