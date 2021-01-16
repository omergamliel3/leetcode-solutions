BIG = 1
MEDUIM = 2
SMALL = 3


class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self._big = big
        self._medium = medium
        self._small = small

    def addCar(self, carType: int) -> bool:
        if carType not in [1, 2, 3]:
            return False
        if carType == SMALL:
            if self._small >= 1:
                self._small -= 1
                return True
        elif carType == MEDUIM:
            if self._medium >= 1:
                self._medium -= 1
                return True
        elif carType == BIG:
            if self._big >= 1:
                self._big -= 1
                return True
        
        return False


def main():
    parking_system = ParkingSystem(1, 1, 0)
    result = parking_system.addCar(1)
    print(result)


if __name__ == "__main__":
    main()
