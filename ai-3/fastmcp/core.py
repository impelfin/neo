class FastMCP:
    def __init__(self, name, dependencies=None):
        self.name = name
        self.dependencies = dependencies or []

    def tool(self):
        def decorator(func):
            # Register your tool logic
            return func
        return decorator

    def resource(self, path):
        def decorator(func):
            # Register your resource logic
            return func
        return decorator

    def prompt(self):
        def decorator(func):
            # Register your prompt logic
            return func
        return decorator