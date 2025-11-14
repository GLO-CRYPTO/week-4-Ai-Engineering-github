def sort_dictionaries(data: list[dict], key_name: str, reverse: bool = False) -> list[dict]:
    """
    Sorts a list of dictionaries based on the value of a specific key.

    This function utilizes the 'sorted()' built-in function for a non-destructive
    sort, meaning it returns a new sorted list without modifying the original.

    Args:
        data: The list of dictionaries to be sorted.
        key_name: The string key whose values will be used for sorting.
        reverse: If True, the list is sorted in descending order (default is False).

    Returns:
        A new list of dictionaries sorted according to the specified key.
    """
    # Use a lambda function as the 'key' argument for the sorted() function.
    # The lambda function tells Python how to extract the comparison key (value)
    # from each dictionary item (d) in the list.
    try:
        sorted_data = sorted(data, key=lambda d: d[key_name], reverse=reverse)
        return sorted_data
    except TypeError as e:
        # Handle cases where the data types for the key are not comparable (e.g., mixing strings and integers)
        print(f"Error: Non-comparable types found for key '{key_name}'. Details: {e}")
        return data
    except KeyError:
        # Handle cases where the specified key_name does not exist in one or more dictionaries
        print(f"Error: Key '{key_name}' not found in one or more dictionaries.")
        return data

# --- Example Usage ---
users = [
    {'name': 'Alice', 'age': 30, 'score': 85},
    {'name': 'Bob', 'age': 25, 'score': 92},
    {'name': 'Charlie', 'age': 30, 'score': 78},
    {'name': 'David', 'age': 25, 'score': 92}
]

print("Original List:")
for user in users:
    print(user)

print("\nSorted by 'age' (Ascending):")
sorted_by_age = sort_dictionaries(users, 'age')
for user in sorted_by_age:
    print(user)

print("\nSorted by 'score' (Descending):")
sorted_by_score = sort_dictionaries(users, 'score', reverse=True)
for user in sorted_by_score:
    print(user)