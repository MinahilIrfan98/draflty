import asyncio


async def fetch_data(name, delay):
    print(f"Fetching data for {name}...")
    await asyncio.sleep(delay)  # Simulate a network call
    print(f"Data fetched for {name}.")
    return {"data": f"Sample data for {name}"}


async def main():
    result = await asyncio.gather(
        fetch_data("A", 2),
        fetch_data("B", 3),
        fetch_data("C", 1),
    )
    print(f"Received data: {result}")


if __name__ == "__main__":
    asyncio.run(main())