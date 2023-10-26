import functools


class Robot:
    __count = 0
    def __init__(self, x: int, y: int) -> None:
        Robot.__count+=1
        self._x = x
        self._y = y
        self.__path = [(x,y)]
    
    @classmethod
    def countOfRobots(cls):
        return cls.__count
     
    # @property
    # def x(self):
    #     return self._x
    # @property
    # def y(self):
    #     return self._y

    def logger(f):
        @functools.wraps(f)
        def wrapper(self,*args, **kwargs):
            res = f(self,*args, **kwargs)
            if len(self.__path)-1 < len(args[-1]):
                print("При перемещении встречено препятствие!")
            else:
                print("Перемещение окончено успешно.")
            return res
        return wrapper

    def __str__(self) -> str:
        return f'Robot ({self._x}, {self._y})'
    
    @logger
    def move(self, s: str):
        x,y = self._x,self._y
        path = [(x,y)]
        for i in s:
            try:
                match i:
                    case 'N':
                        if y < 100: y+=1
                        else: raise ValueError()
                    case 'S':
                        if y > 0: y-=1
                        else: raise ValueError()
                    case 'E':
                        if x < 100: x+=1
                        else: raise ValueError()
                    case 'W':
                        if x > 0: x-=1
                        else: raise ValueError()
                path.append((x,y))
            except ValueError:
                self.__path = path
                self._x,self._y = x,y
                return (x,y)
        self.__path = path
        self._x,self._y = x,y
        return (x,y)

    def path(self):
        return self.__path

    def getDirectionsTO(self, x: int, y: int) -> list:
        path = []
        path+= (['E','W'][self._x < x])*abs(self._x-x)
        path+= (['S','N'][self._y < y])*abs(self._y-y)
        return path
    
    def isAtBoundary(self) -> bool:
        if self._x in [0,100] or self._y in [0,100]:
            return True
        return False

    def getAdjacentCoordinates(self) -> list:
        x,y = self._x, self._y
        res = []
        for i in range(x-1,x+2):
            for j in range(y-1,y+2):
                if i in [-1,101] or j in [-1,101] or i == x and j == y:
                    continue
                res.append((i,j))
        return res


class RobotHelper(Robot):
    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y)
    def __str__(self) -> str:
        return f'RobotHelper ({self._x}, {self._y})' 
    
    # очень полезный декоратор
    def help(f):
        def wrapper(*args, **kwargs):
            print('Если что я помогаю...')
            return f(*args, **kwargs)
        return wrapper
    
    # легальное добавление декоратора к методам
    # @help
    # def move(self, s: str):
    #     return super().move(s)
    

# нелегальное добавление декоратора ко всем методам(так нельзя делать никогда, а то посадят)
for attr_name in Robot.__dict__:
    if attr_name.startswith('__'): # skip magic methods
        continue
    attr = getattr(Robot, attr_name)
    if callable(attr):
        setattr(RobotHelper, attr_name, RobotHelper.help(attr))


def main():

    r = Robot(0,0)
    print(str(r))
    print(r.move('NSEW'))
    print(r.path())
    print(r.isAtBoundary())
    print(r.getAdjacentCoordinates())
    print(r.getDirectionsTO(10,10))

    print()

    rh = RobotHelper(10,0)
    print(str(rh))
    print(rh.move('WNN'))
    print(rh.path())
    print(rh.isAtBoundary())
    print(rh.getAdjacentCoordinates())
    print(rh.getDirectionsTO(10,2))

    print(f'\nКоличество роботов: {Robot.countOfRobots()}')




if __name__ == '__main__':
    main()



# Класс «Робот» «Robot»

# Класс инициализируется начальными координатами положением Робота на плоскости, 
# обе координаты заключены в пределах от 0 до 100.
# Робот может передвигаться на одну клетку вверх (N), вниз ($), вправо (Е), влево (W).
# Выйти за границы плоскости Робот не может.

# Метод move() принимает строку - последовательность команд,
# перемещения робота, каждая буква строки соответствует перемещению на единичный
# интервал в направлении, указанном буквой. Метод возвращает список координат —
# конечное положение Робота после перемещения.

# Метод раth() вызывается без аргументов и возвращает список координат
# точек, по которым перемещался Робот при последнем вызове метода move. Если
# метод не вызывался, возвращает список с начальным положением Робота.

# Метод isAtBoundary(): проверяет, находится ли робот на границе плоскости.

# Метод getAdjacentCoordinates(): возвращает список координат, смежных с
# текущим положением робота.

# Метод getDirectionsTo(): возвращает список направлений, необходимых для
# перемещения от текущих координат робота до указанных.

# Создать класс-наследник от класса «Робот», например, «Робот-помощник».

# Обязательно использование конструктора, декораторов и метода __str__.