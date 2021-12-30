import platform as ops
import getpass as gp
exitpysh=False
usrOS=ops.system()
USR=gp.getuser()
#print("pyshell v0.1a1")
scmd = {'ls':'ls','q':'exit','cd':'cd','mkdir':'mkdir','rmdir':'rmdir','execpython':'python','touch':'touch','os':'ckos','nano':'nano','wget':'wget','openssl':'openssl','sed':'sed','findhash':'findhash','unzip':'unzip','sort':'sort','echo':'echo'}
import os
cwd = os.getcwd()
src = "{0}".format(cwd)
home = "{0}".format(cwd)
cwd=cwd.replace(home, "", 1)
cdm = "~" + cwd.replace("\\", "/")
# blanks:
fullcmd=""
input_name=""
input_data=""
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def setup():
    cd(src)
    from zipfile import ZipFile
    with ZipFile('win32.zip', 'r') as zipObj:
        zipObj.extractall('win32')
    rm("win32.zip")
    cd("~")

def echo(echo=""):
    args = fullcmd.split()
    noa = len(args)
    if noa <= 1:
        print("err")
    else:
        if noa == 2:
            if echo == "":
                echo = fullcmd.split()[1]
            if not '"' in echo:
                if not "'" in echo:
                    try:
                        exec(f'print({echo})')
                    except:
                        print(f"pyshell: echo: variable {echo} does not exist")
            else:
                try:
                    echo=echo.replace('"', '')
                    echo=echo.replace("'", "")
                    print(echo)
                except:
                    print("pyshell: echo: an error has occured")
        else:
            print("pyshell: echo: command only takes 1 argument!")

def set_var(input_name, input_data):
    try:
        exec(f'global {input_name}; {input_name} = {input_data}')
    except:
        print("pyshell: =: an error has occured!")

def nano():
    import subprocess
    cmdargs = fullcmd.partition(' ')[2]
    nano=src + "\\win32\\nano.exe"
    subprocess.run([nano, cmdargs])

def wget():
    import subprocess
    cmdargs = fullcmd.partition(' ')[2]
    wget=src + "\\win32\\wget.exe"
    subprocess.run([wget, cmdargs])

def openssl():
    import subprocess
    cmdargs = fullcmd.partition(' ')[2]
    openssl=src + "\\win32\\openssl.exe"
    subprocess.run([openssl, cmdargs])

def findhash():
    import subprocess
    cmdargs = fullcmd.partition(' ')[2]
    findhash=src + "\\win32\\findhash.exe"
    subprocess.run([findhash, cmdargs])

def unzip(i=""):
    if i != "":
        fullcmd="pysh " + i
    import subprocess
    cmdargs = fullcmd.partition(' ')[2]
    unzip=src + "\\win32\\unzip.exe"
    subprocess.run([unzip, cmdargs])

def sort(i=""):
    if i != "":
        fullcmd="pysh " + i
    import subprocess
    cmdargs = fullcmd.partition(' ')[2]
    sort=src + "\\win32\\sort.exe"
    subprocess.run([sort, cmdargs])

def sed(i=""):
    if i != "":
        fullcmd="pysh " + i
    import subprocess
    cmdargs = fullcmd.partition(' ')[2]
    sed=src + "\\win32\\sed.exe"
    subprocess.run([sed, cmdargs])

def cd(folder=""):
    if folder != "":
        try:
            os.chdir(folder)
            cwd = os.getcwd()
            cwd=cwd.replace(home, "", 1)
            cdm = "~" + cwd.replace("\\", "/")
        except OSError as e:
            if folder == "~":
                try:
                    folder=folder.replace("~", home, 1).replace("\\", "").replace("C:", "")
                    os.chdir(folder)
                    cwd = os.getcwd()
                    cwd=cwd.replace(home, "", 1)
                    cdm = "~" + cwd.replace("\\", "/")
                except OSError as e:
                    print("pyshell: cd: %s: %s" % (folder, e.strerror.replace("file", "folder")))
            else:
                print("pyshell: cd: %s: %s" % (folder, e.strerror.replace("file", "folder")))
        return
    args = fullcmd.split()
    noa = len(args)
    if noa <= 1:
        print("pyshell: cd: command requires argument!")
    else:
        if noa == 2:
            folder = fullcmd.split()[1]
            try:
                os.chdir(folder)
                cwd = os.getcwd()
                cwd=cwd.replace(home, "", 1)
                cdm = "~" + cwd.replace("\\", "/")
            except OSError as e:
                if "~" in folder:
                    folder=folder.replace("~", home, 1)
                    os.chdir(folder)
                    cwd = os.getcwd()
                    cwd=cwd.replace(home, "", 1)
                    cdm = "~" + cwd.replace("\\", "/")
                else:
                    print("pyshell: cd: %s: %s" % (folder, e.strerror.replace("file", "folder")))
        else:
            print("pyshell: cd: command only takes 1 argument!")

