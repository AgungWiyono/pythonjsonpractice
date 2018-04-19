import json

# testing function to check is the module connected properly
def testing():
    print ('This package work')

class data:

    def __str__(self):
        return('The name is {}, he is {} years old {}'.format(self.name, self.age, self.gender))

    def save_data(self,name,age,gender):
        name = name
        age = age
        gender = gender
        data = {'name': name, 'age': age, 'gender': gender}
        with open('jsondata/data.txt', 'a') as file:
            file.write('\n')
            json.dump(data, file, sort_keys=True)

    def show_data(self):
        with open('jsondata/data.txt') as file:
            for x,i in enumerate(file):
                data = json.loads(i)
                print("{}. The name is {}, He is a {} old {}".format(x+1,data['name'], data['age'], data['gender']))