#11
passengers = []
p_out = []

#11-1
passengers.append([1,1,1,1,1])

#11-2
passengers.append([1,1,1])


#11-3
passengers[-1].pop(-1)
passengers[-1].pop(-1)
# passengers.append([])


#11-4
passengers.append([1,1,1,1])



print("승객 리스트: {}".format(passengers))

s = 0
for i in passengers:
    for j in i:
        s = s + 1
print("총 승객: {}".format(s))


print("처음부터 2개의 승객 데이터: {}" .format(passengers[:2]))
print("마지막 2개의 승객 데이터: {}" .format(passengers[-2:]))
