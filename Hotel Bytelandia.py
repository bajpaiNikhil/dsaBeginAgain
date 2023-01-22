
n = int(input())
arr = list(map(int ,input().split()))
dep = list(map(int ,input().split()))

# Combine the arrival and departure times into a single list
times = [(arr[i], 1) for i in range(n)] + [(dep[i], -1) for i in range(n)]
# Sort the list by time
print(times)
times.sort()
print(times)
maxGuests = 0
guests = 0
for time, change in times:
    guests += change
    maxGuests = max(maxGuests, guests)
print(maxGuests)