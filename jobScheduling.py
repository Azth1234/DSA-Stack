def job_sequencing(jobs):

    # Sort by profit (descending)
    jobs.sort(key=lambda x: x[2], reverse=True)

    # Find maximum deadline
    max_deadline = max(job[1] for job in jobs)

    # Create time slots
    slots = [None] * (max_deadline + 1)

    total_profit = 0

    for job in jobs:
        job_id, deadline, profit = job

        # Check slot from deadline to 1
        for i in range(deadline, 0, -1):
            if slots[i] is None:
                slots[i] = job_id
                total_profit += profit
                break

    print("Selected Jobs:")
    for i in range(1, len(slots)):
        if slots[i]:
            print(slots[i], end=" ")

    print("\nTotal Profit:", total_profit)


# Example
jobs = [
    ('A', 2, 100),
    ('B', 1, 19),
    ('C', 2, 27),
    ('D', 1, 25),
    ('E', 3, 15)
]

job_sequencing(jobs)
