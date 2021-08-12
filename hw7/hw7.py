# Напишите программу, которая читает данные из файлов
# /etc/passwd и /etc/group на вашей системе и выводит
# следующую информацию в файл output.txt:
# 1. Количество пользователей, использующих все имеющиеся
# интерпретаторы-оболочки.
# ( /bin/bash - 8 ; /bin/false - 11 ; ... )
# 2. Для всех групп в системе - UIDы пользователей
# состоящих в этих группах.
# ( root:1, sudo:1001,1002,1003, ...)

passwd = open('passwd', 'r')
groups = open('group', 'r')
output = open('output.txt', 'w')

class User:
    def __init__(self, username, uid, pgid):
        self.username = username
        self.uid = uid
        self.pgid = pgid

shellsdict = {}
groupsdict = {}
uidict = {}
userspgids = []

for line in passwd:
    line = line.split(':')
    shell = line[-1].replace('\n','')
    if shell in shellsdict:
        shellsdict[shell] += 1
    else:
        shellsdict[shell] = 1
    user = line[0]
    uid = line[2]
    pgid = line[3]
    userspgids.append(User(user, uid, pgid))
    uidict[user] = uid

for line in groups:
    line = line.split(':')
    group = line[0]
    gid = line[2]
    users = line[-1][:-1].split(',')
    groupsdict[group] = []
    if users != ['']:
        groupsdict[group] = [uidict[user] for user in users]
    # Если группа - primary для пользователя, то его username в /etc/groups не указыватся
    for user in userspgids:
        if gid == user.pgid:
            groupsdict[group].append(user.uid)

for shell in shellsdict:
    output.write(f'{shell} - {shellsdict[shell]}\n')
output.write('\n')
for group in groupsdict:
    output.write(f'{group}: {" ".join(groupsdict[group])}\n')

passwd.close()
groups.close()
output.close()