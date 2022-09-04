"""Customers at Hackbright."""


class Customer:
    """Ubermelon customer."""

    def __init__(self, first_name, last_name, email, password):
        """An Ubermelon Customer type."""

        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def __repr__(self):
        """Convenience method to show information about customer in console."""

        return f"<Customer: {self.first_name}, {self.last_name}, {self.email} >"


def read_customer_file(filepath):

    customer_info = {}

    with open(filepath) as file:
        for line in file:
            (first_name, last_name, email, password) = line.strip().split("|")
            customer_info[email] = Customer(first_name, last_name, email, password)

    return customer_info


def get_by_email(email):
    return customer_info[email]


customer_info = read_customer_file("customers.txt")
