from threading import Timer


def show():
    print("How r u dude?...")

# After 10 second, my function will start
t = Timer(10, show)
t.start()
