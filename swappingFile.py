#file1 = "C:/Users/Abc/Desktop/SamProjects/PythonProjects/functions/sample1.txt"
#file2 = "C:/Users/Abc/Desktop/SamProjects/PythonProjects/functions/sample2.txt"
file1 = input("Enter a file path: ")
file2 = input("Enter another file path: ")

with open(file1, 'r') as a:
    data_a = a.read()

with open(file2, 'r') as b:
    data_b = b.read()

def swapFileData():
    with open (file1, 'w') as a:
        a.write(data_b)

    with open (file2, 'w') as b:
        b.write(data_a)

swapFileData()
 