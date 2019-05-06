newArray=[
[3],
[7, 4],
[2, 4, 6],
[8, 5, 9, 3]]


def max_path(tri):
    while len(tri) > 1:
        t0 = tri.pop()
        t1 = tri.pop()
        tri.append([max(t0[i], t0[i+1]) + t for i,t in enumerate(t1)])
    return tri[0][0]

print(max_path(newArray) )
print(f'time taken : {time.perf_counter()-start}')