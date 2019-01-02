import csv
class SSHDataAddition:
    df = ['user', 'is_private', 'is_failure', 'is_root', 'is_valid', 'not_valid_count', 'ip_failure', 'ip_success','no_failure', 'first', 'td', 'ts', 'class']

    def __init__(self):
        print("Initializing data addition modules")

    def writeSSH(self,df_temp):
        print(df_temp)
        icmp_writer = csv.DictWriter(open('data/SSH.csv', 'a+'), fieldnames=self.df)
        icmp_writer.writerow(df_temp)