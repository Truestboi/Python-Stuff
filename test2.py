#if number is even, we skip it
ages = [5, 12, 3, 56, 24, 78, 1, 15, 44]

#sort ages (optional)
ages.sort()

#add all the ages together
total = sum(ages)

#divide added by the number of positions
average = (total / (len(ages)))

print(average)
