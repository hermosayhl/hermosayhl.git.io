import os


file_names = os.listdir('./')
file_names = [it for it in file_names if('py' not in it)]
for it in file_names:
	os.rename(it, it.replace('(', '-').replace(')', '-').replace(' ', '').replace('（', '-').replace('）', '-'))