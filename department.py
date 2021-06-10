f_name = input("First Name: ")
l_name = input("Last Name: ")
s_number = input("Student Number: ")


lf_name = list(f_name)
ll_name = list(l_name)
ls_number = list(s_number)


def generate_net_id(lf_name, ll_name,ls_number):


    if len(lf_name) > 2 and len(ll_name) > 2:
        #Run this chunk of code if  the first name and last name characters are greater than 2
        net_id = lf_name[:2] + ll_name[:2] + ls_number[-3:]
        res = "".join(net_id)
        print("Net ID: "+res)
    
    
    else:
        #Run this chunk of code if  the first name and last name characters are less than 2
        net_id = lf_name + ll_name + ls_number[-3:]
        res = "".join(net_id)
        print("Net ID: "+res)
            


generate_net_id(lf_name, ll_name,ls_number)