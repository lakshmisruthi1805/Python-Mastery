"""User will enter a number between (1-12) you need to print the month number

January
Febuary ...
December any value other than 1-12 you need to print Invalid Month Number Try again"""
month_number = int(input("Enter a number between 1-12: "))
month = ""
match month_number:
    case 1:
        month = "January" 
    case 2:
        month = "February"
    case 3:
        month = "March"
    case 4:
        month = "April"
    case 5:
        month = "May"
    case 6:
        month = "June"
    case 7:
        month = "July"
    case 8:
        month = "August"
    case 9:
        month = "September"
    case 10:
        month = "October"
    case 11:
        month = "November"
    case 12:
        month = "December"
    case _:
        print("Invalid month number,Try again.")
print(month)