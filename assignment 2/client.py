import socket

HOST, PORT = "localhost", 9999 # host is local host and port is 9999

# Create a socket (SOCK_STREAM means a TCP socket)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    # Connect to server and send data
    sock.connect((HOST, PORT))

    # received menu from server
    menu = str(sock.recv(1024), "utf-8")
    print(menu) # print menu

    # user input of int choice in the menu
    choice = input()

    # send choice value to server.py
    sock.sendall(bytes(choice + "\n", "utf-8"))

    # while client does not pick 8 to exit
    while int(choice) != 8:

        # if invalid number, receive error message from server
        if int(choice) < 1 or int(choice) > 8:
            received = str(sock.recv(1024), "utf-8")  
            print(received + "\n")

        # if client chooses 1, find customer
        if int(choice) == 1:
            received = str(sock.recv(1024), "utf-8")
            print(received)
            name = input() # input customer name and send to server
            sock.sendall(bytes(name + "\n", "utf-8"))
            info = str(sock.recv(1024), "utf-8")
            print(info) # receives customer found or not found
                 
        # if client chooses 2, add customer
        if int(choice) == 2:
            received = str(sock.recv(1024), "utf-8")
            print(received)
            customer = input() # input new customer name
            sock.sendall(bytes(customer + "\n", "utf-8"))

            received = str(sock.recv(1024), "utf-8")
            print(received)
            age = input() #input new customer age
            sock.sendall(bytes(age + "\n", "utf-8"))

            received = str(sock.recv(1024), "utf-8")
            print(received)
            address = input() # input new customer address
            sock.sendall(bytes(address + "\n", "utf-8"))

            received = str(sock.recv(1024), "utf-8")
            print(received)
            pNb = input() # input new customer phone number
            sock.sendall(bytes(pNb + "\n", "utf-8"))

            received = str(sock.recv(1024), "utf-8")
            print(received) # receives success or failure message

        # if client chooses 3, delete customer
        if int(choice) == 3:
            received = str(sock.recv(1024), "utf-8")
            print(received)
            customer = input() # input customer name
            sock.sendall(bytes(customer + "\n", "utf-8"))

            received = str(sock.recv(1024), "utf-8")
            print(received)
            age = input() # input customer age
            sock.sendall(bytes(age + "\n", "utf-8"))

            received = str(sock.recv(1024), "utf-8")
            print(received)
            address = input() # input customer address
            sock.sendall(bytes(address + "\n", "utf-8"))

            received = str(sock.recv(1024), "utf-8")
            print(received)
            pNb = input() # input customer phone number
            sock.sendall(bytes(pNb + "\n", "utf-8"))

            received = str(sock.recv(1024), "utf-8")
            print(received) # print success or failure message

        # if client chooses 4, modify customer age
        if int(choice) == 4:
            received = str(sock.recv(1024), "utf-8")
            print(received)
            name = input() # input customer name to modify
            sock.sendall(bytes(name + "\n", "utf-8"))
            
            # receive count for if statements
            count = str(sock.recv(1024), "utf-8")

            # if count is 0, then customer does not exist
            if int(count) == 0:
                received = str(sock.recv(1024), "utf-8")
                print(received + "\n") # print failure message

            # if count is 1, then one customer exists
            elif int(count) == 1:
                received = str(sock.recv(1024), "utf-8")
                print(received)
                age = input() # input age to modify
                sock.sendall(bytes(age + "\n", "utf-8"))

                received = str(sock.recv(1024), "utf-8")
                print(received + "\n") # print success message

            # if count is more than 1, then more than one customer with the same name exists
            else:
                moreOne = str(sock.recv(1024), "utf-8")
                print(moreOne)
                pick = input() # input which customer to modify
                # input invalid, re prompt user for new value
                while int(pick) < 1 or int(pick) > int(count):
                    print("Not a valid number, try again. Pick a number from 1 to " + count + ":")
                    pick = input() 
                sock.sendall(bytes(pick + "\n", "utf-8"))

                received = str(sock.recv(1024), "utf-8")
                print(received)
                age = input() # input age to modify
                sock.sendall(bytes(age + "\n", "utf-8"))
                
                received = str(sock.recv(1024), "utf-8")
                print(received + "\n") # print success message

        # if client chooses 5, modify customer address
        if int(choice) == 5:
            received = str(sock.recv(1024), "utf-8")
            print(received)
            name = input() # input customer name to modify
            sock.sendall(bytes(name + "\n", "utf-8"))
        
            # receive count for if statements
            count = str(sock.recv(1024), "utf-8")

            # if count is 0, then customer does not exist
            if int(count) == 0:
                received = str(sock.recv(1024), "utf-8")
                print(received + "\n") # print failure message

            # if count is 1, then one customer exists
            elif int(count) == 1:
                received = str(sock.recv(1024), "utf-8")
                print(received)
                address = input() # input address to modify
                sock.sendall(bytes(address + "\n", "utf-8"))

                received = str(sock.recv(1024), "utf-8")
                print(received + "\n") # print success message

            # if count is more than 1, then more than one customer with the same name exists
            else:
                moreOne = str(sock.recv(1024), "utf-8")
                print(moreOne)
                pick = input() # input which customer to modify
                # input invalid, re prompt user for new value
                while int(pick) < 1 or int(pick) > int(count):
                    print("Not a valid number, try again. Pick a number from 1 to " + count + ":")
                    pick = input()
                sock.sendall(bytes(pick + "\n", "utf-8"))

                received = str(sock.recv(1024), "utf-8")
                print(received)
                address = input() # input address to modify
                sock.sendall(bytes(address + "\n", "utf-8"))
                
                received = str(sock.recv(1024), "utf-8")
                print(received + "\n") # print success message

        # if client chooses 6, modify customer phone number
        if int(choice) == 6:
            received = str(sock.recv(1024), "utf-8")
            print(received)
            name = input() # input customer name to modify
            sock.sendall(bytes(name + "\n", "utf-8"))
            
            # receive count for if statements
            count = str(sock.recv(1024), "utf-8")

            # if count is 0, then customer does not exist
            if int(count) == 0:
                received = str(sock.recv(1024), "utf-8")
                print(received + "\n") # print failur message

            # if count is 1, then one customer exists
            elif int(count) == 1:
                received = str(sock.recv(1024), "utf-8")
                print(received)
                pNb = input() # input phone number to modify
                sock.sendall(bytes(pNb + "\n", "utf-8"))

                received = str(sock.recv(1024), "utf-8")
                print(received + "\n") # print success message

            # if count is more than 1, then more than one customer with the same name exists
            else:
                moreOne = str(sock.recv(1024), "utf-8")
                print(moreOne)
                pick = input() # input which customer to modify
                # input invalid, re prompt user for new value
                while int(pick) < 1 or int(pick) > int(count):
                    print("Not a valid number, try again. Pick a number from 1 to " + count + ":")
                    pick = input()
                sock.sendall(bytes(pick + "\n", "utf-8"))

                received = str(sock.recv(1024), "utf-8")
                print(received)
                address = input() # input phone number to modify
                sock.sendall(bytes(address + "\n", "utf-8"))
                
                received = str(sock.recv(1024), "utf-8")
                print(received + "\n") # print success message

        # if client chooses 7, receives database report
        if int(choice) == 7:
            received = str(sock.recv(1024), "utf-8")
            print(received + "\n") # print out report received from server

        
        # received menu
        menu = str(sock.recv(1024), "utf-8")
        print(menu) #print menu
        # user input of int choice in the menu
        choice = input()
        # send choice value to server.py
        sock.sendall(bytes(choice + "\n", "utf-8"))


    goodbye = str(sock.recv(1024), "utf-8")
    print(goodbye + "\n") # when user prompts 8, print out goodbye message received from server
    sock.close() # close socket





