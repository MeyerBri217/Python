#This program is to categorize a tea room order by tea type
#this program will create an array by looping taking an order of 5 types of tea from a user
#a second loop will determine caffeine for each tea ordered by using ord() to convert the string input into ASCII values. The values will then be summed and divied by 10 to get caffeine content
#caffeine content will determine tea type by a caffeine scale: <40 herbal, 40-60 green, 61-70 oolong, 71-75 pu-erh, >75 black tea, creating a new array of the tea types


#Developer Meyer, Brianna   02/25/2024
#---------------------------------------------------------

def main():
    print("Meyer, Brianna   02/25/2024")
    print("\nWelcome to Mint Milk Tea room \nEach order comes with 5 flavors of tea.")

    #Create array taking user input for 5 types of tea
    order=[]
    control=0
    while control<5:
        control= control+1
        print('\n', control, "Enter a flavor of tea you would like to order")
        flavor=input()
        order.append(flavor)
    print("Your order is", order)

    #Loop to call teaType function for each tea ordered
    types=[]
    for tea in order:
        teaType= ''
        tempVar=[ord(x) for x in flavor]
        caffeine= (sum(tempVar)/10)
        if caffeine <40:
            teaType= 'herbal tea'
        elif 40<= caffeine <=60:
            teaType= 'green tea'
        elif 60< caffeine <=70:
            teaType= 'oolong'
        elif 70< caffeine <= 75:
            teaType= 'pu-erh'
        elif 75< caffeine:
            teaType= 'black tea'
        types.append(teaType)

    print("\n\nthese are the types of tea you have ordered:")
    print(types)
        
        

    
main() 
