print("Always remember to close files that you have opened once you no longer need them because if you open a lot of files without closing them, you can run out of file handles and you will not be able to open any new files")
print("Exactly how many files you can open before running out of handles will depend on your OS")

# a program to see how many files you can have open before running out of handles
files = []
try:
    for i in range(10000):
        files.append(open('/home/mutwiri2/Desktop/intro_to_python/file_handling/if'))
        print(i)
except Exception as e:
    print(e)
finally:
    print(f"{i} files opened before running out of handles")