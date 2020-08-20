import os, sys

def find_endwith_name(path, extend_name):
    if not (os.path.exists(path) and os.path.isdir(path)):
        print("请输入一个已存在的文件夹名称!")
        sys.exit()

    for current_dir, sub_dir, filenames in os.walk(path):
        sub_dir
        for filename in filenames:
            if filename.endswith(extend_name):
                print(os.path.join(current_dir, filename))


find_endwith_name("/home/kindleeldnik/CodeWorkSpace/automate_stuff_with_python/ch09", "vue")
find_endwith_name("/home/kindleeldnik/Con/ch09", "vue")

