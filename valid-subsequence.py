import sys
def isValidSubsequqnce(arr, seq):
    ia = i = 0
    while i < len(seq) and len(arr) > ia:
        if seq[i] == arr[ia]:
            ia+=1
            i+=1
            if i == len(seq):
                return True
        else:
            ia+=1
     
    return False

if __name__ == "__main__":
    a = sys.argv[1].split(',')
    b = sys.argv[2].split(',')
    print(a)
    print(b)
    print(isValidSubsequqnce(a,b))
