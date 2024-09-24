# GDB的`layout`

* 来源: [layout](https://blog.csdn.net/KgdYsg/article/details/82453980)

用gdb调试c代码，可用`layout`分割窗口，一边查看代码，一边测试。用起来非常方便！

## 1 - 主要用法

* layout `src`  : 显示源代码窗口
* layout `asm`  : 显示汇编窗口
* layout `regs` : 显示源代码、汇编和寄存器窗口
* layout `split`: 显示源代码和汇编窗口
* layout `prev` : 显示上一个layout
* layout `next` : 显示下一个layout

## 2 - 快捷键

* Ctrl + `L`      : 刷新窗口(`P.S. 调试几轮后屏幕就会显示错乱`)
* Ctrl + `x` + `1`: 单窗口模式，显示一个窗口
* Ctrl + `x` + `2`: 双窗口模式，显示两个窗口
* Ctrl + `x` + `a`: 退出layout，回到执行layout之前的调试窗口

---

`2024/9/24`
