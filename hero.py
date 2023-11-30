from tkinter import Tk, Canvas, ARC, W
from human import Human


class Hero(Human):
    def __init__(self, canvas, name, x, y, gen, h):
        super().__init__(canvas, name, x, y, gen)
        self.health = h
        self._wp = None

        self.health_bar_width = 100
        self.health_bar_height = 10
        self.health_bar_x = self.x + 1.5
        self.health_bar_y = self.y - 300
        self.health_bar_color = "red"
        self.health_bar2_y = self.y - 300
        self.dead_color = "white"


    def _DrawName(self):
        super()._DrawName()
        self.canvas.create_rectangle(self.health_bar_x,
                                     self.health_bar_y,
                                     self.health_bar_x + 100,
                                     self.health_bar_y + self.health_bar_height,
                                     fill=self.dead_color)
        self.canvas.create_rectangle(self.health_bar_x,
                                     self.health_bar_y,
                                     self.health_bar_x + self.health,
                                     self.health_bar2_y + self.health_bar_height,
                                     fill=self.health_bar_color)



    def setWeapon(self, weapon):
        self._wp = weapon

    def attack (self, enemy):
        damage = self._wp.hit()
        enemy.health -= damage
        print(f'{self._name} нанес(ла) {damage} урона {enemy._name}!')
        print(f'у {enemy._name} осталось {enemy.health} здоровья')




    def _drawWeapon(self):
        self._wp.display(self.x+80, self.y-100)

    def display(self):
        super().display()
        self._drawWeapon()








