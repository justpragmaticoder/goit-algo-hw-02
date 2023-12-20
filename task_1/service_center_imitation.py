import queue
import time
import random
import uuid
from enums.command import Command

ticket_types = [
    "TV repair",
    "Smartphone repair",
    "Software upgrade/fix",
    "Vacuum cleaner repair",
    "Laptop repair",
]
ticket_queue = queue.Queue()


def generate_request():
    # Unique ID
    request_id = str(uuid.uuid4())
    # Random ticket type
    request_type = random.choice(ticket_types)
    request = {"ID": request_id, "Type": request_type}
    print(f"Generating Ticket of type '{request_type}' ...")
    # Imitate ticket generation time
    time.sleep(random.uniform(1, 3))
    ticket_queue.put(request)
    print(f"Ticket {request_id} of type '{request_type}' was added to queue.")


def process_request():
    if not ticket_queue.empty():
        request = ticket_queue.get()
        print(f"Ticket {request['ID']} of type '{request['Type']}' is in progress...")
        # Imitate handling time
        time.sleep(random.uniform(1, 3))
        print(f"Ticket {request['ID']} is handled.")
    else:
        print("Queue is empy.")


def get_ticket_qty():
    while True:
        tickets_qty = input("Type how many tickets you want to generate: ")

        if tickets_qty.isdigit():  # Перевірка, що введено число
            return int(tickets_qty)
        else:
            print("Please enter a valid number.")


def generate_tickets(tickets_qty=None):
    tickets_qty = tickets_qty or get_ticket_qty()
    for _ in range(tickets_qty):
        generate_request()
    print("All tickets are generated.")


while True:
    print("\Interface:")
    print(f"{Command.CREATE_TICKET.value}. Create new ticket")
    print(f"{Command.HANDLE_NEXT_TICKET.value}. Handle next ticket")
    print(f"{Command.HANDLE_ALL_TICKETS.value}. Handle all tickets (one by one)")
    print(f"{Command.IMITATE_FULL_CYCLE.value}. Imitate full cycle")
    print(f"{Command.QUIT.value}. Quit")

    choice = input("Choose option: ")

    if choice == Command.CREATE_TICKET.value:
        generate_tickets()
    elif choice == Command.HANDLE_NEXT_TICKET.value:
        process_request()
    elif choice == Command.HANDLE_ALL_TICKETS.value:
        if ticket_queue.empty():
            print("Tickets queue is empty. Plz, create a ticket")
        else:
            while not ticket_queue.empty():
                process_request()
                print("All tickets were handled.")
    elif choice == Command.IMITATE_FULL_CYCLE.value:
        tickets_qty = get_ticket_qty()

        try:
            generate_tickets(tickets_qty)

            print("Starting to process tickets.")

            for _ in range(tickets_qty):
                process_request()
        except KeyboardInterrupt:
            print("\nInterrupted by user.")
    elif choice == Command.QUIT.value:
        print("Programm has finished current session. Have a good day :)")
        break
    else:
        print("Wrong choise. Try again.")
