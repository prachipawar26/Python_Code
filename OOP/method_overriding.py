class Logger:
    def log(self, message: str):
        print(f"Base Log: {message}")

class ConsoleLogger(Logger):
    def log(self, message: str):
        # Overriding the parent method
        print(f"[CONSOLE]: {message}")

class FileLogger(Logger):
    def log(self, message: str):
        # Overriding to add file-writing logic
        with open("app.log", "a") as f:
            f.write(f"[FILE]: {message}\n")

# Polymorphism in action
loggers = [ConsoleLogger(), FileLogger()]
for l in loggers:
    l.log("System started") # Same method name, different behavior