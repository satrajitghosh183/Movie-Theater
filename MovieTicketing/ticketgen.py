# Dictionary to store ticket information
tickets = {}


def generate_ticket(movie_id, seat_number, price):
  # Create a new ticket
  ticket = Ticket(movie_id, seat_number, price)

  # Generate a unique ticket ID
  ticket_id = generate_ticket_id()

  # Store the ticket in the dictionary
  tickets[ticket_id] = ticket

  return ticket_id


def get_ticket(ticket_id):
  # Retrieve the ticket from the dictionary
  return tickets.get(ticket_id)


def generate_ticket_id():
  # Generate a unique ticket ID (e.g., using UUID)
  return str(uuid.uuid4())
