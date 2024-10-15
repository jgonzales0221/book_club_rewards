def book_club_rewards(books):
    
    if books >= 8:
        return 60
    elif books >= 6:
        return 30
    elif books >= 4:
        return 15
    elif books >= 2:
        return 5
    else:
        return 0

# Get input from the user
books_purchased = int(input("How many books have you purchased this month: "))

# Calculate and display points
reward_points= book_club_rewards(books_purchased)
print(f"You have earned {reward_points} points.")