class Vehicle(object):
    """docstring"""

    def __init__(self, color, doors, tires, vtype):
        """Constructor"""
        self.color = color
        self.doors = doors
        self.tires = tires
        self.vtype = vtype

    def brake(self):
        """
        Останови машину
        """
        return "%s тормозит" % self.vtype

    def drive(self):
        """
        Вести машину
        """
        return "Я за рулем %s %s!" % (self.color, self.vtype)


if __name__ == "__main__":
    car = Vehicle("голубой", 5, 4, "машины")
    print(car.brake())
    print(car.drive())

    truck = Vehicle("красного", 3, 6, "грузовика")
    print(truck.drive())
    print(truck.brake())
