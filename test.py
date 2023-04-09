nickname = input("enter your nickname: ....")
paswd = input("enter your password")

try:
# Open the file in read mode
    with open("user.txt", "r") as f:
        # Loop over each line in the file
        for line in f:
            # Split the line into nickname and password
            stored_nickname, stored_password = line.strip().split(":")

            # Check if the nickname and password match
            if nickname == stored_nickname and paswd == stored_password:
                print("Login successful!")
                print(f"hello {nickname}")

        
except FileNotFoundError:       
        with open("user.txt", "a") as f:
    # Write the nickname and password as a list
            f.write(f"{nickname}:{paswd}\n")
            

else:
     with open("user.txt", "a") as f:
            f.write(f"{nickname}:{paswd}\n")



