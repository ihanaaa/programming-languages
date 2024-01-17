import socketserver
import sys
import os

# create empty database
records = []

class MyTCPHandler(socketserver.StreamRequestHandler):

    def handle(self):
        
        # opens file at current directory
        self.file = open(os.path.join(sys.path[0],"data.txt"), "r") # open text file

        # create count to skip "**Python DB content**"
        count1 = 0
        # if empty records, fill record
        if len(records) == 0:
            # read line in text file 
            line = self.file.readline().strip()
            
            # read until EOF is empty string ''
            while line!= '':
                # if first line, skip
                if count1 == 0:
                    line = self.file.readline().strip()
                    count1+=1
                    continue
                # create a list of 4 elements (name, age, address, phone number) and remove "|"
                fileContent = line.split("|")

                # remove whitespace
                for b in range(len(fileContent)):
                    fileContent[b] = fileContent[b].strip()
                # if the name is missing skip
                if fileContent[0] == '':
                    line = self.file.readline().strip()
                    continue
                # add every line in the database
                records.append(fileContent)
                line = self.file.readline().strip() # go to next line

        
        # create variable menu (self. is reference to server.py program)
        self.menu = ("Pyton DB Menu\n\n1. Find customer\n2. Add customer\n3. Delete customer\n4. Update customer age\n5. Update customer address\n6. Update customer phone\n7. Print report\n8. Exit\n\nSelect: ")
       
        # send it to client the menu as a string
        self.wfile.write(self.menu.encode("utf-8"))
        # print menu
        print(self.menu) 
        # integer sent by client using readline() (the connector variable between the two)
        self.choice = int(self.rfile.readline().strip().decode('utf-8'))
        print(self.choice) # print client choice

        # while client does not choose exit
        while int(self.choice) != 8:

            # if invalid number (number does not exist in menu) print error message and send to client error message
            if int(self.choice)< 1 or int(self.choice) > 8:
                self.errorMsg = "Invalid number! Please try again"
                print("Invalid number! Please try again")
                self.wfile.write((self.errorMsg.encode( "utf-8")))
##############################################################################

            # if client chooses to find customer, print out name of customer if exist or error message if does not exist
            if (self.choice == 1):
                # prompt the user for customer name
                self.wfile.write(("Customer Name: ".encode("utf-8")))
                self.aName = str(self.rfile.readline().decode("utf-8").strip())
                print("Customer Name: " + self.aName)
                
                count2 = 0

                # if records has the prompted name once or more, add to string self.serverMsg and send to client
                for x in range(len(records)):
                    if records[x][0] == self.aName:
                        if count2 == 0:
                            self.serverMsg = ("Server response: " + str(records[x][0]) + "|" + str(records[x][1]) + "|" + str(records[x][2]) + "|" + str(records[x][3]) )
                            count2+=1
                        else:
                            self.serverMsg += ("Server response: " + str(records[x][0]) + "|" + str(records[x][1]) + "|" + str(records[x][2]) + "|" + str(records[x][3]))
                        self.serverMsg += "\n"
                
                # if count is 0, then customer not in databse
                if count2 == 0:
                    self.serverMsg = ("Server response: " + self.aName + " not found in database")
                
                # send back to client
                print(self.serverMsg)
                self.wfile.write(self.serverMsg.encode("utf-8"))
##############################################################################

            # if client chooses 2, add customer
            if (self.choice == 2):
                # create a list with four elements to be added of the new customer
                newCustomer = []
                # prompt user for new customer name
                self.wfile.write(("Write the customer you want to add: ").encode("utf-8"))
                self.customer = str(self.rfile.readline().decode("utf-8").strip())
                newCustomer.append(self.customer)
                print("Customer name: "+ self.customer)

                # prompt user for new customer age
                self.wfile.write(("Write the customer age: ").encode("utf-8"))
                self.age = str(self.rfile.readline().decode("utf-8").strip())
                newCustomer.append(self.age)
                print("Customer age: "+ self.age)

                # prompt user for new customer address
                self.wfile.write(("Write the customer address: ").encode("utf-8"))
                self.address = str(self.rfile.readline().decode("utf-8").strip())
                newCustomer.append(self.address)
                print("Customer address: "+ self.address)

                # prompt user for new customer phone number
                self.wfile.write(("Write the customer phone number: ").encode("utf-8"))
                self.pNb = str(self.rfile.readline().decode("utf-8").strip())
                newCustomer.append(self.pNb)
                print("Customer phone number: "+ self.pNb)

                count3 = 0
                # go through database to see if customer already exists
                for y in range(len(records)):
                    if records[y] == newCustomer:
                        self.wfile.write("Customer already exists".encode("utf-8"))
                        print("Customer already exists")
                        count3 +=1
                        break
                    
                # if count is still 0, then customer does not exist, then add new customer
                if count3 == 0:
                    records.append(newCustomer)
                    self.wfile.write("Customer succesfully added".encode("utf-8"))
                    print("Customer succesfully added")
