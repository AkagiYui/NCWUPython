# 对字符串中每个单词出现的次数进行统计，并将结果输出
# 输出出现次数排在前五名的单词
# 将字符串中的单词按照出现次数从多到少进行排序

s = """According to independent research conducted 
on behalf of the IOC, Beijing 2022 has become 
the most digitally engaged Olympic Winter Games in history, 
with 2.01 billion viewers, up 5% from PyeongChang 2018 watching 
the Games through linear TV and digital platforms. 
Viewers watched a total of 713 billion minutes of the 
Games coverage through Olympic media rights partners' channels, 
and Olympic social media also achieved 3.2 billion engagements and 
attracted more than 11 million new followers across various platforms."""

d = {}
for i in s.split():
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
print(d)

d = sorted(d.items(), key=lambda x: x[1], reverse=True)
print(d[:5])
