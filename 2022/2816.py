import sys

a = int(input())
channel_list = [sys.stdin.readline().strip() for i in range(a)]
i = 0
command = ''
while channel_list[i] != "KBS1" and channel_list[i] != "KBS2":
    command = command + '1'
    i += 1
found_channel = channel_list[i]
while i > 0:
    channel_list[i] = 'ABC'
    command = command + '4'
    i -= 1
channel_list[0] = found_channel

if found_channel == "KBS1":
    while channel_list[i] != "KBS2":
        command = command + '1'
        i += 1
    while i > 1:
        command = command + '4'
        i -= 1
else:
    while channel_list[i] != "KBS1":
        command = command + '1'
        i += 1
    while i > 0:
        command = command + '4'
        i -= 1

print(command)
