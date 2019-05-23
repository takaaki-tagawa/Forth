def fizzbuzz(i):
    is_fizz = i % 3 == 0
    is_buzz = i % 5 == 0
    if is_fizz and is_buzz:
        print('Fizz Buzz') 
    elif is_fizz:
        print('Fizz')
    elif is_buzz:
        print('Buzz')
    else:
        print(i)

def main():
    MAX = 100
    for i in range(MAX+1):
        fizzbuzz(i)

if __name__ == "__main__":
    main()
