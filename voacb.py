'''
Made by Ashutosh Maheshwari
Vocabulary Notifications
'''

import notify2
import random
from time import sleep

fw = open('dict.txt', 'r')
vocab = fw.read() #Read the content from file and then split it in list at new line
vocab = vocab.split('\n')


def sendmessage(title, message):
    '''Function to show notifications'''
    notify2.init("Test")
    notice = notify2.Notification(title, message)
    notice.show()
    return


while True:
    i = random.randint(0, len(vocab) - 1) #Random number from 0 to length of list -1
    if i % 2 == 0:
        sendmessage(vocab[i], vocab[i + 1]) #Title at the i-th even location with its meaning at the (i+1)-th location
        sleep(50)
    else:
        continue
