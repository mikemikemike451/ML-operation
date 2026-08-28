##
#  This module defines the Counter class.
#

## Models a tally counter whose value can be incremented, viewed, or reset.
#
class Counter:   
    def __init__(self):
        self._value = 0
        self._maximum = None
    ## Gets the current value of this counter.
    #  @return the current value   
    #
    def getValue(self) :
        return self._value

    ## Advances the value of this counter by 1.
    #
    def click(self) :
        if self._maximum == None:
            print('Please set the limit first')
        elif self._value < self._maximum:
            self._value = self._value + 1
        else:
            print('Limit exceeed.')

    ## Resets the value of this counter to 0.
    #
    def reset(self) :
        self._value = 0

    ## Substract the value of this counter by 1.
    #
    def undo(self):
        if self._value != 0:
            self._value = self._value - 1
    
    ## New: set the maximum value of the counter
    #
    def setLimit(self, maximum):
        self._maximum = maximum
