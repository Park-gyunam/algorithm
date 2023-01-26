angle_a = int(input())
angle_b = int(input())
angle_c = int(input())

if angle_a + angle_b + angle_c == 180:
    if angle_a == angle_b == angle_c == 60:
        print('Equilateral')
    elif angle_a == angle_b or angle_a == angle_c or angle_b == angle_c:
        print('Isosceles')
    else:
        print('Scalene')
else:
    print('Error')