import re

pattern1 = "cat"
pattern2 = "bird"
string = "dog runs to cat"
print (pattern1 in string)
print(pattern2 in string)
print("-------------------------")

print (re.search(pattern1, string))
print (re.search(pattern2, string))
print("-------------------------")

ptn = r"r[au]n" # 引号前面的 r 表示这是一个正则表达式，而非字符串
# [] 表示出现在里面的东西都是可取的, 这里可以匹配到 run 或者 ran
print(re.search(ptn, string))
print(re.search(r"r[a-z]n", string))
# [A-Z], [0-9], [0-9a-z]
print("-------------------------")

# 数字
# \d: decimal digit -> 所有数字形式
print(re.search(r"r\dn", "run r4n"))
# \D: any non-decimal digit -> 所有不是数字的形式
print(re.search(r"r\Dn", "run r4n"))
print("-------------------------")

# 空白
# \s: any white space [\t\n\r\f\v]
print(re.search(r"r\sn", "r\nn r4n"))
# \S: opposite to \s, any non-white space
print(re.search(r"r\Sn", "r\nn r4n"))
print("-------------------------")

# 所有字母数字和"_"(下划线)
# \w: [a-zA-Z0-9_]
print(re.search(r"r\wn", "r\nn r4n"))
# \W: opposite to \w
print(re.search(r"r\Wn", "r\nn r4n"))
print("-------------------------")

# 空白字符
# \b: empty string (only at the start or end of the word)
print(re.search(r"\bruns\b", "dog runs to cat"))
# \B: empty string (but not at the start or end of a word)
print(re.search(r"\Bruns\B", "dog _runs_ to cat"))
print("-------------------------")


# 特殊字符 任意字符
# \\: match \
print(re.search(r"runs\\", "runs\ to me"))
# .: match anything (except \n)
print(re.search(r"r.n", "r{ns to me"))
print("-------------------------")


# 句尾句首
# ^: match line beginning
print(re.search(r"^dog", "dog runs to cat"))
# $: match line ending
print(re.search(r"cat$", "dog runs to cat"))
print("-------------------------")


# 是否
# ?: may or may not occur
print(re.search(r"Mon(day)?", "Monday"))
print(re.search(r"Mon(day)?", "Mon"))
print("-------------------------")


# 多行匹配
# multi-line
string_multiline = """
dog runs to cat.
I run to dog.
""" 
print(re.search(r"^I", string_multiline))
print(re.search(r"^I", string_multiline, flags=re.M))
print("-------------------------")


# 0或多次
print(re.search(r"ab*", "a"))
print(re.search(r"ab*", "abbbbbbbb"))
print("-------------------------")

# 1或多次
print(re.search(r"ab+", "a"))
print(re.search(r"ab+", "ab"))
print(re.search(r"ab+", "abbbb"))
print("-------------------------")

# 可选次数
print(re.search(r"ab{2,10}", "ab"))
print(re.search(r"ab{2,10}", "abb"))
print("-------------------------")


# group 组
match = re.search(r"(\d+), Date: (.+)", "ID: 02153, Date: Feb/12/2017")
print(match.group())
print(match.group(1))
print(match.group(2))
# 给组加入名字
match = re.search(r"(?P<id>\d+), Date: (?P<date>.+)", "ID: 02153, Date: Feb/12/2017")
print(match.group('id'))
print(match.group('date'))
print("-------------------------")

# 寻找所有匹配
# findall
print(re.findall(r"r[ua]n", "run ran ren"))
# |: or
print(re.findall(r"(run|ran)", "run ran ren"))
print(re.findall(r"r(u|a)n", "run ran ren"))
print(re.findall(r"(r(u|a)n)", "run ran ren"))
print("-------------------------")


# 替换
# re.sub() replace
print(re.sub(r"r[au]ns", "catches", "dog runs to cat"))
print("-------------------------")

# 分裂
# re.split()
print(re.split(r"[,;/.]", "a,b;c/d.e"))
print("-------------------------")

# compile
# 先把匹配形式编译出来，然后再用匹配形式去search
complied_re = re.compile(r"r[ua]n")
print(complied_re.search("dog ran to cat"))
print("-------------------------")
