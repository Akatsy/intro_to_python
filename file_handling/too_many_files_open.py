files = []
# for i in range(10000):
#     files.append(open('/home/mutwiri2/Desktop/intro_to_python/file_handling/if'))
#     print(i)

try:
    for i in range(10000):
        files.append(open('/home/mutwiri2/Desktop/intro_to_python/file_handling/if'))
        print(i)
except Exception as e:
    print(e)