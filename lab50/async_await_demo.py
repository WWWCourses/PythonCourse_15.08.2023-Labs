import asyncio

# Define an asynchronous function
async def greet(name, delay):
  await asyncio.sleep(delay)  # Simulate a non-blocking delay
  print(f"Hello, {name}!")

# Create an event loop
async def main():
  # Create multiple asynchronous tasks
  task1 = greet("Pesho", 2)
  task2 = greet("Ivan", 1)

  print('Tasks are finished')

  # Schedule the tasks in the event loop
  await asyncio.gather(task1, task2)

# Run the event loop
if __name__ == "__main__":
  asyncio.run(main())