def mkdir(folder=""):
    if folder != "":
        try:
            os.mkdir(folder)
        except OSError as e:
            print("pyshell: mkdir: %s: %s" % (folder, e.strerror.replace("file", "folder")))
        return
    args = fullcmd.split()
    noa = len(args)
    if noa <= 1:
        print("pyshell: mkdir: command requires argument!")
    else:
        if noa == 2:
            folder = fullcmd.split()[1]
            try:
                os.mkdir(folder)
            except OSError as e:
                print("pyshell: mkdir: %s: %s" % (folder, e.strerror.replace("file", "folder")))
        else:
            print("pyshell: mkdir: command only takes 1 argument!")

def mv(file=""):
    if file != "":
        try:
            os.rename(file)
        except OSError as e:
            print("pyshell: mv: %s: %s" % (file, e.strerror))
        return
    args = fullcmd.split()
    noa = len(args)
    if noa <= 1:
        print("pyshell: mv: command requires argument!")
    else:
        if noa == 2:
            file = fullcmd.split()[1]
            try:
                os.rename(file)
            except OSError as e:
                print("pyshell: mv: %s: %s" % (file, e.strerror))
        else:
            print("pyshell: mv: command only takes 1 argument!")

def mv(file=""):
    if file != "":
        try:
            os.remove(file)
        except OSError as e:
            print("pyshell: rm: %s: %s" % (file, e.strerror))
        return
    args = fullcmd.split()
    noa = len(args)
    if noa <= 1:
        print("pyshell: rm: command requires argument!")
    else:
        if noa == 2:
            file = fullcmd.split()[1]
            try:
                os.remove(file)
            except OSError as e:
                print("pyshell: rm: %s: %s" % (file, e.strerror))
        else:
            print("pyshell: rm: command only takes 1 argument!")

def ckos():
    print("User Is Running: {}".format(ops.system()))

def rmdir(folder=""):
    if folder != "":
        try:
            os.rmdir(folder)
        except OSError as e:
            print("pyshell: rmdir: %s: %s" % (folder, e.strerror.replace("file", "folder")))
        return
    args = fullcmd.split()
    noa = len(args)
    if noa <= 1:
        print("pyshell: rmdir: command requires argument!")
    else:
        if noa == 2:
            folder = fullcmd.split()[1]
            try:
                os.rmdir(folder)
            except OSError as e:
                print("pyshell: rmdir: %s: %s" % (folder, e.strerror.replace("file", "folder")))
        else:
            print("pyshell: rmdir: command only takes 1 argument!")

def hid(path=""):
    import ctypes
    ctypes.windll.kernel32.SetFileAttributesW(path, 2)

def rm(folder=""):
    if folder != "":
        try:
            os.rmdir(folder)
        except OSError as e:
            print("pyshell: rmdir: %s: %s" % (folder, e.strerror.replace("file", "folder")))
        return
    args = fullcmd.split()
    noa = len(args)
    if noa <= 1:
        print("pyshell: rm: command requires argument!")
    else:
        if noa == 2:
            folder = fullcmd.split()[1]
            try:
                os.remove(folder)
            except OSError as e:
                print("pyshell: rm: %s: %s" % (folder, e.strerror.replace("file", "folder")))
        else:
            print("pyshell: rm: command only takes 1 argument!")

