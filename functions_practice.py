def hello():
    print("Hello user")
hello()

def pack(arg1, arg2, arg3):
    print(arg1 + ', ' + arg2+ ', ' +arg3)
pack('toothbrush', 'soap', 'underwear')

def eat_lunch(food_list):
    if len(food_list) == 0:
        print("Oh no my lunch box is empty :(")
    else:
        for x in range(len(food_list)):
            if x == 0:
                print(f'First I will be eating {food_list[0]}')
            else: 
                print(f'Next I will eat {food_list[x]} ')

eat_lunch(["stevia", "blueberries", "salt"])
   
