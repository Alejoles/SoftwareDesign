class Proxy:
    def __init__(self, instance):
        self.instance = instance


    def proxy(self):
        object_instance = self.instance
        if object_instance.number % 2 == 0:
            print("Proxy actuando...")
