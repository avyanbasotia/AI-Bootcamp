import bisect
def find(scores, target):
    index=bisect.bisect(scores, target)
    return index if index < len(scores) else -1

scores= [0.12,0.35,0.41,0.58,0.63,0.77,0.89,0.95]
target= [0.5,0.9,0.1, 1.0,0.41]

for y in target:
        print(f"Target = {y} -> Output index: {find(scores,y)}")