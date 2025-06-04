import queue_sort as que
import montecarlo as m_c
import async1 as a1
import multiprocessing
import asyncio
import random


if __name__ == "__main__": 
    data = list(range(0, 1000))
    with multiprocessing.Pool(processes=10) as pool:
        results = pool.map(m_c.monte_carlo, data)
        print(results)          

    asyncio.run(a1.main())

    data = []
    for i in range(10):
        data.append(random.randint(1, 100))
    producers = que.producer(data)
    consumers = que.consumer()
    producers.start()
    consumers.start()
    producers.join()
    consumers.join()