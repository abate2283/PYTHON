students = {"Jane", "John", "Joseph", "Jacob"}
staffs = {"Matthew", "Mark", "Marylin", "John"}
Not_students = students.difference(staffs)
Not_staffs = staffs.difference(students)
print(Not_students)
print(Not_staffs)
# This will print the difference. If an item is in both.
Not_in_both = staffs.symmetric_difference(students)
# This will print those who are not in both
print(Not_in_both)
students_and_staffs = staffs.intersection(students)
print(students_and_staffs)
AB = students.union(staffs)
print(AB)

cd = students.intersection(AB)
print(cd)
# QUIZZ 6
set_one = {1, 2, 3, 4, 5}
set_two = {1, 3, 5, 7, 9, 11}
set_three = set_one.intersection(set_two)
print(set_three)

Our_friends = {"Alan", "Bob", "Cox"}
userB = input("Enter your friend's name? ")
user_friends = Our_friends.add(userB)
print(Our_friends.intersection(user_friends))