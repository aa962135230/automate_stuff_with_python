import os, sys

def find_endwith_name(path, subject_size):
    if not (os.path.exists(path) and os.path.isdir(path)):
        print("请输入一个已存在的文件夹名称!")
        sys.exit()

    for current_dir, sub_dir, filenames in os.walk(path):
        sub_dir
        for filename in filenames:
            if os.path.getsize(os.path.join(current_dir, filename)) > subject_size:
                print(os.path.join(current_dir, filename) + "size is:" + str(os.path.getsize(os.path.join(current_dir, filename))) )

find_endwith_name("/home/kindleeldnik/CodeWorkSpace/automate_stuff_with_python/ch09", 1000)
# find_endwith_name("/home/kindleeldnik/CodeWorkSpace/automate_stuff_with_python/ch09", "10")

