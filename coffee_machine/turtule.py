# from turtle import Turtle, Screen
# timmy = Turtle()
#
# timmy.shape("turtle")
# timmy.color("coral")
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()
#
from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ["A", "B", "C"])
table.add_column("Type", ["x", "y", "z"])
print(table)