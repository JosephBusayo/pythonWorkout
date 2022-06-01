"""Program that asks the user for an hour between 1 and 12 and for how many hours in the future they want to go"""

def hours_ahead():
    current_hour = int(input("Enter any hour of the day: "))
    hours_to_travel = int(input("How many hours to do you want to travel: "))
    
    #% return reminder
    time_travel = (current_hour + hours_to_travel) % 12
    if time_travel == 0:
        return("You're back at 12 ")
    else:
        return (f"You are now at {time_travel}")