###########################################################################################

            # if client chooses 3 to remove a customer
            if (self.choice == 3):
                # create a list with four elements of customer to remove
                oldCustomer = []

                # prompt user for customer name
                self.wfile.write(("Write the customer you want to delete: ").encode("utf-8"))
                self.customer = str(self.rfile.readline().decode("utf-8").strip())
                oldCustomer.append(self.customer)
                print("Customer name: "+ self.customer)

                # prompt user for customer age
                self.wfile.write(("Write the customer age: ").encode("utf-8"))
                self.age = str(self.rfile.readline().decode("utf-8").strip())
                oldCustomer.append(self.age)
                print("Customer age: "+ self.age)

                # prompt user for customer address
                self.wfile.write(("Write the customer address: ").encode("utf-8"))
                self.address = str(self.rfile.readline().decode("utf-8").strip())
                oldCustomer.append(self.address)
                print("Customer address: "+ self.address)

                # prompt user for customer phone number
                self.wfile.write(("Write the customer phone number: ").encode("utf-8"))
                self.pNb = str(self.rfile.readline().decode("utf-8").strip())
                oldCustomer.append(self.pNb)
                print("Customer phone number: "+ self.pNb)

                count4 = 0
                # go through database to see if customer exists, if so then remove
                for y in range(len(records)):
                    if records[y] == oldCustomer:
                        self.wfile.write("Customer succesfully removed".encode("utf-8"))
                        print("Customer succesfully removed")
                        records.pop(y)
                        count4 +=1
                        break
                # if count is 0, then customer does not exist
                if count4 == 0:
                    self.wfile.write("Customer does not exist".encode("utf-8"))
                    print("Customer does not exist")
######################################################################################################

            # if client chooses 4 to modify the age of a customer
            if (self.choice == 4):
                                
                # prompt the user for customer name
                self.wfile.write(("Customer you want to update: ".encode("utf-8")))
                self.aName = str(self.rfile.readline().decode("utf-8").strip())
                print("Customer to update: " + self.aName)
                
                count5 = 0
                changeCustomerAge = [] # create a list with four elements of customer to modify

                # go through database to see every customer with the name the user prompted
                for z in range(len(records)):

                    if records[z][0] == self.aName:
                        changeCustomerAge.append(records[z]) # place every customer with prompted name in temp database
                        if count5==0:
                            self.serverMsg = (str(records[z]))
                            count5+=1
                        else:
                            self.serverMsg += (str(records[z]))
                            count5+=1
                        self.serverMsg += "\n"
                    
                # send client the counter to create if statements
                self.wfile.write(str(count5).encode("utf-8"))
                
                # if count is 0, then customer does not exist
                if count5 == 0:
                    self.serverMsg = "Customer not found"
                    self.wfile.write(self.serverMsg.encode("utf-8"))
                    print(self.serverMsg)
                    
                # if count is 1, then only one customer with the prompted name exists
                elif count5 == 1:
                    # prompt user for new age
                    self.wfile.write("Customer found. Enter the age you want to change: ".encode("utf-8"))
                    self.newAge = str(self.rfile.readline().decode("utf-8").strip())
                    changeCustomerAge[0][1] = self.newAge # place modified age in temp
                    
                    # go through original database until the same prompted name, then pop old customer and insert modified customer
                    for w in range(len(records)):
                        if records[w][0] == self.aName:
                            records.pop(w)
                            records.insert(w, changeCustomerAge[0])
                            break
                    print("Change succesfully made!")
                    self.wfile.write("Change succesfully made!".encode("utf-8"))

                # if count is more than 1, then more than one customer with the prompted name exists
                else:
                    n = 1
                    # go through temp list 
                    for m in range(len(changeCustomerAge)):
                        if m == 0:
                            self.choose = (str(n) + ". " + str(changeCustomerAge[m][0]) + "|" + str(changeCustomerAge[m][1]) + "|"+ str(changeCustomerAge[m][2]) + "|"+ str(changeCustomerAge[m][3]))
                            n+=1
                        else:
                            self.choose += (str(n) + ". " + str(changeCustomerAge[m][0]) + "|" + str(changeCustomerAge[m][1]) + "|"+ str(changeCustomerAge[m][2]) + "|"+ str(changeCustomerAge[m][3]))
                            n+=1
                        self.choose+= "\n"

                    # print temp list of every customer, and prompt the user to choose between all with identical prompted name
                    self.choose += ( "Choose which one from 1 to " + str(count5))
                    self.wfile.write(str(self.choose).encode("utf-8"))
                    pick = str(self.rfile.readline().decode("utf-8").strip())

                    # prompt user for new age
                    self.wfile.write("Enter the age you want to change: ".encode("utf-8"))
                    self.newAge = str(self.rfile.readline().decode("utf-8").strip())
                    changeCustomerAge[int(pick)-1][1] = self.newAge

                    # go through original database until the same prompted name user picked
                    # and other info as to make sure it is the exact customer that is modified
                    # then pop old customer and insert modified customer
                    for v in range(len(records)):
                        if records[v][0] == self.aName and records[v][2] == changeCustomerAge[int(pick)-1][2] and records[v][3] == changeCustomerAge[int(pick)-1][3]:
                            records.pop(v)
                            records.insert(v, changeCustomerAge[int(pick)-1])
                            break
                    print("Change succesfully made!")
                    self.wfile.write("Change succesfully made!".encode("utf-8"))
