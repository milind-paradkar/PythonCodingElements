
ls = list(range(10))
l1 = [0, 1, 2]

print(ls)
print(ls[0])
print(ls[-1])
print(ls[-2])
print("ls[-10]==", ls[-10]) # max negative index allowed = -(len(ls)), max positive index allowed len(ls)-1
print("len:", len(ls))
# print(l[len(l)]) # IndexError: list index out of range. There is l[0] to l[9]=10 elements. l[10] does not exists
print(ls[len(ls)-1])
print("ls[:5]==", ls[:5])
print("ls[5:]==", ls[5:])
print(ls[3:len(ls)]) # we can use len() because slice skips last index [x:y] slices xth index to y-1 index
print("ls[3:8]",ls[3:8])
print("ls[3:10]",ls[3:10])
print("ls[3:15]",ls[3:15])  # even if range is out of bounds, it will not give error
print("ls[::3]==", ls[::3])
print("ls[1::3]==", ls[1::3])
print("ls[len(ls):2:-1]==", ls[len(ls):2:-1], "even if range is out of bounds (len() will return 10 and ls[10] is not present), stil it will not give error")
print("ls[456:2:-1]==", ls[456:2:-1], "even if range is out of bounds, it will not give error. and -1 step will start from last index (either ls[-1] or ls[len(ls)-1])")
print("ls[456:2:1]==", ls[456:2:1], "even if range is out of bounds, it will not give error, but 456th item is not present with positive steps, so empty []")
print("ls[len(ls)+6:2:-1]==", ls[len(ls)+6:2:-1], "even if range is out of bounds, it will not give error")
print("ls[:2:-1]==", ls[:2:-1])
print("ls[:0:-1]==", ls[:0:-1])
print("ls[::-1]==", ls[::-1])
print("ls[::-3]==", ls[::-3])
print("ls[2::-3]==", ls[2::-3])
print("ls[5:8:-1]", ls[5:8:-1])
print("ls[:5:1]  ==", ls[:5:1])  # started from first index and 5th index skipped
print("ls[:5:-1]  ==", ls[:5:-1])  # started from last (9th) index and 5th index skipped
print("ls[19:5:-1]==", ls[19:5:-1], "Ignored wrong index 19, started from 9th index and 5th index skipped")  # Ignored wrong index 19, started from 9th index and 5th index skipped
print("ls[19:4:-2]==", ls[19:4:-2], "Ignored wrong index 19, started from 9th index and 4th index skipped")  # Ignored wrong index 19, started from 9th index and 5th index skipped
print("ls[5::-1]", ls[5::-1])
print("ls[5:2]", ls[5:2])
print("ls[5:2:]", ls[5:2:])
print("ls[5:2:-1]", ls[5:2:-1], "last index 2 is skipped")
print()
