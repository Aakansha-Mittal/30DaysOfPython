#LOOPS - Repetitive tasks

'''
1. while - Execute block of statements until the condition is satisfied. 

while condition : 
      block of statements

2. while - else :
when the loop stops (the condition is not true), then else block will be executed. 
NOT IF LOOP STOPS BY BREAK, ONLY IF LOOP ENDS NORMALLY.

3. for loop : it iterates over a sequence or in a range.

for iterator in list/set/tuple/dict/str : 
    statements

for iterator in range(start, stop, step) :
     statements

start and step are not mandatory. stop -1 tak.

4. for- else :
else executed if loop ends normally not in break case.

'''

'''
pass - In python when statement is required (after semicolon), but we don't like to execute
 any code there, we can write the word pass to avoid errors.

'''


count = 0
while count < 5:
    #print(count)
    count = count+1
    if (count == 3):
        #break
        continue
    print(count)

else : 
    print (f"count is after loop : {count}")


for i in range(10):
    print(i)
    if (i==8):
        #break
        pass
else :
    print("Out of loop")