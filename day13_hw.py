import turtle as t       # 거북이 함수를 사용합니다.
import random            # random 함수를 사용합니다.
t.shape()
t.speed(0)
t.up()
t.goto(-100,-100)
t.down()
for x in range(4):       # for 구문을 사용해 한변의 길이가 500인 사각형을 만듭니다.
    t.fd(500)
    t.lt(90)
t.up()
t.goto(150,150)
t.down()
n=random.randint(0,360) # n을 0부터 360중 랜덤적인 한 수로 지정합니다.
t.seth(n)               # 거북이가 처음 바라보는 방향을 n이라는 값으로 나타냅니다.
while True:             # 밑의 수식이 참인 경우에 영원히 반복합니다.
    while -100<t.xcor()<400 and -100<t.ycor()<400:  # while 함수가 거북이가 사각형 내부에 존재할때 계속 지속되게 설정합니다.
        t.fd(1)
        n=t.heading()  # 거북이가 면에 충돌해방향을 바꾸게 될 때마다 n값을 그 때 바라보는 방향으로 갱신합니다.
    while 400<=t.xcor()<401:    # 거북이가 오른쪽 면에 충돌했을때 어떤 각도로 들어오는지를 통해 반사각을 정합니다.
        if 0<n<90:
            t.seth(180-n)
            t.fd(1)
        elif 270<n<360 :
            t.seth(540-n)
            t.fd(1)
    while -101<t.xcor()<=-100:  # 거북이가 왼쪽 면에 충돌했을 때 어떤 각도로 들어오는지를 통해 반사각을 갱신합니다.
        if 90<n<180:
            t.seth(180-n)
            t.fd(1)
        elif 180<n<270:
            t.seth(540-n)
            t.fd(1)
    while 400<=t.ycor()<401:    # 거북이가 위쪽 면에 충돌했을 때 어떤 각도로 들어오는지를 통해 반사각을 갱신합니다.
        if 0<n<180:
            t.seth(360-n)
            t.fd(1)
    while -101<t.ycor()<=-100:  # 거북이가 아래쪽 면에 충돌했을 떄 어떤 각도로 들어오는지를 통해 반사각을 갱신합니다.
        if 180<n<360:
            t.seth(360-n)
            t.fd(1)
