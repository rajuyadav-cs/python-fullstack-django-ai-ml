# Async are use for executing the code in concurrent basis
# Async helps for efficiently use of CPU

import asyncio


async def task1():
    print("hello world")
    await asyncio.sleep(5)
    print("Hello Ruuh")


async def task2():
    print("Good Morning")
    await asyncio.sleep(1)
    print("Good Afternoon")
    await asyncio.sleep(5)


class AsyncManager:

    async def __aenter__(self):
        print("Entering the async manager")
        return self
    
    async def __aexit__(self, exc_type, exc, tb):
        print("Ending the function")
        print(exc_type)
        return True


async def main():

    await asyncio.gather(
        task1(),
        task2()
    )

    async with AsyncManager() as a:
        print("Inside block")
        await asyncio.sleep(5)
        print("After waiting")


asyncio.run(main())


# Now running all of them Together both class manager and async function

import asyncio


async def task1():
    print("hello world")
    await asyncio.sleep(5)
    print("Hello Ruuh")


async def task2():
    print("Good Morning")
    await asyncio.sleep(1)
    print("Good Afternoon")
    await asyncio.sleep(5)


class AsyncManager:

    async def __aenter__(self):
        print("Entering the async manager")
        return self
    
    async def __aexit__(self, exc_type, exc, tb):
        print("Ending the function")
        print(exc_type)
        return True


async def manager_task():
    async with AsyncManager() as a:
        print("Inside block")
        await asyncio.sleep(5)
        print("After waiting")


async def main():
    await asyncio.gather(
        task1(),
        task2(),
        manager_task()
    )


asyncio.run(main())


# Iteration using Async

import asyncio


class AsyncCounter:

    def __init__(self):

        self.count = 0

    def __aiter__(self):

        return self

    async def __anext__(self):

        if self.count >= 5:

            raise StopAsyncIteration

        self.count += 1

        await asyncio.sleep(1)

        return self.count


async def main():

    async for number in AsyncCounter():

        print(number)


asyncio.run(main())