#!/usr/bin/env python
# coding: utf-8

# In[1]:


def factor(a,b):
    f1 = a.intersection(b)
    f2 = b - a
    f3 = a - b
    re = min(f1,min(f2,f3))
    return len(re)


# In[15]:


file = open('e.txt','r')
horizontal = []
vertical = []
test = int(file.readline())
for _ in range(test):
    temp_f = file.readline()
    temp_f = temp_f[0:len(temp_f)-1]
    inp = list(temp_f.split(" "))
    temp = (set(inp[2:]))
    fin = []
    fin.append(_)
    fin.append(temp)
    if inp[0]=="H":
        horizontal.append(fin)
    else:
        vertical.append(fin)
file.close()


# In[65]:


i = 0
while i<len(vertical) and len(vertical) >=2:
    j = i+1
    leni = len(vertical[i][1])
    maxn = 10000000000000000000
    com = 0
    comsj = vertical[i][1]
    while j < len(vertical):
        coms = vertical[i][1].union(vertical[j][1])
        lenij = len(coms)
        if maxn > lenij:
            com = j
            comsj = coms
        j+=1
    if i != com:
        tem = []
        tem.append(str(vertical[i][0]) +  " " + str(vertical[com][0]) )
        tem.append(comsj)
        horizontal.append(tem)
    vertical.pop(i)
    vertical.pop(com-1)


# In[68]:


i = 0
final_ans = []
while i < len(horizontal):
    max_score = 0
    temp_i = -1
    max_score_i = -1
    while temp_i < len(horizontal):
        if temp_i != i:
            temp_score = factor((horizontal[temp_i][1]),(horizontal[i][1]))
            if temp_score > max_score:
                max_score = temp_score
                max_score_i = temp_i
        temp_i+=1
    final_ans.append(horizontal[i][0])
    horizontal.pop(i)
    if len(horizontal) == 1:
        final_ans.append(horizontal[0][0])
        break


# In[70]:


print(len(final_ans))
print(*final_ans,sep="\n")


# In[ ]:


# out = open('output.txt','w')
# out.write(str(len(final_ans)))
# out.write("\n")
# for out_i in final_ans:
#     out.write(str(out_i))
#     out.write("\n")
# out.close()

