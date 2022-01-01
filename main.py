import os

flag = 0
markdown = """# 2021年终总结

<!-- 此处待完善 -->
想要添加您的年终总结？请发 Issue 或有能力者自行编辑 metadata.md 并发PR。

本项目将长期维护（直到2023年初），因为[以往的经验](https://t.me/blogrsslist/269)告诉我——有些博主的年终总结可能要[拖拉个半年才写得完](https://idealclover.top/archives/627/)，还有些博主明明都年中了才写完了上一年的年终总结，又觉得不好意思而自己把文章发布时间改成年初，掩耳盗铃。有趣有趣……

---

https://t.me/blogrsslist/350
"""

with open('metadata.md', 'r') as f:
  file = f.read()
lines = file.splitlines()
lines = set(lines)
lines.discard('')
lines = list(lines)
lines.sort()

with open('metadata.md', 'w') as f:
    for line in lines:
        f.write(line+'\n')

with open('README.md', 'w') as f:
  for line in lines:
    if flag == 0:
        f.write(markdown+'\n'+'- '+line+'\n')
        flag = 1
    else:
        f.write('- '+line+'\n')
