sentence = input("Enter a sentence: ")
tidied_message = sentence.lower().replace(" ", "")
print(tidied_message)

coke_input = input("Do you have coke (yes/no): ")
chips_input = input("Do you have chips (yes/no): ")
has_coke = (coke_input == "yes")
has_chips = (chips_input == "yes")
both = has_coke and has_chips
any_item = has_coke or has_chips
neither = not any_item
print(f"Need both: {both}")

booked_input = input()
screen_input = input()
print(f"Booked seats: {booked_input}")
print(f"Seats on screen: {screen_input}")
cleaned_booked = booked_input.lower().replace(" ", "")
cleaned_screen = screen_input.lower().replace(" ", "")
exact_match = cleaned_booked == cleaned_screen
inside_screen = cleaned_booked in cleaned_screen
print(f"Exact match: {exact_match}")
print(f"Inside screen: {inside_screen}")

import sys
questions_answers = [
    ("How many books can I borrow?", "You can borrow 3 books."),
    ("What time does the library open?", "The library opens at 9 AM."),
    ("Where is the reading room?", "The reading room is on the first floor.")]
def clean_text(text):
    """Converts text to lowercase and removes all whitespace characters."""
    return "".join(text.lower().split())
print("Library Helper Bot is active. Press Ctrl + C to stop.\n")
try:
    while True:
        user_input = input("Prompt: ")
        
      
        cleaned_input = clean_text(user_input)
        matched = False
        
     
        if cleaned_input:
            for question, answer in questions_answers:
                cleaned_question = clean_text(question)
                
          
                if cleaned_input in cleaned_question:
                    print(f"Response: {answer}")
                    matched = True
                    break  # Stop checking once a match is found
        if not matched:
            print("Response: Sorry, I don't understand that question.")
except KeyboardInterrupt:
    print("\nBot stopped. Goodbye!")

age = int(input("Enter age: "))
ticket = input("Have a ticket (yes/no): ").upper()
vip_pass = input("VIP pass (yes/no): ").upper()
banned = input("On banned list (yes/no): ").upper()
age = int(input("Enter age: "))
ticket = input("Have a ticket (yes/no): ").upper()
vip_pass = input("VIP pass (yes/no): ").upper()
banned = input("On banned list (yes/no): ").upper()
if (has_ticket or has_vip) and age >= 12 and not is_banned:
    print("Entry: Allowed")
else:
    print("Entry: Denied")
