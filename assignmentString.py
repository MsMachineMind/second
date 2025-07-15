                                           #1. STRING TASK

#1. Take a string input and print it with quotes around it.
s = input("Enter the string: ")
print(f"the string with quotes is \"{s}\" ")
#2. Concatenate two strings and print the result.
s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")
print("Concatenated string :-")
print(s1 + s2)

#3. Find the length of a string.
s = input("Enter the string :")
print(f"length of the string is {len(s)}")

#4. Print a specific character using indexing
s = input("Enter the string :")
i = int(input("Enter the index: "))
print(f"character at {i} index is {s[i]}")

#5. Slice the string to get a part of it.
s = input("Enter the string :")
i1,i2 = map(int, input("Enter the first and last index separated with comma :").split(","))
l = len(s)
if(i1 < l and i1 <l):
    print(f"part of the string for the given range is \"{s[i1:i2]}\" ")
else:
    print("sorry you had entered the out of range indices")
    
#6. Check if the string ends with a specific substring
s = input("Enter the string :")
e = input("Enter the character you want to check that whether the string ends with it or not: ")
if(s.endswith(e)):
    print(f"Yes the given string \"{s}\" ends with the charcter \"{e}\"")
else:
    print(f"Sorry but it doesn't endswith \"{e}\"")
    
#7. Capitalize the first letter of the string
s = input("Enter the string :")
sn = s[0].capitalize()# it will only store the first capital letter of s because strings are imutable
for i in range(1,len(s)):
    sn = sn+s[i]
print(f"string after caspitalizing the first letter {sn}")

#8. Replace a character with another in a string
s = input("Enter the character: ")
o,n = map(str,input("Enter the old and new character that you want to replace:").split(","))
if(o in s ):
    print(s.replace(o,n))
else:
    print("Sorry the old character doesn't exist in the string")
    
#9. Count how many times a word appears in a sentence
s = input("Enter the sentece: ")
w = input("Enter the word you want to count: ")
# OR******************************************
# print(s.count(w))
count = 0
l = s.split(" ")
if(w in s):
    for i in l:
        if(i == w):
                count = count+1
    print(f"the given word exist in the sentence for \"{count}\" number fo times")
else:
    print("the word \"{w}\" you entered doesn't exist in the sentence")
    
# 10. Find the index of a character in the string.
s = input("Enter the string :")
c = input("Enter the character :")
#OR******************************
#print(s.index(c))
if(c in s):
    for i in range(0,len(s)):
        if(c == s[i]):
            id = i
            break
    print(f"the character \"{c}\" exist at index \"{id}\"")
else:
    print(f"Sorry this \"{c}\"character doesn't exist")
