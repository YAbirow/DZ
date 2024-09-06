my_dict = {"Vlad":2003}
print(my_dict)
print(my_dict.pop("Vlad"))
print(my_dict.get("inton"), "Такой переменной нет")

my_dict.update({"Ignat":2004,
                "Igor":2005})

print(my_dict)


my_set = {1,2,3,4,5,32421}
print(my_set)
my_set.update({1,2,3,4,5,32421,
               1,3})
print(my_set.discard(3))
print(my_set)