import math

def dist(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def closest(points):
    n = len(points)

    if n <= 3:  # brute force
        return min(dist(points[i], points[j]) 
                   for i in range(n) for j in range(i+1, n))

    mid = n // 2
    dl = closest(points[:mid])
    dr = closest(points[mid:])
    d = min(dl, dr)

    mid_x = points[mid][0]

    strip = [p for p in points if abs(p[0] - mid_x) < d]
    strip.sort(key=lambda x: x[1])   # sort by y-coordinate

    for i in range(len(strip)):
        for j in range(i+1, min(i+7, len(strip))):
            d = min(d, dist(strip[i], strip[j]))

    return d


points = [(2,3),(12,30),(40,50),(5,1),(12,10),(3,4)]
points.sort()

print("Minimum Distance:", closest(points))