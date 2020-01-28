#!/usr/bin/python3

""" Base module """

import json
import csv
import turtle


class Base:
    """ Base class """

    __nb_objects = 0

    def __init__(self, id=None):
        """ instantiates the Base class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns JSON representation of a list of dict """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON representation of list_objs to a file"""
        if list_objs is None:
            with open("{}.json".format(cls.__name__), 'w') as f:
                f.write("[]")
                f.close()
        else:
            json_list = []
            with open("{}.json".format(cls.__name__), 'w') as f:
                for item in list_objs:
                    json_list.append(item.to_dictionary())

                string = cls.to_json_string(json_list)
                f.write(string)
                f.close()

    @staticmethod
    def from_json_string(json_string):
        """ Returns a list of the str repr json_string"""
        new_list = []
        if json_string is None or len(json_string) == 0:
            return new_list
        else:
            new_list = json.loads(json_string)
            return new_list

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes all set """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        a_file = str(cls.__name__) + ".json"
        try:
            with open(a_file, encoding="utf-8") as f:
                instances = []
                ln = f.read()
                dictionary = cls.from_json_string(ln)
                for item in dictionary:
                    instances.append(cls.create(**item))
                return instances
        except:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ CSV """
        if cls.__name__ == "Rectangle":
            fieldnames = ["id", "width", "height", "x", "y"]
        if cls.__name__ == "Square":
            fieldnames = ["id", "size", "x", "y"]
        with open("{}.csv".format(cls.__name__), 'w', newline='') as f:
            writer = csv.DictWriter(f, delimiter=',', fieldnames=fieldnames)
            [writer.writerow(item.to_dictionary()) for item in list_objs]

    @classmethod
    def load_from_file_csv(cls):
        """ CSV """
        a_file = cls.__name__ + ".csv"
        if cls.__name__ == "Rectangle":
            fieldnames = ["id", "width", "height", "x", "y"]
        if cls.__name__ == "Square":
            fieldnames = ["id", "size", "x", "y"]
        with open(a_file, encoding="utf-8") as f:
            reader = csv.DictReader(f, fieldnames=fieldnames)
            instances = []
            new_dict = {}
            for item in reader:
                for key in item:
                    new_dict[key] = int(item[key])
                instances.append(cls.create(**new_dict))
            return instances

    def draw(list_rectangles, list_squares):
        """ draws with turtle python module"""
        for rectangle in list_rectangle:
            turtle.shape('turtle')
            turtle.screensize(600,600)
            turtle.penup()
            turtle.setpos(-280,280)
            turtle.pendown()
            turtle.color("red")
            turtle.forward(rectangle.width)
            turtle.right(90)
            turtle.forward(rectangle.height)
            turtle.right(90)
            turtle.forward(rectangle.width)
            turtle.right(90)
            turtle.forward(rectangle.height)
            turtle.setheading(0)
            turtle.penup()
            turtle.setpos(rectangle.width + 20 + rectangle.x, 280)
            turte.pendown()

        for square in square:
            turtle.shape('turtle')
            turtle.screensize(600,600)
            turtle.penup()
            turtle.setpos(-280,280)
            turtle.pendown()
            turtle.color("red")
            turtle.forward(square.width)
            turtle.right(90)
            turtle.forward(square.width)
            turtle.right(90)
            turtle.forward(square.width)
            turtle.right(90)
            turtle.forward(square.width)
            turtle.setheading(0)
            turtle.penup()
            turtle.setpos(square.width + 20 + rectangle.x, 280)
            turte.pendown()

        turtle.getscreen()._root.mainloop()
