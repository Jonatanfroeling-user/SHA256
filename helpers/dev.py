def hr(length = 32, icon = '-'):
    if isinstance(length, str) or length == 0:
        length = 32
        
    print(''.join([icon for _ in range(length)]))

def pt(title):
    print()
    hr(len(title))
    print(title)
    hr(len(title))
    
def br(*prints):
    print()
    for i in prints:
        print(i)
    
def px(*prints):
    for i in prints:
        print(i)