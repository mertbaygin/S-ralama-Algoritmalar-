# O notasyonu diğer yerleştirmeli sıralamalardan farklı olacaktır, normal durumlarda ve en kötü durumda O(nlogn)'dir
#Algoritmanın yapacağı karşılaştırma sayısı her zaman C=n(logn-loge-+0,5) olacaktır.

array =[3,0,1,8,7,2,5,4,9,6]
def yerDegis(x,y):
    temp =array[x]
    array[x]=array[y]
    array[y]=temp

for i in range(9,1,-1):
    j=0
    while (j<i):
        if(array[j] > array[j+1]):
            yerDegis(j,j+1)
        j+=1
