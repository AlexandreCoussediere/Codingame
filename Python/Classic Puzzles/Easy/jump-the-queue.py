# Read number of friend groups (g) and number of events (e)
g, e = map(int, input().split())

# Map each student id to the list of ids in their friend group
friend_group = {}
for _ in range(g):
    ids = list(map(int, input().split()))
    for student_id in ids:
        friend_group[student_id] = ids

# Read the sequence of events (positive id = enqueue, -1 = dequeue)
events = list(map(int, input().split()))

queue = []
output = []

for event in events:
    if event == -1:
        # Dequeue: remove and record the student at the head of the queue
        output.append(str(queue.pop(0)))
    else:
        student_id = event
        # Friends of this student, empty list if none
        friends = friend_group.get(student_id, [])

        # Default: insert at the tail of the queue
        insert_index = len(queue)
        # Scan from tail to head to find the last friend in the queue
        for idx in range(len(queue) - 1, -1, -1):
            if queue[idx] in friends:
                insert_index = idx + 1
                break

        queue.insert(insert_index, student_id)

# Print each dequeued student id on its own line
print('\n'.join(output))
