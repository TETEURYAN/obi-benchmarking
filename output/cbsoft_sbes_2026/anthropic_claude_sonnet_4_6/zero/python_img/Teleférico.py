import math

C = int(input())
A = int(input())

# Each trip can carry at most C-1 students (1 monitor required)
students_per_trip = C - 1
print(math.ceil(A / students_per_trip))