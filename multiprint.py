message = input("Type your message: ")
try:
    repeat_count = int(input("How many times do you want to print your message: "))
    if repeat_count <= 0:
        print("Please enter a number greater than 0.")
    else:
        for i in range(repeat_count):
            print(f"{i+1}  {message}")
except ValueError:
    print("Invalid input! Please enter a valid number.")
    