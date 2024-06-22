
def main():
    feet2meter(v)

def feet2meter(v):
    v = v.rstrip(' ft')
    v = float(v)
    v = round(v*0.3048, 2)
    s = f'Это будет {v} метров.'
    print(s)

v = input("Сколько футов:")
main()
