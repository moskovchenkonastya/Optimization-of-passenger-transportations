import string 


# Variables initialization
# Coordinates
class Point:
    def __init__(self, x = 0, y = 0):
        self.x, self.y = x, y
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    def __lt__(self, other):
        return self.x < other.x or self.x == other.x and self.y < other.y

class Time:
    def __init__(self, start = 0, end = 0):
        self.start, self.end = start, end    

# Bus
class Bus:
    def __init__(self, count, time, cost):
        self.capacity = count
        self.minTime  = time
        self.costRent = cost

# Depo
class Depo(Point):
    
# Order
class Order(Poin, Time):
    def __init__(self, numPas):
        self.numPassenger = numPas
        //self.x = startPoint
    def time(self, startTime, endTime):
        self.start, self.end = startTime, endTime
    def coordinates(self, startPoint, endPoint)
        self.startPoint, self.endPoint = startPoint, endPoint

# optimization
def main():
    # считывание данных 
    # считывание данных с api
    # optinization 

    