from random import randint

def hod():
    global num
    num = int(randint(1,7))
    print(f"hodil si: {num} ")
    
    return num
hod()

if num == 3:
    print("mozes skakat ty zebrak ")
    hod()
elif num % 2 ==0:
    print("davaj drepy")
    hod()
else:
    print("mas stastie")
    hod()