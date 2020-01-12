def JumpDistance(ordinaryHeight,jumpTimes,index=0.6):

#        Ordinary Height:初始高度
#        Jump Times: 弹跳次数
    distance = 0
    for i in range(jumpTimes):
        print(i)
        distance += (ordinaryHeight+ordinaryHeight*index)
        ordinaryHeight = ordinaryHeight*index
    return distance

print(JumpDistance(10,1))