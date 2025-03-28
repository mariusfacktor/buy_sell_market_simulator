
import requests
import random

url = 'http://127.0.0.1:5000/'

# random.seed(8)

names = ['Martin Tubins', 'Ryan Loaf', 'Andrew Harrington', 'Alicia Kind', 'Zara Barns', 'Trisha Hansen', 'Drake Reiner', 'Peter Thames', 'Thomas Bing',
        'George Christianson', 'Mary Eiger', 'Ronda Meere', 'Barney Opinheimer', 'Rick Zork', 'Walter Moon', 'Simon Baxter', 'Susan Nelson', 'Ed Yon',
        'Charlie Young', 'Mandy Poppins', 'Jon Phelps', 'Harry Platter', 'Sven Beans', 'Donna Waters', 'Neal Borgswith', 'Torance Miller', 'Rod Fried',
        'Ralph Gibbons', 'Scooter Coolidge', 'Jim Roberts', 'Ripley James', 'Ashley Summers', 'Andy Florence', 'Vanessa Craw', 'Ted Moe', 'Tia Alfred']

resources = ['apple', 'orange', 'tomato']


def create_person():
    name = names[random.randint(0, len(names) - 1)]
    cash = random.randint(100, 1000)
    resource_dict = {}

    for resource in resources:
        if random.randint(0, 1):
            resource_dict[resource] = random.randint(0, 60)

    data = {'name': name, 'cash': cash, 'resource_dict': resource_dict}

    response = requests.post(url + 'create_person', json=data)
    print(response.json())

    return name


def sell(name):

    resource_type = resources[random.randint(0, len(resources) - 1)]
    amount = random.randint(1, 30)
    price = random.randint(1, 15)

    data = {'name': name, 'resource_type': resource_type, 'amount': amount, 'price': price}

    response = requests.post(url + 'sell', json=data)
    print(response.json())


def buy(name):

    resource_type = resources[random.randint(0, len(resources) - 1)]
    amount = random.randint(1, 15)

    data = {'name': name, 'resource_type': resource_type, 'amount': amount}

    response = requests.post(url + 'buy', json=data)
    print(response.json())



def examples(num_iter=1):
    existing_names = []

    for i in range(num_iter):

        name = create_person()
        existing_names.append(name)

        sell(name)
        sell(name)
        buy(name)
        print('')



def main():

    num_iter = 200

    examples(num_iter)





if __name__ == '__main__':
    main()





















