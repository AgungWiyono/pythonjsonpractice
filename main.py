from jsondata.models import data

proccess = data()

choice = input("Apakah anda ingin memasukkan data baru (y/n)? ")
if choice.lower() == 'y':
    name = input("Masukkan nama  : ")
    age = input("Masukkan usia : ")
    gender = input("Masukkan jenis kelamin : ")
    proccess.save_data(name,age,gender)

print("Data member : ")
print('')
proccess.show_data()