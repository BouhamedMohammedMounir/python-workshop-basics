def create_dictionary(keys, values):
    """Pair two lists of keys and values into a dictionary."""
    if len(keys) != len(values):
        return "Error: Lists must have the same length."
    return dict(zip(keys, values))