import turtle
import math

s = turtle.Screen()
s.setup(900, 900)
s.title("智能与信息工程学院 - 未来架构")
s.bgcolor("#edf5f7")
s.tracer(0)

t = turtle.Turtle()
t.hideturtle()
t.speed(0)

navy = "#101f39"
cyan = "#43d5cf"
white = "#ffffff"
silver = "#a7c5d6"

def move(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

def path(points, color, width=2, fill=None):
    t.pensize(width)
    t.pencolor(color)
    move(*points[0])
    if fill:
        t.fillcolor(fill)
        t.begin_fill()
    for p in points[1:]:
        t.goto(*p)
    if fill:
        t.goto(*points[0])
        t.end_fill()

def dot(x, y, r, color):
    t.pencolor(color)
    t.fillcolor(color)
    move(x, y-r)
    t.begin_fill()
    t.circle(r)
    t.end_fill()

def write(x, y, words, size, color):
    move(x, y)
    t.pencolor(color)
    t.write(words, align="center",
            font=("Microsoft YaHei", size, "bold"))

def hexagon(radius, color, fill, width):
    pts = []
    for i in range(6):
        angle = math.radians(90-i*60)
        pts.append((
            radius*math.cos(angle),
            radius*math.sin(angle)
        ))
    path(pts, color, width, fill)

# 六边形外框
hexagon(390, navy, navy, 5)
hexagon(367, cyan, None, 4)
hexagon(337, silver, None, 1)

# 顶部文字
write(0, 256, "智能与信息工程学院", 27, white)
write(0, 212, "SCHOOL OF INTELLIGENCE", 14, cyan)
write(0, 188, "AND INFORMATION ENGINEERING", 12, cyan)

# 中央几何 A 型结构
path([
    (-185, -100),
    (0, 145),
    (185, -100),
    (125, -100),
    (0, 57),
    (-125, -100)
], cyan, 5)

# 中央横梁
path([
    (-94, -45),
    (94, -45)
], white, 9)

# 内部建筑结构
path([
    (-48, -100),
    (-48, -65),
    (48, -65),
    (48, -100)
], silver, 5)

# 数据网络
for side in [-1, 1]:
    path([
        (side*185, -100),
        (side*240, -100),
        (side*270, -65)
    ], cyan, 3)
    dot(side*270, -65, 7, cyan)

    path([
        (side*110, 0),
        (side*220, 0),
        (side*245, 30)
    ], silver, 3)
    dot(side*245, 30, 6, silver)

# 顶部数据节点
path([(0, 145), (0, 178)], cyan, 4)
dot(0, 178, 9, cyan)

# 下面数据矩阵
for row in range(3):
    for col in range(7):
        x = -90 + col*30
        y = -125-row*25
        dot(x, y, 3.5, cyan if (row+col)%2 else silver)

# 下方英文简称
write(0, -248, "S I I E", 27, white)
write(0, -286, "INNOVATION  ·  TECHNOLOGY", 12, cyan)

# 角落装饰
for x in [-150, 150]:
    dot(x, -235, 5, cyan)

s.update()
turtle.done()