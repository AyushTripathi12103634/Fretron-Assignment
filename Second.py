from functools import lru_cache

a = []
n = int(input("Enter apple weight in gram (-1 to stop): "))
while n != -1:
    a.append(n)
    n = int(input("Enter apple weight in gram (-1 to stop): "))
a.sort(reverse=True)
b = a.copy()
n = len(a)

@lru_cache(maxsize=None)
def ks(W, i, arr):
    global a, b, n
    if i >= n:
        a = b.copy()
        n = len(a)
        return arr
    if sum(arr) + a[i] > W:
        return ks(W, i + 1, tuple(arr))
    else:
        b.remove(a[i])
        return ks(W, i + 1, tuple(arr + tuple([a[i]])))

t = sum(a)
r_w = t * 0.5
s_w = t * 0.3
rm_w = t * 0.2

ram_a = ks(r_w, 0, tuple([]))
sham_a = ks(s_w, 0, tuple([]))
rahim_a = ks(rm_w, 0, tuple([]))

print("Distribution Result: ")
print(f"Ram: {list(ram_a)}")
print(f"Sham: {list(sham_a)}")
print(f"Rahim: {list(rahim_a)}")
