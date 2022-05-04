from User import User
from Admin import Admin 
from Instructor import Instructor
from Student import Student

# Function to display menu to the user
def show_menu(user=None):
    print("""
    1. EXTRACT_DATA
    2. VIEW_COURSES
    3. VIEW_USERS
    4. VIEW_REVIEWS
    5. REMOVE_DATA
    """)
    
# Function to control all the operations and input from user
def process_operations(user,isAdmin=False):
    cmd_input = input()
    cmd_list = cmd_input.split()
    
    # Using exception handling for when parameter1 and parameter2 is not required
    try:
        op = cmd_list[0]
        parameter1 = cmd_list[1]
        parameter2 = cmd_list[2]
    except:
        pass

    # Using dictionary in place of if-else for better efficiency
    methods = {
        1:user.extract_info,
        2:user.view_courses,
        3:user.view_users,
        4:user.view_reviews,
        5:user.remove_data,
    }

    #for logging out user
    if op=="logout":
        main() 
    choice = int(op)

    # for when user is admin and chooses 2
    if choice==2:
      try:
        command =  parameter1
        if command=="": 
            methods[choice]()
            return

        if not command: 
            print("invalid command")
            return
        
        value = parameter2
        
        methods[choice](args=[command,value])
        return
      except:
          print("Invalid Operation. Try again")
          process_operations(user)

    # When user is 
    if choice==4:
        command =  parameter1
        if not command: 
            print("invalid command")
            return 
        
        value = parameter2

        methods[choice](args=[command,value])
        return
    
    methods[choice]()

# main function run when file is executed
def main():
    while True:
        # Code from line 81-133 is for login
        print("Please input username and password to login:(format username password)")

        cred = input()
        if cred=="exit":
            break
        username,password = cred.split(" ")

        user = User(username=username,password=password)
        login_result,login_role,login_info =  user.login()

        users={
            "Admin":Admin,
            "Instructor":Instructor,
            "Student":Student
        }

        if login_result:
            print(login_role,"login successfully")

        else:
            print("incorrect credentials")
            continue

        if login_role=="Student":
            login_info = login_info.split(";;;")
            user = users[login_role](
                login_info[0],
                user.username,
                user.password,
                login_info[3],
                login_info[4],
                login_info[5],
                login_info[6],
                ) 
        elif login_role=="Instructor":
            login_info = login_info.split(";;;")
            user = users[login_role](
                login_info[0],
                user.username,
                user.password,
                login_info[3],
                login_info[4],
                login_info[5],
                login_info[6],
                ) 
        elif login_role=="Admin":
            user = users[login_role](
                username=user.username,
                password=user.password
            )

        print(f"welcome {login_role.lower()} your role is {login_role}")
        
        # To run the main program after logging in
        while True:
            show_menu()
            process_operations(user,isAdmin=True if login_role=="Admin" else False)
        
    print("system closed")


if __name__ == "__main__":
    print("Welcome to our system")
    main()