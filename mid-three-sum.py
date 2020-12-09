import sys


def threeNumberSum(arr, target):
  arr = sorted(arr)
  rs = []
  for i in range(len(arr)):
    cur_sum = []
    if sum(cur_sum) + arr[i] <= target:
      cur_sum.append(arr[i])
      for j in range(i +1, len(arr)):
        if sum(cur_sum) + arr[j] <= target:
          cur_sum.append(arr[j])  
          for k in range(j + 1, len(arr)):
            if sum(cur_sum) + arr[k] == target:
              rs.append(cur_sum + [arr[k]])
        cur_sum.pop()

  return rs


if __name__ == "__main__":
  arr = [int(a) for a in sys.argv[1].split(',')]
  target = int(sys.argv[2])
  print(threeNumberSum(arr, target))
