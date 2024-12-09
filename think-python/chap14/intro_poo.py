# class and functions 
class Time:
    """represents a time of day"""

# creating a new object is "instanciation" and the object is a instance of the class
lunch = Time()
print(type(lunch))
print(lunch)

# attributes
lunch.hour=11
lunch.minute=59
lunch.second=1

# an state diagram which shows the objects and its attributes its called "object diagram"

print(lunch.hour)

total_minutes = lunch.hour * 60 + lunch.minute
print(total_minutes)

print(f"{lunch.hour}:{lunch.minute:02d}:{lunch.second:02d}")

def print_time(time):
    s = f'{time.hour}:{time.minute:02d}:{time.second:02d}'
    print(s)

print_time(lunch)

def make_time(hour, minute, second):
    time = Time()
    time.hour=hour 
    time.minute=minute
    time.second=second
    return time

time=make_time(11,59,1)
print_time(time)

## objects are mutable
start = make_time(9, 20, 0)
print_time(start)

start.hour += 1
start.minute += 32
print_time(start)

def increment_time(time, hours, minutes, seconds):
    time.hour+=hours
    time.minute+=minutes 
    time.second+=seconds

start = make_time(9, 20, 0)
increment_time(start, 1, 32, 0)
print_time(start)

from copy import copy

start=make_time(9, 20, 0)
end = copy(start)

print_time(start)
print_time(end)
print(start is end)

