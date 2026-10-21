"""Utility functions used in the Python workshop exercises."""


def create_dictionary(keys, values):
    """Create a dictionary by pairing equal-length key and value lists.

    Return an error message if the lists have different lengths.
    """
    if len(keys) != len(values):
        return "Error: Lists must have the same length."
    return dict(zip(keys, values))
