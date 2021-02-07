from datetime import datetime


class CarFactoryIterator:
    """The class for iterating cars """

    def __init__(self, lot):
        self.lot = lot

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.lot) == 0:
            raise StopIteration
        return self.lot.pop(0)


class CarFactory:
    """ The class for iterating the cars  """

    def __init__(self, cars_number: int, serial_number: int):
        self.serial_l = []
        self.lot_l = []
        self.day = datetime.now()
        self.serial_l.append(serial_number)
        self.lot_number = serial_number // 20
        for i in range(1, cars_number + 1):
            self.serial_l.append(serial_number + i)
        for j in range(1, cars_number + 2, 20):
            self.lot_number += 1
            self.lot_l.append(self.lot_number)

    def right_side_driving(self) -> list:
        list_right_side = []
        for i in self.serial_l:
            if i % 2 != 0:
                list_right_side.append(i)
        return list_right_side

    def left_side_driving(self):
        list_left_side = []
        for i in self.serial_l:
            if i % 2 != 1:
                list_left_side.append(i)
        return list_left_side

    def __iter__(self):
        return CarFactoryIterator(self.lot_l)


cars = CarFactory(111, 91)
print("Serial number list: ", cars.serial_l)
print("Lot car list: ", cars.lot_l)
print("driving on the right: ", cars.right_side_driving())
print("driving on the left: ", cars.left_side_driving())


f = open("homework6.txt", "x")
for i in cars:
    f.write(str(i))
    f.write("\n")