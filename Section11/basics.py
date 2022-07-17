# myfile = open("fruit.txt")
# content = myfile.read()    # how to read file in python
# myfile.close()

# print(content)

# # Better way to read file
# with open("files/vegetables.txt", "w") as myfile :
#     myfile.write("Tomato\nCucumber\nOnion\n")
#     myfile.write("Garlic")


# # Exercise
# def fileProcessInsideFunc(char, filePath) :
#     with open(filePath) as myfile:
#         content = myfile.read()

#     occurance = 0

#     for character in content :
#         if character == char :
#             occurnace += 1
    
#     return occurance

# # Exercise
# with open("files/file.txt", "w") as myfile :
#     myfile.write("snail")   # write할 때는 따로 변수에 저장할 필요 없음

# # Exercise
# with open("bear.txt") as myfile :
#     content = myfile.read(90)
#     myfile.close()

# with open("files/file.txt", "w") as myfile :
#     myfile.write(content)

# # Add line to existing file
# with open("files/fruit.txt", "a+") as myfile :
#     myfile.write("\nOkra")
#     myfile.seek(0) # move cursor to 0 position
#     content = myfile.read()

# print(content)

# # Exercise
# with open("bear1.txt") as myfile :
#     content = myfile.read()

# with open("bear2.txt", "a") as myfile :
#     myfile.write("\n", content)

# Exercise
with open("files/data.txt", "a+") as readFile :
    readFile.seek(0)
    content = readFile.read()
    readFile.write(content)
    readFile.write(content)