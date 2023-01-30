"""
Build schedule w/ pairings for the redpill-cup
Version 0.0.1-alpha by Pfulsk
This is just the proof of concept.
"""

import os, random, pandas as pd

os.chdir(os.path.abspath(os.path.dirname(__file__))) # Change working directory to current
wd = os.getcwd()                                     # working directory

def schedule(intTeams = 4, prt = [], boolSecondRound = True):
    print(prt)

    if not (intTeams % 2) == 0:
        return(False)

    n = intTeams - 1
    m = int(intTeams / 2)

    df = pd.DataFrame(columns=['H', 'A', 'RD'])
    
    for i in range(1,intTeams):
        h = intTeams
        a = i

        # home or away
        if not (i % 2) == 0:
            a, h = h, a

        df = pd.concat([df, pd.DataFrame({'H': prt[h-1], 'A': prt[a-1], 'RD': [i]})], ignore_index=True)
        
        for k in range(1,m):
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

            df = pd.concat([df, pd.DataFrame({'H': prt[h-1], 'A': prt[a-1], 'RD': [i]})], ignore_index=True)

    if boolSecondRound:
        count = df.shape[0]

        for x in range (0,count):
            df = pd.concat([df, pd.DataFrame({'H': df.at[x,'A'], 'A': df.at[x,'H'], 'RD': [df.at[x,'RD']+m+1]})], ignore_index=True)

    return(df)

count = 0
file1 = open('participants.txt', 'r')
participants = file1.readlines()
for participant in participants:
    participants[count] = participant.strip()
    count += 1
random.shuffle(participants)

if not(count % 2 == 0):
    participants.append('NaN')
    count += 1

df = schedule(count, participants, False)

print(df)