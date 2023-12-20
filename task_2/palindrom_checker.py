from collections import deque
from enums.command import Command


def is_palindrome(input_string):
    input_string = input_string.lower().replace(" ", "")

    char_queue = deque()
    for char in input_string:
        char_queue.append(char)

    while len(char_queue) > 1:
        if char_queue.popleft() != char_queue.pop():
            return False
    return True


print(f"This program helps to check if you typed palindrome or not.")
print(f"E.g words Civic, Level, Mom are palindroms")
print(f'Sentence "Was it a car or a cat I saw?" is also a palindrome')


while True:
    print("\Options:")
    print(f"{Command.CHECK_STRING.value}. Check string on palindrome")
    print(f"{Command.QUIT.value}. Quit")

    choice = input("Choose option: ")

    if choice == Command.CHECK_STRING.value:
        string_to_check = input("Type your string: ")
        if is_palindrome(string_to_check):
            print(f"Current string is a palindrom")
        else:
            print(f"It is not a palindrom")
    elif choice == Command.QUIT.value:
        print("Programm has finished current session. Have a good day :)")
        break
    else:
        print("Wrong choise. Try again.")
