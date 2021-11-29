SizeOfMap_X=4
SizeOfMap_Y=4
Probability_X=1/(SizeOfMap_X-1)         #Assume uniform
Probability_Y=1/(SizeOfMap_Y-1)         #Assume uniform
AvgTotalDistanceForOrder=0

for x in range(SizeOfMap_X):
    for y in range(SizeOfMap_Y):
        vertical=0
        horizontal=0
        for v in range(y,y+SizeOfMap_Y):
            vertical=vertical + abs(SizeOfMap_Y-1-v)
        vertical=vertical*Probability_Y
        for h in range(x,x+SizeOfMap_X):
            horizontal=horizontal + abs(SizeOfMap_X-1-h)
        horizontal=horizontal*Probability_X
        TotalDistance=horizontal+vertical
        AvgTotalDistanceForOrder=AvgTotalDistanceForOrder+TotalDistance
        print('Location ({}, {})'.format(x, y))
        print('Expected distance is: {}'.format(TotalDistance))
print('Average Order Distance: ({})'.format(AvgTotalDistanceForOrder*2/(SizeOfMap_X*SizeOfMap_Y)))
