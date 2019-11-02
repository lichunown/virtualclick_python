# python版按键精灵

## 依赖

- matplotlib
- keyboard
- PIL
- argparse


## 目前实现功能

- 在指定区域单击或双击

## 存在问题

- 我为啥要用matplotlib进行截屏呢？打包文件好大

## 打包方式

**由于存在utf8编码，所以需要对一些骚操作**

```bash
chcp 65001 
pyinstall -F main.py 
```