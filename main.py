def parallel_processing(n, m, data):
    output = []
    threads = [(0, i) for i in range(n)]
    heapq.heapify(threads)
    current_time = 0

    for job_index, job_time in enumerate(data):
        start_time, thread_index = heapq.heappop(threads)
        if current_time > start_time:
            current_time = start_time
        output.append((thread_index, current_time))
        current_time += job_time
        heapq.heappush(threads, (current_time, thread_index))

    return output

def main():
    n, m = map(int, input().split())
    data = list(map(int, input().split()))

    result = parallel_processing(n, m, data)

    for thread_index, start_time in result:
        print(thread_index, start_time)

if __name__ == "__main__":
    main()
