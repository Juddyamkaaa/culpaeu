def list_to_binary(lst):
    """Convert a list of integers to their binary representations."""
    if all(isinstance(i, int) for i in lst):
        return [bin(i)[2:] for i in lst]
    else:
        raise ValueError("All elements in the list must be integers.")

# Example usage
numbers = [10, 15, 20]
binary_list = list_to_binary(numbers)
print(binary_list)  # Output: ['1010', '1111', '10100']
