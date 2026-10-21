def create_dict(keys, values):
    """Create a dictionary from two lists."""
    if len(keys) != len(values):
        return "Error: Lists must have the same length."
    return dict(zip(keys, values))