###########################################################################################################################

            # if client chooses 5 to change address of customer
            if (self.choice == 5):

                # prompt the user for customer name
                self.wfile.write(("Customer you want to update: ".encode("utf-8")))
                self.aName = str(self.rfile.readline().decode("utf-8").strip())
                print("Customer to update: " + self.aName)
                
                count6 = 0
                changeCustomerAddress = [] # create a list with four elements of customer to modify

                # go through database to see every customer with the name the user prompted
                for z in range(len(records)):

                    if records[z][0] == self.aName:
                        changeCustomerAddress.append(records[z]) # place every customer with prompted name in temp database
                        if count6==0:
                            self.serverMsg = (str(records[z]))
                            count6+=1
                        else:
                            self.serverMsg += (str(records[z]))
                            count6+=1
                        self.serverMsg += "\n"
                    
                # send client the counter to create if statements
                self.wfile.write(str(count6).encode("utf-8"))
                
                # if count is 0, then customer does not exist    
                if count6 == 0:
                    self.serverMsg = "Customer not found"
                    self.wfile.write(self.serverMsg.encode("utf-8"))
                    print(self.serverMsg)
                    
                # if count is 1, then only one customer with the prompted name exists
                elif count6 == 1:
                    # prompt user for new address
                    self.wfile.write("Customer found. Enter the address you want to change: ".encode("utf-8"))
                    self.newAddress = str(self.rfile.readline().decode("utf-8").strip())
                    changeCustomerAddress[0][2] = self.newAddress # place modified address in temp
                    
                    # go through original database until the same prompted name, then pop old customer and insert modified customer
                    for w in range(len(records)):
                        if records[w][0] == self.aName:
                            records.pop(w)
                            records.insert(w, changeCustomerAddress[0])
                            break
                    print("Change succesfully made!")
                    self.wfile.write("Change succesfully made!".encode("utf-8"))

                # if count is more than 1, then more than one customer with the prompted name exists
                else:
                    n = 1
                    # go through temp list 
                    for m in range(len(changeCustomerAddress)):
                        if m == 0:
                            self.choose = (str(n) + ". " + str(changeCustomerAddress[m][0]) + "|" + str(changeCustomerAddress[m][1]) + "|" + str(changeCustomerAddress[m][2]) + "|" + str(changeCustomerAddress[m][3]) + "|")
                            n+=1
                        else:
                            self.choose += (str(n) + ". " +  str(changeCustomerAddress[m][0]) + "|" + str(changeCustomerAddress[m][1]) + "|" + str(changeCustomerAddress[m][2]) + "|" + str(changeCustomerAddress[m][3]) + "|")
                            n+=1
                        self.choose+= "\n"

                    # print temp list of every customer, and prompt the user to choose between all with identical prompted name
                    self.choose += ( "Choose which one from 1 to " + str(count6))
                    self.wfile.write(str(self.choose).encode("utf-8"))
                    pick = str(self.rfile.readline().decode("utf-8").strip())

                    # prompt user for new address
                    self.wfile.write("Enter the address you want to change: ".encode("utf-8"))
                    self.newAddress = str(self.rfile.readline().decode("utf-8").strip())
                    changeCustomerAddress[int(pick)-1][2] = self.newAddress

                    # go through original database until the same prompted name user picked
                    # and other info as to make sure it is the exact customer that is modified
                    # then pop old customer and insert modified customer
                    for v in range(len(records)):
                        if records[v][0] == self.aName and records[v][1] == changeCustomerAddress[int(pick)-1][1] and records[v][3] == changeCustomerAddress[int(pick)-1][3]:
                            records.pop(v)
                            records.insert(v, changeCustomerAddress[int(pick)-1])
                            break
                    print("Change succesfully made!")
                    self.wfile.write("Change succesfully made!".encode("utf-8"))
