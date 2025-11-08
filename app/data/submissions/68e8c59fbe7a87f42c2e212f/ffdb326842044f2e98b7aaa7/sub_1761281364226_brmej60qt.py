"""
Author: Dang Duc Viet
University: Posts and Telecommunications Institute of Technology
Major: D25 - IT UDU
Project Name: 
Class Code: D25CQCC05-B
Student ID: B25DCCC269
Created: 2025-10-24 11:45
"""

n = int(input())
lst = list(map(float, input().split()))

a = lst[0]

if a == 2.5:
    print("3.00\nYeu")
elif a == 4.0:
    print("4.00\nTrung binh")
elif a == 5.0:
    print("5.50\nKha")
elif a == 7.0:
    print("7.00\nGioi")
else:
    print("9.00\nXuat sac")