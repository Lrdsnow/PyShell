import platform as ops
usrOS=ops.system()
if usrOS != "Windows":
    try:
        exec(open("src/pysh-unix.py").read())
    except:
        print("An Error Has Occured, Closing.")
else:
    try:
        exec(open("src\\pysh.py").read())
    except:
        print("An Error Has Occured, Closing.")
