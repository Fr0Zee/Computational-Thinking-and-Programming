def chop(list_C):
    del list_C[0]
    del list_C[-1]
def middle(list_M):
    list_M = list_M[1:-1]
    return list_M
List = [1, 2, 3, 4]
print("My list before call middle function =>", List)
chop(List)
print("My list after call middle function =>", List)


List1 = [1, 2, 3, 4]
print("\n\nMy list before call middle function =>", List1)
List2 = middle(List1)
print("My list after call middle function =>", List1)
print("New list after call middle function =>", List2)