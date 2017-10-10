import turtle as t
t.shape("turtle") # 거북이 그래픽 모듈을 실행합니다.
# 꽃모양에 무지개색을 순서대로 입히기
angle=85 # 거북이가 왼쪽으로 회전할 각도 85도로 정합니다.
t.bgcolor("black") # 배경색을 검은색으로 정합니다.
t.color("red") # 펜 색을 빨간색으로 정합니다.
t.pensize(2) # 펜 사이즈를 2 크기로 정합니다.
t.speed(200) # 거북이의 속도를 200으로 정합니다.
for x in range(40): # x값을 0부터 39까지 바꾸면서 40번 실행합니다.
    t.fd(x) # x값만큼 앞으로 이동합니다.
    t.left(angle) # 거북이가 angle 값인 85만큼 왼쪽으로 회전합니다.
t.color("orange") # 펜 색을 주황색으로 변경합니다.
for x in range(40,80): # x값을 40부터 79까지 바꾸면서 40번 실행합니다.
    t.fd(x) # x값만큼 앞으로 이동합니다.
    t.left(angle) # 거북이가 angle 값인 85만큼 왼쪽으로 회전합니다.
t.color("yellow") # 펜 색을 노란색으로 변경합니다.
for x in range(80,120): # x값을 80부터 119까지 바꾸면서 40번 실행합니다.
    t.fd(x) # x값만큼 앞으로 이동합니다.
    t.left(angle) # 거북이가 angle 값인 85만큼 왼쪽으로 회전합니다.
t.color("green") # 펜 색을 초록 색으로 변경합니다.
for x in range(120,160): # x값을 120부터 159까지 바꾸면서 40번 실행합니다.
    t.fd(x) # x값만큼 앞으로 이동합니다.
    t.left(angle) # 거북이가 angle 값인 85만큼 왼쪽으로 회전합니다.
t.color("blue") # 펜 색을 파란색으로 변경합니다.
for x in range(160,200): # x값을 160부터 199까지 바꾸면서 40번 실행합니다.
    t.fd(x)  # x값만큼 앞으로 이동합니다.
    t.left(angle) # 거북이가 angle 값인 85만큼 왼쪽으로 회전합니다.
t.color("dark blue") # 펜 색을 남색으로 변경합니다.
for x in range(200,240): # x값을 200부터 239까지 바꾸면서 40번 실행합니다.
    t.fd(x) # x값만큼 앞으로 이동합니다.
    t.left(angle) # 거북이가 angle 값인 85만큼 왼쪽으로 회전합니다.
t.color("purple") # 펜 색을 보라색으로 변경합니다.
for x in range(240,279): # x값을 240부터 278까지 바꾸면서 39번 실행합니다.
    t.fd(x) # x값만큼 앞으로 이동합니다.
    t.left(angle) # 거북이가 angle 값인 85만큼 왼쪽으로 회전합니다.
t.ht() # 거북이의 모습을 숨깁니다.
