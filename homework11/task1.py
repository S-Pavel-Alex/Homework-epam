class SimplifiedEnum(type):
    def __new__(mcs, name: str, superclass: tuple, dct: dict):
        cls_key = f'_{name}__keys'
        cls_instance = super().__new__(mcs, name, superclass, dct)
        if hasattr(cls_instance, cls_key):
            for key in getattr(cls_instance, cls_key):
                setattr(cls_instance, key, key)
        return cls_instance
