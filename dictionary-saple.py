students = {}

number = input("Öğrenci no : ")
name = input("Öğrenci adı: ")
surname = input("Öğrenci soyad: ")
phone = input("Öğrenci telefon:" )

students[number] = {
    'ad': name,
    'soyad': surname,
    'telefon': phone,
}

print(f'Elklediğiniz {number} nolu öğrencinin adı : {name} soyadı: {surname} ve telefon ise {phone}')