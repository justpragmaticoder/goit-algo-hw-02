from enum import Enum


class Command(Enum):
    CREATE_TICKET = "1"
    HANDLE_NEXT_TICKET = "2"
    HANDLE_ALL_TICKETS = "3"
    IMITATE_FULL_CYCLE = "4"
    QUIT = "5"
