class KeyValueStorage:
    def __init__(self, file):
        self.file = file
        # with open(self.file) as document:
        #     document.read()



k = KeyValueStorage('text.txt')
print(k.__dict__)