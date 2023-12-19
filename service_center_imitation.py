import queue
import time
import random
from enums.command import Command

ticket_types = ["TV repair", "Smartphone repair", "Software upgrade/fix"]
ticket_queue = queue.Queue()


def generate_request():
    # Unique ID imitation
    request_id = len(ticket_queue.queue) + 1
    # Random ticket type
    request_type = random.choice(ticket_types)
    request = {"ID": request_id, "Type": request_type}
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


while True:
    print("\Interface:")
    print(f"{Command.CREATE_TICKET.value}. Create new ticket")
    print(f"{Command.HANDLE_NEXT_TICKET.value}. Handle next ticket")
    print(f"{Command.HANDLE_ALL_TICKETS.value}. Handle all tickets (one by one)")
    print(f"{Command.IMITATE_FULL_CYCLE.value}. Imitate full cycle")
    print(f"{Command.QUIT.value}. Quit")

    choice = input("Choose option: ")

    if choice == Command.CREATE_TICKET.value:
        generate_request()
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
        generate_request()
        process_request()
    elif choice == Command.QUIT.value:
        print("Programm has finished current session. Have a good day :)")
        break
    else:
        print("Wrong choise. Try again.")
