"""
垃圾邮件清理和恢复
    原理：正常和垃圾邮件文件分别存放到指定的目录下。即在在正常邮件文件目录下的就是正常邮件文件，垃圾邮件同理。
        垃圾邮件清理即是删除垃圾邮件目录下的垃圾邮件文件；
        垃圾邮件恢复即是将垃圾邮件目录下的垃圾邮件文件移动到正常邮件文件目录下

    目录结构：（可更改设置）
        src
            mail
                spamMail
                normalMail

"""
import shutil       # 文件移动
import os           # 文件删除

spamMailPath = "src/mail/spamMail"          # 垃圾邮件文件目录
normalMailPath = "src/mail/normalMail"      # 正常邮件文件目录

# 清理全部垃圾邮件
def spamCleanupAll():
    filelist = os.listdir(spamMailPath)     # 获得spamMailPath路径下的所有文件列表
    for file in filelist:
        filePath = os.path.join(spamMailPath, file)
        # print(filePath)
        os.remove(filePath)                     # 遍历并删除所有垃圾邮件文件

# 恢复全部垃圾邮件
def spamRecoveryAll():
    filelist = os.listdir(spamMailPath)     # 获得spamMailPath路径下的所有文件列表
    # print(filelist)
    for file in filelist:
        src = os.path.join(spamMailPath, file)
        dst = os.path.join(normalMailPath, file)
        # print('src:', src)
        # print('dst:', dst)
        shutil.move(src, dst)               # 移动到正常邮件文件目录

# 清理指定的一个垃圾邮件文件
def spamCleanup(fileName):
    filePath = os.path.join(spamMailPath, fileName)
    os.remove(filePath)

# 恢复指定的一个垃圾邮件文件
def spamRecover(fileName):
    srcFilePath = os.path.join(spamMailPath, fileName)
    dstFilePath = os.path.join(normalMailPath, fileName)
    shutil.move(srcFilePath, dstFilePath)

# 返回全部垃圾邮件文件列表，对应功能——显示所有垃圾邮件文件
def spamAll():
    return os.listdir(spamMailPath)

# 清理指定的多个垃圾邮件文件
def spamCleanups(fileNameList):
    for fileName in fileNameList:
        filePath = os.path.join(spamMailPath, fileName)
        os.remove(filePath)

# 恢复指定的多个垃圾邮件文件
def spamRecovers(fileNameList):
    for fileName in fileNameList:
        srcFilePath = os.path.join(spamMailPath, fileName)
        dstFielPath = os.path.join(normalMailPath, fileName)
        shutil.move(srcFilePath, dstFielPath)

# spamRecoveryAll()     # 测试恢复全部垃圾邮件文件——T
# spamCleanupAll()      # 测试清理全部垃圾邮件文件——T
# spamCleanup("001")    # 测试清理指定的一个垃圾邮件文件——T
# spamRecover("007")    # 测试恢复指定的一个垃圾邮件文件——T
# print(spamAll())      # 测试返回全部垃圾邮件文件的文件名列表——T
"""
# 测试清理指定的多个垃圾邮件文件——T
fileNameList = spamAll()
spamCleanups(fileNameList)
"""
"""
# 测试恢复指定的多个垃圾邮件文件——T
fileNameList = spamAll()
spamRecovers(fileNameList)
"""

