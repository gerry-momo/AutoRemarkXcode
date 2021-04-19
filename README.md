# AutoRemarkXcode

### Automatically add Remark for Swift UI file in Xcode

#### 自动为swift ui 项目下的.swift 文件添加形如 // VStack 的备注
#### 全自动拯救双眼 


## 使用方法

#### 1.直接运行 可执行文件 AutoRemarkXcode 或者main.py (py3)
#### 2.输入项目目录，回车
#### 3.自动扫描该目录下所有的swift文件，并处理添加备注
#### 4.处理结束，按回车跳回步骤3重新处理

## 警告

#### 本项目为python自动化脚本，会完全替换原始代码文件（不会处理非swift结尾文件）
#### 首次使用前请注意备份自己的代码，以免出现意外情况
#### 个性化定制请直接自行修改handler/markit.py


##### 破事水：xcode都超过20G了..为什么连1.7G的idea都打不过...
