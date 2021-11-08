#T = int(input())
#print("\n".join(str(T-i) for i in range(T) ))

print('\n'.join(map(repr, range(int(input()), 0, -1))))
