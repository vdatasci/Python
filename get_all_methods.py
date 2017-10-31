[func for func in dir(Foo) if callable(getattr(Foo, func))]
