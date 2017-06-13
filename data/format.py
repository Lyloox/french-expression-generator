import os

files = [f for f in os.listdir('.') if os.path.isfile(f)]
for f in files:
    if f.endswith('.in'):
        print("cleaning " + f)
        with open(f, 'r') as datas:
            words = sorted(set([_ for _ in datas if (len(_) != 0)]))
        with open(f, 'w') as datas:
            for word in words:
                datas.write(word)
