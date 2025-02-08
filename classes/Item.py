class Item:
    def __init__(self, item_data, position):
        self.__name = item_data['name']
        self.__price1 = item_data['price1']
        self.__price2 = item_data['price2']
        self.__price3 = item_data['price3']
        self.__price4 = item_data['price4']
        self.__position = position
        self.__star = None

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def price(self):
        return self.__price1
    
    @property
    def position(self):
        return self.__position
    
    @property
    def star(self):
        return self.__star
    
    @property
    def bottom_right_position(self):
        return (self.__position[0] + 70, self.__position[1] + 70)
    
    def is_equal_to(self, other):
        tolerance = 10
        x, y = self.__position
        other_x, other_y = other.position
        return (
            x < other_x + tolerance and x > other_x - tolerance
            and
            y < other_y + tolerance and y > other_y - tolerance
        )