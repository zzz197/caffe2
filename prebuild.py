#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import shutil
import os
import sys
import subprocess

#Build_Folder_Name = "caffe_win"

def GenerateCppOut(protocPath, protoPath, caffe2Path):
    #cmdString = protocPath + " --cpp_out " + dstPath + " -I " + includePath + " " + protoPath
    cmdString = protocPath + " --cpp_out=" + caffe2Path +  " --proto_path=" + caffe2Path + " " + protoPath
    print(cmdString)
    returnCode = subprocess.call(cmdString)

def GeneratePyOut(protocPath, protoPath, caffe2Path):
    dstPath = os.path.join(caffe2Path , "caffe_win")    #项目工程地址
    cmdString = protocPath + " --python_out=" + dstPath + " --proto_path=" + caffe2Path + " " + protoPath
    print(cmdString)
    returnCode = subprocess.call(cmdString)

def CopyPythonFiles(dstPath, srcPath):
    fileList = os.listdir(srcPath)
    for iFile in fileList:
        [name, ext] = os.path.splitext(iFile)
        srcFile = os.path.join(srcPath, iFile)
        dstFile = os.path.join(dstPath, iFile)
        if ext == ".py" or ext == ".ipynb":
            shutil.copyfile(srcFile, dstFile)
        elif os.path.isdir(srcFile):
            if not os.path.exists(dstFile):
                os.makedirs(dstFile)
            CopyPythonFiles(dstFile, srcFile)


def RunPrebuild(caffe2Path):
    rootPath = os.path.dirname(os.path.dirname(caffe2Path))
    protocPath = os.path.join(rootPath, "A0000_common\\lib\\release\\win64\\protoc.exe")
    proto1Src = os.path.join(caffe2Path, "caffe\\proto")
    proto2Src = os.path.join(caffe2Path, "caffe2\\proto")

    #拷贝python脚本到指定目录
    dstPath = os.path.join(caffe2Path, "caffe_win\\caffe2\\python")
    srcPath = os.path.join(caffe2Path, "caffe2\\python")
    CopyPythonFiles(dstPath, srcPath)

    #处理caffe的proto
    protoList = os.listdir(proto1Src)
    for protoName in protoList:
        [name, ext] = os.path.splitext(protoName)
        if ext == ".proto":
            GenerateCppOut(protocPath, os.path.join(proto1Src, protoName), caffe2Path)
            GeneratePyOut(protocPath, os.path.join(proto1Src, protoName), caffe2Path)

	#处理caffe2的proto
    protoList = os.listdir(proto2Src)
    for protoName in protoList:
        [name, ext] = os.path.splitext(protoName)
        if ext == ".proto":
            GenerateCppOut(protocPath, os.path.join(proto2Src, protoName), caffe2Path)
            GeneratePyOut(protocPath, os.path.join(proto2Src, protoName), caffe2Path)

if __name__ == '__main__':
#    returnCode = subprocess.call('svm-toy.exe')
    caffe2Path = sys.path[0]
    RunPrebuild(caffe2Path)
