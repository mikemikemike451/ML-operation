class Customer:
    def __init__(self, accumulation, discount):
        self._accumulation  = accumulation
        self._discount = discount
    
    def makePurchase(self, amount):
        if self._discount:
            amount -= 10
            self._discount = False
        self._accumulation  += amount
        self.discountReached()
        print(f'Please pay {amount} dollar,\n accumlation:{self._accumulation},\n DiscountNextTime:{self._discount}')

            
    def discountReached(self):
        if self._accumulation >= 100:
            self._discount = True
            self._accumulation = self._accumulation % 100


Jim = Customer(50,True)
Jim.makePurchase(45)
Jim.makePurchase(75)


