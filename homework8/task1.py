class KeyValueStorage:
    dict_class = {}

    def __init__(self, file):
        self.file = file
        try:
            with open(file) as document:
                for line in document:
                    key, value = line.strip().split('=')
                    if not key.isidentifier():
                        raise ValueError(key)
                    if KeyValueStorage.__get
                        KeyValueStorage.__setattr__(self, key, value)
        except FileNotFoundError:
            print(f'File {self.file} not founded')

    def __getitem__(self, key):
        return getattr(self, key)


k = KeyValueStorage('task1.txt')
print(k.__dict__)