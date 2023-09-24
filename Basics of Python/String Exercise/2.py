# 1. Finding length of the list.
heros=['spider man','thor','hulk','iron man','captain america']
print("Length of the list=",len(heros))
# 2. Adding "black panther" in the list.
heros.append("black panther")
print(heros)
# 3. Moving black panther after hulk.
del heros[5]
heros.insert(3,"black panther")
print(heros)
# 4. Replacing thor and hulk with doctor strange.
heros[1:3]=["doctor strange"]
print(heros)
# 5. Alphabetical sorting of list heros.
heros.sort()
print(heros)