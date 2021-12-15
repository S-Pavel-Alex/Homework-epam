def instances_counter(cls):
    class ModifiedClass:
        count_instance = 0

        def __init__(self, *args, **kwarg):
            self.obj = cls(*args, **kwarg)
            super().__init__(*args, **kwarg)
            ModifiedClass.count_instance += 1

        @classmethod
        def get_created_instances(cls):
            return cls.count_instance

        @classmethod
        def reset_instances_counter(cls):
            value_instance = cls.count_instance
            cls.count_instance = 0
            return value_instance

        def __getattribute__(self, item):
            try:
                x = super().__getattribute__(item)
            except AttributeError:
                return self.obj.__getattribute__(item)
            else:
                return x

    return ModifiedClass
