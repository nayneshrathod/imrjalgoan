# # Health
# # Management
# # System
# client_list = {1: "Harry", 2: "Rohan", 3: "Hammad"}
# lock_list = {1: "Exercise", 2: "Diet"}
#
#
# def getdate():
#     import datetime
#     return datetime.datetime.now()
#
#
# try:
#     print("Select Client Name:")
#     for key, value in client_list.items():
#         print("Press", key, "for", value, "\n", end="")
#     client_name = int(input())
#
#     print("Selected Client : ", client_list[client_name], "\n", end="")
#
#     print("Press 1 for Lock")
#     print("Press 2 for Retrieve")
#     op = int(input())
#
#     if op is 1:
#         for key, value in lock_list.items():
#             print("Press", key, "to lock", value, "\n", end="")
#         lock_name = int(input())
#         print("Selected Job : ", lock_list[lock_name])
#         f = open(client_list[client_name] + "_" + lock_list[lock_name] + ".txt", "a")
#         k = 'y'
#         while (k is not "n"):
#             print("Enter", lock_list[lock_name], "\n", end="")
#             mytext = input()
#             f.write("[ " + str(getdate()) + " ] : " + mytext + "\n")
#             k = input("ADD MORE ? y/n:")
#             continue
#         f.close()
#     elif op is 2:
#         for key, value in lock_list.items():
#             print("Press", key, "to retrieve", value, "\n", end="")
#         lock_name = int(input())
#         print(client_list[client_name], "-", lock_list[lock_name], "Report :", "\n", end="")
#         f = open(client_list[client_name] + "_" + lock_list[lock_name] + ".txt", "rt")
#         contents = f.readlines()
#         for line in contents:
#             print(line, end="")
#         f.close()
#     else:
#         print("Invalid Input !!!")
# except Exception as e:
#     print("Wrong Input !!!")
#
#
#
# A = [[1, 4, 5, 12],
#     [-5, 8, 9, 0],
#     [-6, 7, 11, 19]]
# print("A =", A)
# print("A[1] =", A[1])      # 2nd row
# print("A[1][2] =", A[1][2])   # 3rd element of 2nd row
# print("A[0][-1] =", A[0][-1])   # Last element of 1st Row
# column = [];        # empty list
# for row in A:
#   column.append(row[2])
# print("3rd column =", column)

# Open a file
fo = open("demo1.py", "r+")
str = fo.readlines(5);
print("Read String is : ", str)
# Close opend file
fo.close()
lis =[]
for i in range(1,4):
    for j in range(1,4):
        lis[[i][j]]

print(lis)