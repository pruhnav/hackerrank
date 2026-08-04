if __name__ == '__main__':
    n = int(input())
    for i in range(0,n):
        print(i**2)
        i+=1 

## Corrected Answer

def is_leap(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False
