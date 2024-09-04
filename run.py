import platform,os
bit = platform.architecture()[0]
print(' CHECKING FOR UPDATES');os.system('git pull')
if bit == '32bit':
    from data import BRZZRS32
elif bit == '64bit':
    from data import BRZZRS64
else: exit(" SORRY YOUR DEVICE DOESN'T SUPPORT THIS TOOL USE 32/64 BIT PHONE");exit()
