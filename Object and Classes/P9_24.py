class Message():
    
    def __init__(self, recipient, sender, text):
        self._recipient = recipient
        self._sender = sender
        self._text = text
    
    def append(self, newline):
        self._text += '\n'
        self._text += newline
    
    def toString(self):
        print(f"From: {self._sender}\nTo: {self._recipient}\n{self._text}")


