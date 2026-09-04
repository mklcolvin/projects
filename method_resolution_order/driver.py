# TODO: Import all required classes
# from device import Device
# from screen import Screen
# from computer import Computer
# from laptop import Laptop
from device import Device
from screen import Screen
from computer import Computer
from laptop import Laptop

def explain_mro(class_name):
    # TODO: Print the MRO (Method Resolution Order) for the given class
    # TODO: Format: "MRO for [class name]:" (note: NO space after the colon)
    # TODO: Use class_name.__name__ to get the name of the class
    # TODO: Use class_name.__mro__ to get the MRO tuple
    # TODO: Print each class name in the MRO on separate lines
    
    # TODO: Create an instance of the class
    # TODO: Call power_on() on the instance and store the result
    # TODO: Print: "Power on result: [result]"
    # TODO: Print an empty line for better readability
    print(f"MRO for {class_name.__name__}:")
    for cls in class_name.__mro__:
        print(cls.__name__)
    instance = class_name()
    result = instance.power_on()
    print(f"Power on result: {result}")


# Test your code
# TODO: Call explain_mro() with each class: Device, Screen, Computer, and Laptop
explain_mro(Device)
print()
explain_mro(Screen)
print()
explain_mro(Computer)
print()
explain_mro(Laptop)