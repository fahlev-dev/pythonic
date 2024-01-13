# percabangan dengan dictionary (switch case) di python

def one():
    print('satu-one')
    
def two():
    print('dua-two')
    
def three():
    print('tiga-three')
    
case = 2
switch = {
    1: one,
    2: two,
    3: three
}

switch[case]()
    
