import json
import datetime


# function to load clients from the json file
def load_clients():
    #open file (in read mode by default)
    with open('clients.json') as file:
        #load JSON data from the file
        data = json.load(file)
    return data['clients']


# Function save clients to the json file
def save_clients(clients):
    
    with open("clients.json","w") as file:
        json.dump({'clients': clients}, file)

def get_age(dob):
    # convert the dob from string to datetime object
    dob = datetime.datetime.strptime(dob, '%Y-%m-%d')
    # get current date
    today = datetime.datetime.today()
    #calculation
    age = today.year - dob.year
    return age
    

def add_client(clients, name, dob, balance):
    # determining id of last client
    client_id = clients[-1]["client_id"] + 1
    # adding new client
    clients.append({
        "client_id":client_id,
        "name":name,
        "dob":dob,
        "balance":balance
    })
    #saving updated clients list to JSON file
    save_clients(clients)
    

def update_client(clients, client_id, name=None, dob=None, balance=None):
    #loop through client list
    for client in clients:
        # select client by id
        if client['client_id'] == client_id:
            # if name is provided, update clients name

            if name:
                client['name'] = name
                #if dob is provided, update clients dob
            if dob:
                client['dob'] = dob
                #if balance is provided, update clients balance
            if balance:
                client['balance'] = balance
            break
    # save updated clients list to JSON file
    save_clients(clients)


def delete_client(clients, client_id):
    
    for client in clients:
        if client['client_id'] ==client_id:
            # delete client
            del client
            # end loop to avoid unnecessary looping
            break
    # save updated client list to JSON
    save_clients(clients)

def display_client(clients, client_id):
    
    for client in clients:
        if client['client_id'] == client_id:

            print(f'Client ID {client["client_id"]}')
            print(f'Client Name {client["name"]}')
            print(f'Client DOB {client["dob"]}')
            print(f'Client Age {get_age(client["dob"])}')
            print(f'Client ID {client["client_id"]}')
#Function to display the total amount of money in the bank
def display_total(clients):
    # Calculate the total balance by adding the balance of each client
    total = sum(client['balance'] for client in clients)
    #Print the total balance
    print('Total bank balance: ', total)


##
#print(get_age("1996-03-25"))

#clients = load_clients()
#add_client(clients, "Igor", "1980-04-01", 14)