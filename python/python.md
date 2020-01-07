# python源码剖析

## python总体框架理解

![image-20200102195735413](/Users/fanding/gitProjects/notes/python/src/image-20200102195735413.png)

## 编译python

![image-20200102203638085](/Users/fanding/gitProjects/notes/python/src/image-20200102203638085.png)

- 编译时遇到的问题
  - mac系统在编译python2.5时有点不兼容，所以改为了python3.7.6
  - 安装成功

## 第一章python对象初探

- 对象理解

  ![image-20200102215422173](/Users/fanding/gitProjects/notes/python/src/image-20200102215422173.png)

- 对象一旦被创建，内存大小就不会再改变，通过维护一个指针，来指向一块可变内存，进而来维护动态变化的数据

  ![image-20200103113444519](/Users/fanding/gitProjects/notes/python/src/image-20200103113444519.png)

### 代码层面理解对象

- pyobject代码	![image-20200103114309797](/Users/fanding/gitProjects/notes/python/src/image-20200103114309797.png)

### 创建对象

- 泛型api（内建对象）

  ![image-20200102231629311](/Users/fanding/gitProjects/notes/python/src/image-20200102231629311.png)

- 与类型相关api（内建对象）

  ![image-20200102231701037](/Users/fanding/gitProjects/notes/python/src/image-20200102231701037.png)

- 对象分类

  ![image-20200103111646684](/Users/fanding/gitProjects/notes/python/src/image-20200103111646684.png)

## 第二章python中的整数对象

