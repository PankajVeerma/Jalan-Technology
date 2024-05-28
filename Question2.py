class Guest:
    def __init__(self, age):
        self.age = age
    
    def get_price(self):
        if self.age <= 2:
            return 0
        elif 2 < self.age < 18:
            return 100
        elif 18 <= self.age < 60:
            return 500
        else:  # age >= 60
            return 300
    
    def __str__(self):
        return f"Guest (age: {self.age})"

class Ticket:
    def __init__(self, guests):
        self.guests = guests
        self.total_price = sum(guest.get_price() for guest in guests)
    
    def display_ticket(self):
        for i, guest in enumerate(self.guests, start=1):
            print(f"Guest {i} (age: {guest.age})")
        print(f"Total Charges: INR {self.total_price}")

class TicketCounter:
    def __init__(self):
        self.tickets = []
    
    def issue_ticket(self, guest_ages):
        guests = [Guest(age) for age in guest_ages]
        ticket = Ticket(guests)
        self.tickets.append(ticket)
        return ticket
    
    def validate_ticket(self, ticket):
        print("Validating Ticket:")
        ticket.display_ticket()

# Example usage
ticket_counter = TicketCounter()

# Input the number of guests and their ages
guest_ages = [23, 25, 2, 17, 60]
ticket = ticket_counter.issue_ticket(guest_ages)

# Display the issued ticket
print("Issued Ticket:")
ticket.display_ticket()

# Validate the ticket
print("\nSecurity Validation:")
ticket_counter.validate_ticket(ticket)
