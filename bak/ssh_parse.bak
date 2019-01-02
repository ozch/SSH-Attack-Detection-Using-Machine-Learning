import time
import ipaddress
class ParseUbuntu:
    # [internal,failed,td,root,root_access,attempts]
    # dict = { IP:{internal:"",root:"",failure,td,}}
    dict = {}
    number_of_failure = 0
    def GetFailure(self):
        return self.number_of_failure
    def parsingAbort(self,str_):
        if str_.find("Server listening") != -1:
            return 1
        if str_.find("disconnect") != -1:
            return 1
        if str_.find("Received disconnect") != -1:
            return 1
        if str_.find("Removed session") != -1:
            return 1
        if str_.find("New session") != -1:
            return 1
        if str_.find("Disconnected from user") != -1:
            return 1
        if str_.find("session closed") != -1:
            return 1
        if str_.find("disconnected by user") != -1:
            return 1
        if str_.find("Connection closed") != -1:
            return 1
        return 0

    def getInfoAccepted(self,str_):
        if str_.find("Accepted password for") != -1:
            loc_start = str_.find("from ") + len("from ")
            loc_end = str_.find("port")
            self.number_of_failure = 0
            return str_[loc_start:loc_end - 1]
        else:
            return "-1"

    def GetFailedPasswordIP(self,str_):
        if str_.find("Failed password for ") != -1:
            loc_start = str_.find("from ") + len("from ")
            loc_end = str_.find("port")
            return str_[loc_start:loc_end - 1]
        else:
            return "-1"

    def GetFirstFailedPasswordIP(self,str_):
        if str_.find("authentication failure;") != -1:
            loc_start = str_.find(" rhost=") + len(" rhost=")
            loc_end = str_.find("  user=")
            return str_[loc_start:loc_end]
        else:
            return "-1"
    def SshProcessed(self,str_):
        t = time.time()
        td = 0
        is_failure, is_root, is_valid, user, ip = self.SshMonitor(str_)
        is_private = 1
        if user != "-1" or ip != "-1":
            print("IP ADDRESS : "+ip[:len(ip)-2]+"  ORIGINAL : "+ip)
            print("USER : " + user)
            print("IS ROOT : " + str(is_root))
            print("IS VALID: " + str(is_valid))
            print("IS FAILURE: " + str(is_failure))
            is_private = int(ipaddress.ip_address(ip[:len(ip)-2]).is_private)
            print("IS PRIVATE: " + str(is_private))
        num = self.number_of_failure
        if user != "-1" or ip != "-1":
            if self.dict.get(ip) != None:
                t_old = self.dict[ip]["td"]
                td = int(t)-int(t_old)
                self.dict.update({ip:{"is_private":is_private, "is_failure": is_failure , "is_root": is_root , "is_valid": is_valid , "user": user , "no_failure":num,"td":int(td)}})
            else:
                td = int(t)
                self.dict.update({ip: {"is_private":is_private,"is_failure": is_failure, "is_root": is_root, "is_valid": is_valid, "user": user,"no_failure": num, "td": td}})
                #self.dict[ip]='{"is_failure": "{0}" , "is_root": "{1}" , "is_valid": "{2}" , "user": "{3}" , "ip": "{4}" ,"no_failure": "{5}","td":"{6}"}'.format(str(is_failure), str(is_root), str(is_valid), user, ip,str(self.number_of_failure),str(int(t)))
        #printing dict
        #print(self.dict)
        return is_private,is_failure, is_root, is_valid, user, ip,td,self.number_of_failure
    def SshMonitor(self,str_):
        is_failure = 1
        is_valid = 1
        ip = ""
        ip = self.GetFirstFailedPasswordIP(str_)
        if ip == "-1":
            ip = self.GetFailedPasswordIP(str_)
            if ip == "-1":
                ip = self.getInfoAccepted(str_)
                if ip == "-1":
                    ip = "-1"
                    return 0, 0, 0, "-1", "-1"
        if str_.find("authentication failure;") != -1:
            loc_start = str_.find(" user=") + len(" user=")
            loc_end = str_.rfind("n")
            user = str_[loc_start:loc_end - 1]
            if user.find("root") != -1:
                is_root = 1
            else:
                is_root = 0
            is_failure = 1
            is_valid = 1
            self.number_of_failure = self.number_of_failure + 1
            return is_failure, is_root, is_valid, user, ip
        elif str_.find("Accepted password for") != -1:
            loc_start = str_.find("Accepted password for ") + len("Accepted password for ")
            loc_end = str_.find(" from")
            user = str_[loc_start:loc_end]
            if user.find("root") != -1:
                is_root = 1
            else:
                is_root = 0
            is_failure = 0
            is_valid = 1
            self.number_of_failure = 0
            return is_failure, is_root, is_valid, user, ip
        elif str_.find("Failed password for") != -1:
            if str_.find("invalid user") != -1:
                is_valid = 0
                loc_start = str_.find("Failed password for invalid user ") + len("Failed password for invalid user ")
                loc_end = str_.find(" from")
                user = str_[loc_start:loc_end]
            else:
                loc_start = str_.find("Failed password for ") + len("Failed password for ")
                loc_end = str_.find(" from")
                user = str_[loc_start:loc_end]
            if user.find("root") != -1:
                is_root = 1
            else:
                is_root = 0
            is_failure = 1

            self.number_of_failure = self.number_of_failure + 1
            return is_failure, is_root, is_valid, user, ip
        elif str_.find("Invalid user ") != -1:
            loc_start = str_.find("Invalid user ") + len("Invalid user ")
            loc_end = str_.find(" from")
            user = str_[loc_start:loc_end]
            is_root = 0
            is_failure = 1
            is_valid = 0
            self.number_of_failure = self.number_of_failure + 1
            return is_failure, is_root, is_valid, user, ip
        else:
            return 0, 0, 0, "-1", ip