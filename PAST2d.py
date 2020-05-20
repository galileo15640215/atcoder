s = list(input())
k = len(s)
if k == 1:
    cnt = 2
elif k == 2:
    if s[0] == s[1]:
        cnt = 6
    else:
        cnt = 7
else:
    dic = {}
    for i in range(k-2):
        if i not in dic.keys():
            dic[s[i]] = [s[i], s[i]+'.', s[i]+'..']
    for i in range(k-2):
        if s[i]+s[i+1]+'.' not in dic[s[i]]:
            dic[s[i]].append(s[i]+s[i+1]+'.')
        if s[i]+'.'+s[i+2] not in dic[s[i]]:
            dic[s[i]].append(s[i]+'.'+s[i+2])
    dic['.'] = ['.', '..', '...']
    for i in range(k-2):
        if '.'+s[i+1] not in dic['.']:
            dic['.'].append('.'+s[i+1])
        if '.'+s[i+1]+s[i+2] not in dic['.']:
            dic['.'].append('.'+s[i+1]+s[i+2])
        if '.'+s[i+1]+'.' not in dic['.']:
            dic['.'].append('.'+s[i+1]+'.')
        if '.'+'.'+s[i+2] not in dic['.']:
            dic['.'].append('.'+'.'+s[i+2])
    for i in range(k-2):
        if s[i]+s[i+1] not in dic[s[i]]:
            dic[s[i]].append(s[i]+s[i+1])
        if s[i]+s[i+1]+s[i+2] not in dic[s[i]]:
            dic[s[i]].append(s[i]+s[i+1]+s[i+2])
    if '.'+s[-1] not in dic['.']:
        dic['.'].append('.'+s[-1])
    if s[-2] not in dic.keys():
        dic[s[-2]] = [s[-2], s[-2]+'.']
    if s[-1] not in dic.keys():
        dic[s[-1]] = [s[-1]]
    if s[-2]+s[-1] not in dic[s[-2]]:
        dic[s[-2]].append(s[-2]+s[-1])     
    cnt = 0
    for i in dic.keys():
        cnt += len(dic[i])
print(cnt)