
def convert():
    v1 = v.replace(':)','\U0001f642')
    v1 = v1.replace(':(','\U0001F641')
    return v1

def main():
    print(convert())

v = input("Введите текст: ")
main()
