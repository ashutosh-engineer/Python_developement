import asyncio as a

# What are co-routunes
# Co routines are function which can stop and get resume again
# Unlike normal functions jo ki directly memeory mein data dump karte hain


async def wait():
    print("Fetching started")
    await a.sleep(2)
    print("Data Fetched Successfully")
    return "Data"

# Event loops in asyncio
# Needed to run The corotines on it.
#It became tasks 

async def simon():
    return "Hello"
    # task = a.create_task(wait())
    # await task


# a.run(main())




#USing gather method in python

async def main():
    results=await a.gather(wait() , simon())

    print(results) 
    # Data is returned in list ;

a.run(main())