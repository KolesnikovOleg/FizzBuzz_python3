def FizzBuzz(numb):
    result = ''
    if numb%3 == 0 :
        result += 'Fizz'
    if numb%5 == 0 :
        result += 'Buzz'
    if result == '' :
        result = str(numb)
    print(result)


for n in range(1, 101):
    FizzBuzz(n)
