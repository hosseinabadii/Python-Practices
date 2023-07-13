class Pizza:
    def __init__(self, ingrediants):
        self.ing = ingrediants
    
    def __repr__(self, ):
        return f'Pizza ==> {self.ing}'
    
    def price(self, cost):
        return [item + str(cost) for item in self.ing]
    
    @classmethod
    def mushroom(cls):
        return cls(['mushroom','chease'])
    
    @staticmethod
    def shape():
        return 'circle'
    
p1 = Pizza(['bread', 'meat'])
print(p1)

print(p1.price(20))

print(Pizza.mushroom())  # use classmethod on the class itself.
print(p1.mushroom())     # you are able to use classmethod on an instance.

print(Pizza.shape())     # use staticmethod on the class itself.
print(p1.shape())        # you are able to use staticmethod on an instance.