# Dizinin ikinci elemanından başlanarak kayıtlar sırayla kontrol edilir.
# Bir önceki kayıt o anki kayıttan büyükse bu iki elemanın yerleri değiştirilir.
# Normal ve en kötü durumda O(n^2)dir
# Her durumda yapacağı karşılaştırma sayısı C=n(n-1)/2



array =[3,0,1,8,7,2,5,4,9,6]
def yerDegis(x,y):
    temp =array[x]
    array[x]=array[y]
    array[y]=temp


for i in range(1,len(array)):
    j=i
    while (j>0):
        if(array[j] < array[j-1]):
            yerDegis(j,j-1)
        else:
            break
        j=j-1
