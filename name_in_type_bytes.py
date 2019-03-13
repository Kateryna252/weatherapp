print("Hello\n"
      "Nice to meet you in my program about type of data as bytes\n"
      "Do you want to know, how your name be in bytes type?\n")
name = input("Enter your name ...\n")
name_in_bytes_type = bytes(name,'utf-8')
name_in_utf_16 = name.encode("utf-16")
print("Your name in bytes type is like  -  ", name_in_bytes_type)
print("Your name in utf-16 is like  -  ", name_in_utf_16)

