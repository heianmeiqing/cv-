
def get_u_p(filename="userinfo.txt"):
    with open(filename) as f:
        data=f.readlines()
    return data

def checkuserinfo(username,password,filename="userinfo.txt"):
    flag=False
    all_data=get_u_p(filename)
    for user in all_data:
        if (username==user.split(':')[0].strip() and password==user.split(':')[1].strip()):
            flag=True
        else:
            pass
        return flag