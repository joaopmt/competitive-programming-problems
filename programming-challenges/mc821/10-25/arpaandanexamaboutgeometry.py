def dist(x1, y1, x2, y2):
    return (x1-x2)**2 + (y1-y2)**2

ax, ay, bx, by, cx, cy = [int(x) for x in input().split()]
ab = dist(ax, ay, bx, by)
ac = dist(ax, ay, cx, cy)
bc = dist(bx, by, cx, cy)
if (ax*(by-cy) + (bx*(cy-ay)) + (cx*(ay-by)) != 0) and (ab==ac or ab==bc):
    print("Yes")
else: print("No")
