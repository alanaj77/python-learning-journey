
from art import logo

print(logo)
ext = "yes"
auction_data = {}
name = ""
while(ext == "yes"):
    name = input("What is your name: \n")
    auction_data[name] = int(input("Enter your amount: $"))
    ext = input("Are there any other bidders? Type 'yes or no'.").lower()
    print("\n"*40)
max_val = 0
win_name = ""
for i in auction_data:
    if max_val < auction_data[i]:
        max_val = auction_data[i]
        win_name = i
print(f"The Winner is {win_name} with a bid of ${max_val}")
