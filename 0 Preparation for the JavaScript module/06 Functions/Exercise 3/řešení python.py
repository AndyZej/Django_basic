def calculateTip(amount, rating):
    if rating == "Very good service":
        return amount * 0.25
    elif rating == "Good service":
        return amount * 0.20
    elif rating == "Average service":
        return amount * 0.15
    elif rating == "Bad service":
        return amount * 0
    else:
        return "Unreadable description"


# Example usage
result = calculateTip(100, "Very good service")

print(result)