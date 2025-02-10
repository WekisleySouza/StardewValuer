class Item:
    def __init__(self, item_data, position):
        self.__name = item_data['name']
        self.__price1 = item_data['price1']
        self.__price2 = item_data['price2']
        self.__price3 = item_data['price3']
        self.__price4 = item_data['price4']
        self.__quantity = 1
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
        if self.__star == 'silver':
            return self.__price1 * 1.25 * self.__quantity
        elif self.__star == 'gold':
            return self.__price1 * 1.5 * self.__quantity
        elif self.__star == 'iridium':
            return self.__price1 * 2 * self.__quantity
        elif self.__star == 'unknown':
            return self.__price1 * self.__quantity
    
    @property
    def quantity(self):
        return self.__quantity
    
    @quantity.setter
    def quantity(self, value: int):
        self.__quantity = value
    
    @property
    def position(self):
        return self.__position
    
    @property
    def star_color(self):
        if self.__star == 'silver':
            return (255, 255, 255)
        elif self.__star == 'gold':
            return (0, 255, 255)
        elif self.__star == 'iridium':
            return (128, 0, 128)
        elif self.__star == 'unknown':
            return (0, 0, 0)
    
    @property
    def star(self):
        return self.__star
    
    @star.setter
    def star(self, value: str):
        self.__star = value
    
    @property
    def bottom_right_position(self):
        return (self.__position[0] + 70, self.__position[1] + 70)
    
    @property
    def star_top_left_position(self):
        return (self.__position[0]+5, self.__position[1] + 50)
    
    @property
    def star_bottom_right_position(self):
        return (self.__position[0] + 15, self.__position[1] + 60)
    
    @property
    def number_top_left_position(self):
        return (self.__position[0] + 20, self.__position[1] + 40)
    
    @property
    def number_bottom_right_position(self):
        return (self.__position[0] + 70, self.__position[1] + 75)
    
    def is_equal_to(self, other):
        tolerance = 10
        x, y = self.__position
        other_x, other_y = other.position
        return (
            x < other_x + tolerance and x > other_x - tolerance
            and
            y < other_y + tolerance and y > other_y - tolerance
        )