# task 1
data = {
        "Monday": {},
        "Tuesday": {},
        "Wednesday": {},
        "Thursday": {},
        "Friday": {},
        "Saturday": {},
        "Sunday": {}
    }

def get_command():
    print("s - Store Program")
    print("l - List daily program")
    print("x - Exit")
    command = input("chose from the list:")

    if command == "s":
        store_program(data)
    if command == "l":
        list_programs(data)
    if command == "x":
        exit()


def store_program(data):
    day = input("which day?")
    time = str(input("what time?"))
    program = input("what is the program?")
    for i in data:
        if day == i:
            data[i][time + ":00"] = program
    get_command()

def list_programs(data):
    day = input("Which day?")
    result = {}
    for i in data:
        if i == day:

                for hour in range(0,24):
                    result[str(hour) + ":00"] = ""
                    for time in data[i]:
                        if str(hour) + ":00" == time:
                            result[str(hour) + ":00"] = data[i][time]
    for program in result:
        print(program + " " + result[program])

    get_command()


get_command()


