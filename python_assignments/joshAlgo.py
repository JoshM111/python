# nums = [6,8,9,3]

# for i in range(0, len(nums)):
#     print(nums[i])

# for x in nums:
#     print(x)

# arr = [4, 6, 7] #list
# print(arr[1])

# obj = {"color": "purple", "smell": "lilac"} #dictionary
# print(obj["smell"])

students = [
    {'first_name': "Tyler", "last_name": "Smith", "list": [9,7,5]},
    {'first_name': "Bob", "last_name": "Jones"}
]

# for student in students:
#     print(student['first_name'])
#              name_of_dict[key] => value

for student in students:
    print(student)
    for key, val in student.items(): #could also use .keys() or .values()
        print("*****")
        print(key)
        #print(student[key])
        print(val)
        print("*****")