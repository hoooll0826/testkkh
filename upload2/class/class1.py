class Robot:
    def __init__(self,rbt,cpt):#self -> a?
        self.motor=rbt
        self.computer=cpt
    def rotate(a):#a는 가짜
        print("motor op")
    def motorangle(a,input):#+str(a.motor) a.motor수를 string으로 바꿔야 넣을수있음
        ans=input+60
        return ans

robotArr = [0,0,0,0,0]

for i in range(5):
    robotArr[i]=Robot(i*2,i*3)#Robot i번째에 rbt=i*2 , cpt=i*3

print(robotArr[2].motor)#robot 2번째에서 .motor로 rbt를 불러옴
robotArr[2].rotate()
