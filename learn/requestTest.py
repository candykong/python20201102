#!/usr/bin/python
# -*- coding:UTF-8 -*-

import queue

userQueue = queue.Queue()
usernames = ['09876543215', '09876543217', '13107700873']
for username in usernames:
    userQueue.put(username)
print('ddd',userQueue.empty())
print(userQueue.get())
print(userQueue.get())
print(userQueue.get())