########################################################################################################################################################
                
            # if customer chooses 6 to change phone number of a customer
            if (self.choice == 6):
                # prompt the user for customer name
                self.wfile.write(("Customer you want to update: ".encode("utf-8")))
                self.aName = str(self.rfile.readline().decode("utf-8").strip())
                print("Customer to update: " + self.aName)
                
                count7 = 0
                changeCustomerPhonenb = [] # create a list with four elements of customer to modify

                # go through database to see every customer with the name the user prompted
                for z in range(len(records)):

                    if records[z][0] == self.aName:
                        changeCustomerPhonenb.append(records[z]) # place every customer with prompted name in temp database
                        if count7==0:
                            self.serverMsg = (str(records[z]))
                            count7+=1
                        else:
                            self.serverMsg += (str(records[z]))
                            count7+=1
                        self.serverMsg += "\n"
                    
                # send client the counter to create if statements
                self.wfile.write(str(count7).encode("utf-8"))
                
                # if count is 0, then customer does not exist
                if count7 == 0:
                    self.serverMsg = "Customer not found"
                    self.wfile.write(self.serverMsg.encode("utf-8"))
                    print(self.serverMsg)
                    
                # if count is 1, then only one customer with the prompted name exists
                elif count7 == 1:
                    # prompt user for new phone number
                    self.wfile.write("Customer found. Enter the phone number you want to change: ".encode("utf-8"))
                    self.newPNb = str(self.rfile.readline().decode("utf-8").strip())
                    changeCustomerPhonenb[0][3] = self.newPNb # place modified phone number in temp

                    # go through original database until the same prompted name, then pop old customer and insert modified customer
                    for w in range(len(records)):
                        if records[w][0] == self.aName:
                            records.pop(w)
                            records.insert(w, changeCustomerPhonenb[0])
                            break
                    print("Change succesfully made!")
                    self.wfile.write("Change succesfully made!".encode("utf-8"))

                # if count is more than 1, then more than one customer with the prompted name exists
                else:
                    n = 1
                    # go through temp list 
                    for m in range(len(changeCustomerPhonenb)):
                        if m == 0:
                            self.choose = (str(n) + ". " + str(changeCustomerPhonenb[m][0]) + "|" + str(changeCustomerPhonenb[m][1]) + "|" + str(changeCustomerPhonenb[m][2]) + "|" + str(changeCustomerPhonenb[m][3]) + "|")
                            n+=1
                        else:
                            self.choose += (str(n) + ". " + str(changeCustomerPhonenb[m][0]) + "|" + str(changeCustomerPhonenb[m][1]) + "|" + str(changeCustomerPhonenb[m][2]) + "|" + str(changeCustomerPhonenb[m][3]) + "|")
                            n+=1
                        self.choose+= "\n"

                    # print temp list of every customer, and prompt the user to choose between all with identical prompted name
                    self.choose += ( "Choose which one from 1 to " + str(count7))
                    self.wfile.write(str(self.choose).encode("utf-8"))
                    pick = str(self.rfile.readline().decode("utf-8").strip())

                    # prompt user for new phone number
                    self.wfile.write("Enter the phone number you want to change: ".encode("utf-8"))
                    self.newPNb = str(self.rfile.readline().decode("utf-8").strip())
                    changeCustomerPhonenb[int(pick)-1][3] = self.newPNb

                    # go through original database until the same prompted name user picked
                    # and other info as to make sure it is the exact customer that is modified
                    # then pop old customer and insert modified customer
                    for v in range(len(records)):
                        if records[v][0] == self.aName and records[v][2] == changeCustomerPhonenb[int(pick)-1][2] and records[v][1] == changeCustomerPhonenb[int(pick)-1][1]:
                            records.pop(v)
                            records.insert(v, changeCustomerPhonenb[int(pick)-1])
                            break
                    print("Change succesfully made!")
                    self.wfile.write("Change succesfully made!".encode("utf-8"))
#########################################################################################################################S

            # if client chooses 7 to print Python DB contents in alphabetical order
            if (self.choice == 7):
                records.sort() # sort database in alphabetical order

                self.report = "** Python DB contents **\n"
                for a in range(len(records)):
                    self.report += (str(records[a][0]) + "|" + str(records[a][1]) + "|" + str(records[a][2]) + "|" + str(records[a][3]) )
                    self.report += "\n"

                # print database
                print(self.report + "\n")
                # send database to client
                self.wfile.write(self.report.encode("utf-8"))


            # send to client the menu
            self.wfile.write(self.menu.encode("utf-8"))
            # print the menu
            print(self.menu)
            # received new choice value
            self.choice = int(self.rfile.readline().decode("utf-8").strip())
            # print choice value
            print(self.choice)

        # close data.txt file
        self.file.close()

        # send to client goodbye message
        self.wfile.write("Thank you for using our Python DB Menu Services. Good bye!".encode("utf-8"))
        print("Thank you for using our Python DB Menu Services. Good bye!")
       






if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    # Create the server, binding to localhost on port 9999
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()

