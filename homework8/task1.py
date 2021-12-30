class KeyValueStorage:
    def __init__(self, file):
        self.file = file
        try:
            with open(file) as document:
                for line in document:
                    key, value = line.strip().split('=')
                    if not key.isidentifier():
                        raise ValueError(f'{key} is bad key')
                    if getattr(self, key, None) is None:
                        self.__setattr__(key, value)
        except FileNotFoundError:
            raise FileNotFoundError(f'File {self.file} not founded')

    def __getitem__(self, key):
        return getattr(self, key)


k = KeyValueStorage('task1.txt')
print(k.__dict__)
