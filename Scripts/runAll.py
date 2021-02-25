# import os,sys
# os.system("python ./test_login.py")
# os.system("python ./test_top.py")
# os.system("python ./test_tab.py")
# os.system("python ./test_org.py")
# os.system("python ./test_com.py")
# sys.path.append(os.getcwd())
# lists = os.listdir(os.getcwd())
# for c in lists:
#     if os.path.isfile(c) and c.endswith('.py') and c.find("runAll") == -1:  # 去掉AllTest.py文件
#         print(c)
#         os.system("python ./%s" % c)# 改动
# import os
#
# lst = os.listdir(os.getcwd())
#
# for c in lst:
#     if os.path.isfile(c) and c.endswith('.py') and c.find("AllTest") == -1:  # 去掉AllTest.py文件
#         print(c)
#         os.system(os.path.join(os.getcwd(),c))
#         sys.path.append(os.getcwd())

#文件名是test_firstFile.py
#coding=utf-8

import pytest
import time

class Test_Pytest():

        def test_one(self):
                print("test_one方法执行" )
                time.sleep(1)
                assert 1==1

        def test_two(self):
                print("test_two方法执行" )
                time.sleep(1)
                assert "o" in "love"

        def test_three(self):
                print("test_three方法执行" )
                time.sleep(1)
                assert 3-1==2

if __name__=="__main__":
    pytest.main(['-s','-v','-n','3','runAll.py'])
    # pytest.main(['-s', '-v', 'runAll.py'])