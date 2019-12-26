

# 操作系统笔记

## 引用

```
https://www.youtube.com/watch?v=ujVSQDPwdOE&list=PLg5ULjirtivtd1p89jL5t1SKU6batBysz&index=8
```



## 系统调用

![image-20191225161656493](/Users/fanding/gitProjects/notes/os/img/image-20191225161656493.png)

![image-20191225162434412](/Users/fanding/gitProjects/notes/os/img/image-20191225162434412.png)

## 两种指令、两种处理器状态、两种程序

![image-20191225162919424](/Users/fanding/gitProjects/notes/os/img/image-20191225162919424.png)

![image-20191225163032358](/Users/fanding/gitProjects/notes/os/img/image-20191225163032358.png)

![image-20191225163125504](/Users/fanding/gitProjects/notes/os/img/image-20191225163125504.png)

![image-20191225163210002](/Users/fanding/gitProjects/notes/os/img/image-20191225163210002.png)

## 内核

![image-20191225163535237](/Users/fanding/gitProjects/notes/os/img/image-20191225163535237.png)

## 中断和异常

![image-20191225163946364](/Users/fanding/gitProjects/notes/os/img/image-20191225163946364.png)

![image-20191225164526158](/Users/fanding/gitProjects/notes/os/img/image-20191225164526158.png)

- 内中断和外中断
- ![image-20191225164806369](/Users/fanding/gitProjects/notes/os/img/image-20191225164806369.png)

## 进程

### PCB

![image-20191225182602602](/Users/fanding/gitProjects/notes/os/img/image-20191225182602602.png)

### 进程的组织方式

![image-20191225182906106](/Users/fanding/gitProjects/notes/os/img/image-20191225182906106.png)

- 索引方式

  ![image-20191225182935593](/Users/fanding/gitProjects/notes/os/img/image-20191225182935593.png)

- 链式组织

  ![image-20191225183017313](/Users/fanding/gitProjects/notes/os/img/image-20191225183017313.png)

### 进程总结

![image-20191225183529136](/Users/fanding/gitProjects/notes/os/img/image-20191225183529136.png)

### 进程状态转换

![image-20191225184836265](/Users/fanding/gitProjects/notes/os/img/image-20191225184836265.png)

### 进程控制与原语

![image-20191225194429662](/Users/fanding/gitProjects/notes/os/img/image-20191225194429662.png)

### 进程间通信

- 共享存储

  ![image-20191225194936338](/Users/fanding/gitProjects/notes/os/img/image-20191225194936338.png)

- 管道

  ![image-20191225195250596](/Users/fanding/gitProjects/notes/os/img/image-20191225195250596.png)

- 消息传递

  ![image-20191225212935511](/Users/fanding/gitProjects/notes/os/img/image-20191225212935511.png) 

- 进程通信总结

  ![image-20191225213027031](/Users/fanding/gitProjects/notes/os/img/image-20191225213027031.png)

## 线程

![image-20191225213737249](/Users/fanding/gitProjects/notes/os/img/image-20191225213737249.png)

### 内核级线程和用户级线程的关系

![image-20191225214312631](/Users/fanding/gitProjects/notes/os/img/image-20191225214312631.png)

### 多线程模型

- 多对一模型

![image-20191225214505058](/Users/fanding/gitProjects/notes/os/img/image-20191225214505058.png)

- 一对一模型

  ![image-20191225214640718](/Users/fanding/gitProjects/notes/os/img/image-20191225214640718.png)

- 多对多模型

  ![image-20191225214748087](/Users/fanding/gitProjects/notes/os/img/image-20191225214748087.png)

### 线程总结

![image-20191225215016603](/Users/fanding/gitProjects/notes/os/img/image-20191225215016603.png)

## 处理机调度

### 调度分类

![image-20191225220758900](/Users/fanding/gitProjects/notes/os/img/image-20191225220758900.png)

### 挂起模型

![image-20191225220209272](/Users/fanding/gitProjects/notes/os/img/image-20191225220209272.png)

### 挂起和阻塞的区别

![image-20191225220332472](/Users/fanding/gitProjects/notes/os/img/image-20191225220332472.png)

### 进程调度时机

![image-20191225221530690](/Users/fanding/gitProjects/notes/os/img/image-20191225221530690.png)

### 进程的调度方式

![image-20191225222514385](/Users/fanding/gitProjects/notes/os/img/image-20191225222514385.png)

### 进程调度算法

![image-20191226093747038](/Users/fanding/gitProjects/notes/os/img/image-20191226093747038.png)

- 先来先服务例子

  

  ![image-20191226094439546](/Users/fanding/gitProjects/notes/os/img/image-20191226094439546.png)

  ![image-20191226100009013](/Users/fanding/gitProjects/notes/os/img/image-20191226100009013.png)

- 短作业优先

  ![image-20191226100802827](/Users/fanding/gitProjects/notes/os/img/image-20191226100802827.png)

  ![image-20191226101307247](/Users/fanding/gitProjects/notes/os/img/image-20191226101307247.png)

- 高响应比优先

  ![image-20191226101805534](/Users/fanding/gitProjects/notes/os/img/image-20191226101805534.png)

- 时间片轮转（交互式系统）

  ![image-20191226103129308](/Users/fanding/gitProjects/notes/os/img/image-20191226103129308.png)

- 优先级调度（交互式系统）

  ![image-20191226172130379](/Users/fanding/gitProjects/notes/os/img/image-20191226172130379.png)

  ![image-20191226171708563](/Users/fanding/gitProjects/notes/os/img/image-20191226171708563.png)

- 多级反馈队列调度（交互式系统）

  ![image-20191226172954656](/Users/fanding/gitProjects/notes/os/img/image-20191226172954656.png)

## 进程同步

![image-20191226211549332](/Users/fanding/gitProjects/notes/os/img/image-20191226211549332.png)

### 进程互斥软件手段

- 单标记法

  ![image-20191226212228441](/Users/fanding/gitProjects/notes/os/img/image-20191226212228441.png)

- 双标记先检查法、双标记后检查法

  - 双标记先检查法：打破忙则等待

    ![image-20191226213226111](/Users/fanding/gitProjects/notes/os/img/image-20191226213226111.png)

  - 双标记后检查法：打破有限等待

    ![image-20191226213326877](/Users/fanding/gitProjects/notes/os/img/image-20191226213326877.png)

- peterson算法解决了以上两种算法的问题:打破让权等待
- ![image-20191226213816917](/Users/fanding/gitProjects/notes/os/img/image-20191226213816917.png)

### 进程互斥硬件手段

![image-20191226220211324](/Users/fanding/gitProjects/notes/os/img/image-20191226220211324.png)

### 死锁产生条件

![image-20191226225004672](/Users/fanding/gitProjects/notes/os/img/image-20191226225004672.png)