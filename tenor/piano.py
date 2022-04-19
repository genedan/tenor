from tenor.pitch import pitches

piano = {}

for i in range(88):
    piano[i] = pitches[i % 12] + str(i // 12)
