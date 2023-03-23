#!/usr/bin/python3
"""Make changes"""

def makeChange(coins, total):
    """
    make changes
    """

    if total == 0:
        return 0
    
    holder = []
    hold = 0
    count = 0
    for coin in coins:
        for i in coins:
            hold = coin
            while hold <= total:
                if hold < total:
                    hold += i
                    count += 1
                if hold == total:
                    count += 1
                    holder.append(count)
                    print(hold)
                    hold = 0
                    count = 0
                    break

    if len(holder) > 0:
        return min(holder)
    else:
        return -1
