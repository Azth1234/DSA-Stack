def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    
    if val == 0:
        return 0   # collinear
    elif val > 0:
        return 1   # clockwise
    else:
        return 2   # counterclockwise

def convex_hull(points):
    points.sort()

    lower = []
    for p in points:
        while len(lower) >= 2 and orientation(lower[-2], lower[-1], p) != 2:
            lower.pop()
        lower.append(p)

    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and orientation(upper[-2], upper[-1], p) != 2:
            upper.pop()
        upper.append(p)

    return lower[:-1] + upper[:-1]


points = [(0,3),(2,2),(1,1),(2,1),(3,0),(0,0),(3,3)]
#points = eval(input("Enter points: "))

hull = convex_hull(points)

print("Convex Hull Points:")
for p in hull:
    print(p)