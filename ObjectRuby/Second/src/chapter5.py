from trip import Trip
from mechanic import Mechanic
from trip_coordinator import TripCoordinator
from driver import Driver
from bicycle import Bicycle
from customer import Customer
from vehicle import Vehicle

if __name__ == "__main__":
    my_bicycles = [Bicycle(), Bicycle(), Bicycle()]
    my_family = [Customer(), Customer(), Customer(), Customer(), Customer()]
    my_vehicle = Vehicle()
    my_trip = Trip(my_bicycles, my_family, my_vehicle)
    prepares = [Mechanic(), TripCoordinator(), Driver()]
    print("--- 処理前 ---")
    print(my_trip)
    my_trip.prepare(prepares)
    print("--- 処理後 ---")
    print(my_trip)
