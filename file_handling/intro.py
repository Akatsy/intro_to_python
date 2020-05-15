print("All kinds of files have a similar structure on a computer i.e they are just strings of characters that encode some information")
print("The specific file format often indicated by the extension of the file name e.g .py, .txt, .jpg, .htm, .csv e.t.c will indicate how those characters are organized")
print("These characters in a file are interpreted by the programs we use to interact with them e.g an image editing program will interpret the information of a digital photograph file and display the image. If we edit the image, then we are using the program to change characters in the file")
print('#' * 99)


f = open('/home/mutwiri2/Desktop/intro_to_python/file_handling/if')
f_text = f.read()
f.close()
print(f_text)