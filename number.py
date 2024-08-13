import sys

while True:
    print('숫자를 입력하세요')
    value = sys.stdin.readline()
    try:
        new_value = int(value)
    except:
        print('다시 입력하세요')
        continue
    
    result = format(new_value, ",")
    print(result)
    break