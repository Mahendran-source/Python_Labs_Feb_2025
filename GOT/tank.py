#! /usr/bin/env python3
# Author: Mahendran
# Description: This module describe a Class of Tank
"""
    Tank class for - Game of Tanks
"""

class Tank:
    # Attributes/Data + Behaviour/Methods
    def __init__(self, country, model):
        self.country = country
        self.model = model
        self._speed = 0
        self._location = {'x':0, 'y':0, 'z':0}
        self._direction = 0
        self._shells = 20
        self._health = 100
        # No Explicit Return, as called implicitly.

    def accel(self, increase):
        self._speed += increase
        return None

    def decel(self, decrease):
        self._speed -= decrease
        return None

    def rotate_left(self, degree):
        self._direction -= degree % 360
        return None

    def rotate_right(self, degrees):
        self._direction += degrees % 360
        return None

    def shoot(self):
        self._shells -= 1
        return None

    def take_damage(self, damage):
        self._health -= damage
        return None

    # Some special methods
    # Example of OPERATOR overloading

    def __add__(self, other):
        return self._health + other._health

    def __del__(self):
        print("Boom...Boom...Boom...!!!")
        return None

    # Example of GETTER and SETTER method.

    def get_health(self):
        return self._health

    def set_health(self, newhealth):
        self._health = newhealth
        return None

    # Wrap access to the getter and setter ONE variable name interface
    tank_health = property(get_health, set_health)

    # Alternative using DECORATORS !
    @property
    def tank_health(self):
        return self._health

    @tank_health.setter
    def tank_health(self, newhealth):
        self._health = newhealth
        return None









