def instances_counter(original_class):

    def get_created_instances(cls):
        if "counter" not in cls.__dict__:
            return 0
        return cls.counter

    old_init = original_class.__init__

    def some_init(cls, *args, **kwargs):
        old_init(cls, *args, **kwargs)
        if "counter" not in cls.__class__.__dict__:
            cls.__class__.counter = 1
        else:
            cls.__class__.counter += 1

    def reset_instances_counter(cls):
        if "counter" not in cls.__dict__:
            return 0
        value = cls.counter
        cls.counter = 0
        return value

    original_class.get_created_instances = classmethod(get_created_instances)
    original_class.__init__ = some_init
    original_class.reset_instances_counter = \
        classmethod(reset_instances_counter)

    return original_class
