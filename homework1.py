grades = [
    [5, 3, 3, 5, 4],
    [2, 2, 2, 3],
    [4, 5, 5, 2],
    [4, 4, 3],
    [5, 5, 5, 4, 5],
    [2, 2, 2, 2],

]

users1 = {
    'Johnny',
    'Bilbo',
    'Steve',
    'Khendrik',
    'Aaron',
    'Test'
}

list_ = sorted(list(users1))

print(sorted(list_))


average_grade = []

for val in grades:
    print(sum(val)/len(val))

print(average_grade)


dict_ = dict(zip(list_, average_grade))

print(dict_)



users = [
    {
        "name": "Carl",
        "age": 18
    },
    {
        "name": "John",
        "age": 20
    },
    {
        "name": "Vano",
        "age": 21
    },
    {
        "name": "Petr",
        "age": 22
    },
    {
        "name": "Alex",
        "age": 44
    },

]


for user in users:
    print(user)