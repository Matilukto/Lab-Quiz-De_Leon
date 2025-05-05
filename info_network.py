import datetime

# Personal Information
full_name = "Matt Tyone De Leon" 
student_id = "231-0071"  

# Get current date and time
now = datetime.datetime.now()
current_datetime = now.strftime("%Y-%m-%d %H:%M:%S")

# Print information
print("Full Name:", full_name)
print("Student ID:", student_id)
print("Current Date and Time:", current_datetime)
print("-" * 30)

# Prompt user for networking issue
networking_problem = input("Please describe a networking issue you've encountered: ")

# Save the response to network_issue.txt
try:
    with open("network_issue.txt", "w") as file:
        file.write(networking_problem)
    print("\nYour networking issue description has been saved to network_issue.txt")
except Exception as e:
    print(f"\nAn error occurred while saving to the file: {e}")
