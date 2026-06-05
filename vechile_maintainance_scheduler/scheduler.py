def optimize_tasks(tasks, capacity):

    n = len(tasks)

    dp = [[0] * (capacity + 1)
          for _ in range(n + 1)]

    for i in range(1, n + 1):

        duration = tasks[i - 1]["Duration"]
        impact = tasks[i - 1]["Impact"]

        for h in range(capacity + 1):

            if duration <= h:

                dp[i][h] = max(
                    dp[i - 1][h],
                    dp[i - 1][h - duration] + impact
                )

            else:
                dp[i][h] = dp[i - 1][h]

    selected = []

    h = capacity

    for i in range(n, 0, -1):

        if dp[i][h] != dp[i - 1][h]:

            selected.append(tasks[i - 1])

            h -= tasks[i - 1]["Duration"]

    selected.reverse()

    return selected