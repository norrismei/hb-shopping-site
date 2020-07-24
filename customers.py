"""Customers at Hackbright."""


class Customer(object):
    """Ubermelon customer."""

    def __init__(self, first_name, last_name, email, password):
        """Creates a Customer object"""

        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def __repr__(self):
        """Human readable representation of Customer object"""

        return "<Customer: {} {}, {}>".format(self.first_name, self.last_name,
                                                self.email)

def read_customers_from_file(filepath):
    """Read customer data and populate dictionary of customers

    Dictionary will be {email: Customer object"""

    customers = {}

    with open(filepath) as file:
        for line in file:
            (first_name,
             last_name,
             email,
             password) = line.strip().split("|")

            customers[email] = Customer(first_name, last_name, email, password)

    return customers

def get_by_email(email):
    """Return a Customer, given their email.

    Relies on access to global dictionary 'customers'"""

    return customers[email]


customers = read_customers_from_file("customers.txt")
