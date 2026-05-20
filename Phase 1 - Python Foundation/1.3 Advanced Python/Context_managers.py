


class Demo:

    def __enter__(self):
        print("Program Enter")
        return self
    
    def __exit__(self, exc_type, exc, tb):
        print("Program exit")
        print(exc_type)
        if exc_type:
            print("Due to error next code didnt execute")
        return True


with Demo() as d:

    a = 10/0
    print(a)
    print("Hello my friend")


from contextlib import contextmanager
@contextmanager
def demo():

    print("Program started")
    yield
    print("Program Ended")

with demo() as d:
    print("this is the middle yield process")    


@contextmanager
def newdemo():

    print("Start")

    try:

        yield

    except Exception as e:

        print("Error handled:", e)

    finally:

        print("End")

with newdemo() as d:
    a = 10/0
    print(a)
