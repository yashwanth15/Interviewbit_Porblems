import os

packages = []

with open('packages.txt', 'r') as file:
    data = file.read()
    splitted_data = data.split('\n')
    for i in range(2, len(splitted_data)-3):
        package = splitted_data[i].strip()[:-1]
        packages.append(package)

for package in packages:
    print('Trying to install ', package)
    command = 'pip install ' + package
    os.system(command)
    print()
    