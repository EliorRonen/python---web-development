file_read = open('Codingal.txt','r')
print("File in Read Mode-")
print(file_read.read())
file_read.close()


file_write = open('Codingal.txt','w')
file_write.write("file in write mod...")
file_write.write("write")
file_write.close()


file_append = open('Codingal.txt', 'a')
file_append.write("\n File in append mode ...")
file_append.write("HI! I am HI! and i am a Word!")
file_append.close()