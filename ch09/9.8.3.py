import os, re, shutil, sys

def squence(dir, prefixname):
    if not (os.path.exists(dir) and os.path.isdir(dir)):
        print("请输入一个已存在的文件夹名称!")
        sys.exit()

    regex_str = '(' + prefixname  + ')'+ r'(\d+)'
    regex = re.compile(regex_str)
    # print(regex)
    dict = {}
    for filename in os.listdir():
        mo = regex.search(filename)
        if mo != None:
            dict[int(mo.group(2))] = filename
    
    list_sort = list(dict.keys())
    list_sort.sort()
    print(type(len(list_sort)))
    
    for i in range(len(list_sort)):
        print(list_sort[i])
        print(dict[list_sort[i]])
        mo = regex.search(dict[list_sort[i]])
        # print(mo.group(1), mo.group(2))
        # shutil.move(dict[list_sort[i], mo.group(1) + str(list_sort[i]) + os.path.splitext(dict[list_sort[i]])[1])
        print(os.path.splitext(dict[list_sort[i]])[1])

    print(dict)




squence('/home/kindleeldnik/CodeWorkSpace/automate_stuff_with_python/ch09', 'spam')
