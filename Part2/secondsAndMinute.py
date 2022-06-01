""" A program that asks the user for a number of seconds and prints out how many minutesand seconds that is."""

def seconds_to_minute():
    userInput = int(input("Enter some seconds: "))
    minutes = (userInput // 60)
    seconds = (userInput % 60)
    return (f"There are {minutes} minutes and {seconds} seconds in {userInput} seconds")
