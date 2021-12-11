import time

print("Welcome to 'save logins' program!")
time.sleep(0.6)
next_dataset = input("Would like to write new datasets? yes/no: ")

while next_dataset=="yes":
    f = open("logindata.txt", "a")

    service = input("Enter service: ")
    username = input("Enter username: ")
    password = input("Enter password: ")
    

    f.write(service+"\n")
    f.write(username+"\n")
    f.write(password+"\n")
    f.write("\n")

    next_dataset = input("Would you like to save another login dataset? yes/no: ")
else:
    print("Entered logins are saved!")
    time.sleep(0.5)
    readout_logins = input("Would you like to read out your current logins? yes/no: ")
    if readout_logins == "yes":
        f = open("logindata.txt", "r")
        content = f.read()
        print(content)
    