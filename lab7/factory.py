class Factory:
    def __init__(self, instance):
        self.instance = instance
        self.base = "app.views"

    def get_instance(self):
        if not self.instance:
            raise "Error..."
        path = f"{self.base}.{self.instance}".split(".")
        module_path = ".".join(path[:-1])
        module = __import__(
            module_path
        )
        for component in path[1:]:
            print(module, component)
            module = getattr(module, component)
        return module
