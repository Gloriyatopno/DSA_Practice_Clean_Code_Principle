#Queue
queue = []

queue.append(10)
queue.append(20)
queue.append(30)

print("Queue:", queue)
print("Front:", queue[0])
print("Rear:", queue[-1])

removed = queue.pop(0)

print("Removed:", removed)
print("Queue:", queue)