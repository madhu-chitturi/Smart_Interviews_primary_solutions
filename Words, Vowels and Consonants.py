                                                          Words, Vowels and Consonants
  Given a sentence containing only uppercase/lowercase english alphabets and spaces, you have to count the number of words, vowels and consonants.

Input Format

First line of input contains T - number of test cases. Its followed by T lines, each line contains a single sentence.

Constraints

1 <= T <= 1000
1 <= len(sentence) <= 104

Output Format

For each test case, print the number of words, vowels and consonants, separated by newline.

Sample Input 0

4
Hi
Hello World
  Exception  
Hi there
Sample Output 0

1 1 1
2 3 7
1 4 5
2 3 4
  
  <=================================== PYTHON SOLUTION =================================>
  
 def words(str1):
    return len(str1.split())
def vow(str1):
    v=0
    c=0
    str1=str1.lower()
    for i in str1:
        if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
            v+=1
        else:
            c+=1
    return v

def cons(str1):
    v=0
    c=0
    s=0
    str1=str1.lower()
    for i in str1:
        if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
            v+=1
        elif(i==' '):
            s+=1
        else:
            c+=1
    return c
t=int(input())
for i in range(t):
    str1=input()
    print(words(str1) ,vow(str1) ,cons(str1))
