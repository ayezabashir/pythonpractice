# to insert a new item without replacing existing values

# INSERT()
fruits= ["apple", "banana", "oranges"]
fruits.insert(1,"watermelon")
print(fruits)

# APPEND()  add item at the end of the list
fruits.append("melon")
print(fruits)

# EXTEND() to append elements from other lists
sibling = ["aqsa", "ayesha", "mariam"]
parents = ["bushra"]
parents.extend(sibling)
sibling.extend(parents)
print(parents)