def ls(folder=""):
    if folder != "":
        try:
            files = os.listdir(folder)
            print(str(f'{files}  ')[1:-1].replace(",", "").replace("'", ""))
        except:
            if "~" in folder:
                folder=folder.replace("~", home, 1)
                files = os.listdir(folder)
                print(str(f'{files}  ')[1:-1].replace(",", "").replace("'", ""))
            else:
                print("pyshell: ls: folder " + folder + " does not exist!")
        return
    args = fullcmd.split()
    noa = len(args)
    if noa <= 1:
        files = os.listdir()
        print(str(f'{files}  ')[1:-1].replace(",", "").replace("'", ""))
    else:
        if noa == 2:
            folder = fullcmd.split()[1]
            try:    
                files = os.listdir(folder)
                print(str(f'{files}  ')[1:-1].replace(",", "").replace("'", ""))
            except:
                if "~" in folder:
                    try:
                        folder=folder.replace("~", home, 1).replace("\\", "/").replace("C:", "")
                        files = os.listdir(folder)
                        print(str(f'{files}  ')[1:-1].replace(",", "").replace("'", ""))
                    except:
                        print("pyshell: ls: folder " + folder + " does not exist!")
                else:
                    print("pyshell: ls: folder " + folder + " does not exist!")
        else:
            print("pyshell: ls: command only takes 1 argument!")

def python():
    cmdargs = fullcmd.partition(' ')[2]
    exec(cmdargs)

def q():
    exitpysh=True

def exebat():
    import subprocess
    try:
        subprocess.run([cmd], check = True, shell = True, stdout=subprocess.DEVNULL,
    stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError:
        print("pyshell: {}: Command does not exist!".format(cmd))

def touch(file=""):
    if file == "":
        file = fullcmd.split()[1]
    try:
        f = open(file, "x")
        f.close()
    except:
        print("pyshell: touch: An Error Has Occured")

def wrfile():
    content = fullcmd.split()[0].replace('"', '')
    file = fullcmd.split()[2]
    try:
        f = open(file, "w")
        f.write(content)
        f.close()
    except:
        print("pyshell: >: An Error Has Occured")

def apfile():
    file = fullcmd.split()[2]
    content = fullcmd.split()[0].replace('"', '')
    try:
        f = open(file, "a")
        f.write(content)
        f.close()
    except:
        print("pyshell: >>: An Error Has Occured")

if not __name__ == "__main__":
    exitpysh = True
else:
    cmd=""
    fullcmd=""
    cd("C:\\Users\\{}".format(USR))
    cwd = os.getcwd()
    home = "{0}".format(cwd)
    cwd=cwd.replace(home, "", 1)
    cdm = "~" + cwd.replace("\\", "/")
    cd("~")

while exitpysh == False:
    cwd = os.getcwd()
    cwd=cwd.replace(home, "", 1)
    if not "C:" in cwd:
        cdm = "~" + cwd.replace("\\", "/")
    else:
        cwd=cwd.replace("C:", "", 1)
        cdm = cwd.replace("\\", "/")
    cmdf = False
    cpi = "{USR}@{usrOS}:{cdm}$ ".format(usrOS=usrOS.lower(), USR=USR.lower(), cdm=cdm)
    cmd = input(cpi)
    fullcmd = cmd
    cmd = cmd.split()[0]
    for cmdn, cmdn in scmd.items():
        if cmdn == cmd:
            cmdf = True
            eval(cmd+'()')
    if cmdf != True:
        if '>' in fullcmd:
            if '>>' in fullcmd:
                apfile()
            else:
                wrfile()
        else:
            if '=' in fullcmd:
                try:
                    var_name=fullcmd.split()[0]
                    var_data=fullcmd.split()[2]
                    set_var(var_name, var_data)
                except:
                    try:
                        fullcmd=fullcmd.replace("=", " ")
                        var_name=fullcmd.split()[0]
                        var_data=fullcmd.split()[1]
                        set_var(var_name, var_data)
                    except:
                        print(f'pyshell =: an error has occured')
            else:
                if './' in cmd:
                    try:
                        file=cmd.replace("./", "")
                        exec(open(file).read())
                    except:
                        print("pyshell: run: file {} not found or not in correct format!".format(file))
                else:
                    try:
                        exec(cmd)
                    except:
                        print("pyshell: {}: Command does not exist!".format(cmd))