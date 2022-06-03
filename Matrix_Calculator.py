import numpy as np

def mat_input(m , n , nums = 1):        # nums is number of matrices the user want to input
    mat = np.zeros((m, n)).astype(float)      #store matrix m*n in ram
    for x in range(m):       #loop in Rows
        for k in range(n):           #loop in col
            num = input(f"Please enter element{x +1 ,k + 1}")
            mat[x,k] = num # store the element
    if nums == 1:
        
        print("your matrix = \n" , mat)
        global aaaa
        aaaa = mat # store matrix in glopal variable
    else:
        print(f"your matrix {nums} =  \n" , mat)
        global bbbb
        bbbb = mat

def mat_random (m , n , nums = 1):
    mat = np.random.random((m, n)).astype(float)
    if nums == 1:
        
        print("your matrix = \n" , mat)
        
    else:
        print(f"your matrix {nums} =  \n" , mat)
    a = mat
    return a


def find_element(aaaa, value):
    testss = False
    for row in range(m):
        for element in range(n):
            if aaaa[row , element] == value:
                print(f"we found it in {row + 1, element + 1}")
                testss = True
    if testss == False:
        print("Not found")

print("----------------- Hello Sir, ----------------------------")


print("Please enter what you need")
print("1 --- 1 matrix")
print("2 --- 2 matrices")
print("3 --- Random Matrix")
print("4 --- Diagonal Matrix")

choice = float(input())


if choice == 1:
    m = int(input("please enter rows"))
    n = int(input("please enter col"))
    mat_input(m , n)
    print("---------------------------------------------------------------------------")
    print("---------------------------------------------------------------------------")
    print("1 ==> Sum")
    print("2 ==> Multiply")
    print("3 ==> Division")     
    print("4 ==> The proposal")
    print("5 ==> Power")       
    print("6 ==> Transpose") 
    print("7 ==> Trace")
    print("8 ==> Det")
    print("9 ==> Inverse")    
    print("10 ==> Norm")    
    print("11 ==> Eigens") 
    print("12 ==> index")     
    print("13 ==> Reshape")    
    print("14 ==> Start is End")    
    print("15 ==> Max")    
    print("16 ==> Min")    
    print("17 ==> Sort") 
    print("18 ==> Search for Element")  
    
    print("\n")  
    
    user_choice = int(input("Enter what you need"))
    if user_choice == 1:
        
        print("1 ==> By scalar")
        print("2 ==> By axis") 
        sum_type = int(input("1 or 2"))
        if sum_type == 1:
            print(aaaa + int(input("Put your scalar")))
            
        if sum_type == 2:
            print(np.multiply.reduce(aaaa, axis= int(input("Put your axis"))))
        
    elif user_choice == 2:
        print("1 ==> By scalar")
        print("2 ==> By axis") 
        mult_type = int(input("1 or 2"))
        if mult_type == 1:
            print(aaaa * int(input("Put your scalar")))
            
        if mult_type == 2:
            print(np.sum(aaaa , axis = int(input("Put your axis"))))
            
            
    elif user_choice == 3:
        print(aaaa / int(input("Put your scalar")))
    
    elif user_choice == 4:
        print(aaaa - int(input("Put your scalar")))
    
    elif user_choice == 5:
        print(aaaa ** int(input("Put your scalar")))
    
    elif user_choice == 6:
        tr = np.transpose(aaaa) 
        print("your trans matrix = \n" , tr)
        
    elif user_choice == 7:
        print("Trace = " , np.trace(aaaa))
        
    elif user_choice == 8:
        print("Det = " , np.linalg.det(aaaa))
        
        
    elif user_choice == 9 and m == n:
        print("Invese = \n" , np.linalg.inv(aaaa))
    elif user_choice == 9 and m != n:
        print("Wrong non square Matrix")
        
    elif user_choice == 10:
        print(np.linalg.norm(aaaa , ord = int(input("l1 or l2")) , axis = int(input("Put your axis"))))
    
    elif user_choice == 11 and m == n:
        k , v = np.linalg.eig(aaaa)
        print("Eigen Values = \n" , k)
        print("Eigen Vectors = \n" , v) 
    elif user_choice == 11 and m != n:
        print("Wrong non square Matrix")
        
    elif user_choice == 12:
        r = int(input("element in row"))
        r = r-1
        c = int(input("element in col"))
        c = c-1
        print(aaaa[r , c])
    elif user_choice == 13:
        l = int(input("Put second row dimension you want"))
        j = int(input("Put second row dimension you want"))
        if l*j == m*n:
            print("New Matrix = \n", np.reshape(aaaa , (l , j)))
        else:
            print("Wrong : non suitable dimension")
    elif user_choice == 14:
        print(aaaa[::-1 , ::-1])
        
        
    elif user_choice == 15:
        print(np.max(aaaa))
    
    elif user_choice == 16:
        print(np.min(aaaa))
        
        
    elif user_choice == 17:
        print("1 ==> By row")
        print("2 ==> By col") 
        rc_type = int(input("1 or 2"))
        if rc_type == 1:
            print("Sorted Matrix :\n" , np.sort(aaaa , axis = 0))
            
        if rc_type == 2:
            print("Sorted Matrix :\n" , np.sort(aaaa , axis = 1))
             
        
    elif user_choice == 18:
        
        find_element(aaaa , int(input("Put your element")))


if choice == 2:
    
    m = int(input("please enter rows"))
    n = int(input("please enter col"))
    mat_input(m , n , nums = 1)
    m = int(input("please enter rows"))
    n = int(input("please enter col"))
    mat_input(m , n , nums = 2)
    
    
    print("---------------------------------------------------------------------------")
    print("---------------------------------------------------------------------------")
    print("1 ==> Sum")
    print("2 ==> Multiply")
    print("3 ==> Division")     
    print("4 ==> Solve")
    
    user_choice = int(input("Enter what you need"))
    if user_choice == 1:
        print(np.add(aaaa, bbbb))
    elif user_choice == 2:
        try:
            print(np.matmul(aaaa, bbbb))
        except:
            print("Wrong ")
    elif user_choice == 3:
        try:
            print(np.divide(aaaa, bbbb))
        except:
            print("Wrong ")

    elif user_choice == 4:
        try:
            print(np.linalg.solve(aaaa, bbbb))
        except:
            print("Wrong ")

if choice == 3:
    
    m = int(input("please enter rows"))
    n = int(input("please enter col"))
    mat_random(m , n , nums = 1)

if choice == 4:
    
    m2 = int(input("how much elements (max 10)"))
    mat2 = np.zeros((m2,m2))
    
    for k in range(m2):
        num2 = input(f"Please enter element{k + 1}")
        mat2[k] = num2
    print("Your elemnts =\n " , np.diag(mat2))
    print("Your matrix =\n ", np.diag(np.diag(mat2) , k = int(input("Put your key (as you like)"))))

