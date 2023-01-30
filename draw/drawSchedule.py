"""
Build schedule w/ pairings for the redpill-cup
Version 0.0.1-alpha by Pfulsk
This is just the proof of concept.
The draw is still missing (but very easy to implement)
"""

import pandas as pd

def schedule(intTeams = 4, boolSecondRound = True):

    usedTeams = intTeams
    if not (usedTeams % 2) == 0:
        usedTeams += 1

    n = usedTeams - 1
    m = int(usedTeams / 2)

    df = pd.DataFrame(columns=['H', 'A', 'RD'])
    
    for i in range(1,usedTeams):
        h = usedTeams
        a = i

        # home or away
        if not (i % 2) == 0:
            a, h = h, a

        df = pd.concat([df, pd.DataFrame({'H': [h], 'A': [a], 'RD': [i]})], ignore_index=True)
        
        for k in range(1,m):
            print(i-k)
            if (i-k) < 0:
                a = n + (i-k)
            else:
                a = (i-k) % n
                if a == 0:
                    a = n

            h = (i+k) % n
            if h == 0:
                h = n

            # home or away
            if (k % 2) == 0:
                a, h = h, a

            df = pd.concat([df, pd.DataFrame({'H': [h], 'A': [a], 'RD': [i]})], ignore_index=True)

    if boolSecondRound:
        count = df.shape[0]

        for x in range (0,count):
            df = pd.concat([df, pd.DataFrame({'H': df.at[x,'A'], 'A': df.at[x,'H'], 'RD': [df.at[x,'RD']+m+1]})], ignore_index=True)

    return(df)

df = schedule(4)
print(df)