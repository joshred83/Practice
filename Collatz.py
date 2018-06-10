import sys

def collatz(number):
    try:
        number = int(number)
        if number % 2 == 0:
            out = int(number / 2)

        elif number % 2 == 1:
            out = 3 * number + 1

        return out
    except ValueError:
        print("Invalid input.")
        sys.exit()


def main():
    user_number = input('Your number: ')
    print(user_number)

    while user_number != 1:
        user_number = collatz(user_number)
        print(user_number)


if __name__ == '__main__':
    main()
