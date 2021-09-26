def static_init(cls):
    if getattr(cls, "init_class", None):
        cls.init_class()
    return cls
