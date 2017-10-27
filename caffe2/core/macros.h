#pragma once

// This is a placeholder. The real content will be generated by the cmake
// script.

#ifndef CAFFE2_USE_EIGEN_FOR_BLAS
#define CAFFE2_USE_EIGEN_FOR_BLAS
#endif // CAFFE2_USE_EIGEN_FOR_BLAS

#if 0 && (defined _MSC_VER) && !(defined __CUDACC__)

#ifndef CAFFE2_USE_GOOGLE_GLOG
#define CAFFE2_USE_GOOGLE_GLOG

#ifndef GOOGLE_GLOG_DLL_DECL
#define GOOGLE_GLOG_DLL_DECL 
#endif //GOOGLE_GLOG_DLL_DECL

#endif //CAFFE2_USE_GOOGLE_GLOG

#ifndef CAFFE2_UNIQUE_LONG_TYPEMETA
#define CAFFE2_UNIQUE_LONG_TYPEMETA
#endif // CAFFE2_UNIQUE_LONG_TYPEMETA

#ifndef CAFFE2_NO_BUILTIN_CPU_SUPPORTS
#define CAFFE2_NO_BUILTIN_CPU_SUPPORTS
#endif // CAFFE2_NO_BUILTIN_CPU_SUPPORTS

#ifndef CAFFE2_USE_GFLAGS
#define CAFFE2_USE_GFLAGS
#endif // CAFFE2_USE_GFLAGS

#endif //0 && (defined _MSC_VER) && !(defined __CUDACC__)

#ifdef _MSC_VER
#pragma comment(lib, "Shlwapi.lib")
#pragma comment(lib, "Rpcrt4.lib")
#pragma comment(lib, "ntdll.lib")
#endif //MSC_VER