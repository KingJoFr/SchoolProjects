import time

n = 500000
print("List Comprehensions vs. For Loops")
 
# Calculate time taken by for loop
begin1 = time.time()
result1 = []
for i in range(n):
    result1.append(i**2)
end1 = time.time()
 
# Time taken by for
print('\nTime taken bny the for loop:', round(end1-begin1, 2))
 
# Calculate time taken by list comprehension
begin2 = time.time()
result2 = []
result2 = [i**2 for i in range(n)]
end2 = time.time()

# Time taken by comprehension
print('\nTime taken by the list comprehension:', round(end2-begin2, 2))

print('\nPercent savings by comprehension: ', round(100*(end1-begin1 - (end2-begin2))/(end1-begin1),2),"%", sep = "")