import json
from datetime import datetime


class DataProcessor:
    def __init__(self):
        self.data = []

    def process_user_data(self, user_info):
        processed = {
            "id": user_info["id"],
            "name": user_info["name"],
            "email": user_info["email"],
            "age": self.calculate_age(user_info["birthdate"]),
            "status": "active",
        }

        self.data.append(processed)
        return processed

    def calculate_age(self, birthdate):
        birth_date = datetime.strptime(birthdate, "%Y-%m-%d")
        today = datetime.now()
        age = today.year - birth_date.year

        if today.month < birth_date.month:
            age -= 1

        return age

    def filter_by_age(self, min_age, max_age):
        filtered = []
        for user in self.data:
            if user["age"] >= min_age and user["age"] <= max_age:
                filtered.append(user)

        return filtered

    def export_to_json(self, filename):
        with open(filename, "w") as f:
            json.dump(self.data, f, indent=4)

        print(f"Data exported to {filename}")

    def get_average_age(self):
        total = 0
        for user in self.data:
            total += user["age"]

        # BUG2: Division by zero if no data
        return total / len(self.data)
