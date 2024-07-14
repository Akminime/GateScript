# What is Gate Script?

## Short Description
- Gate Script is a custom programming language. It is a simple, compiled language that allows users to declare, assign values, and print variables. More features will be added with time. The language is designed to be easy to understand and learn. Gate Script files have a **.gate** extension and can be compiled or run using the **Gate.py** command-line interface. The **gatelib.py** file contains the core interpreter logic for Gate Script. Once you have compiled a gate script file, it will be compiled into a .gs file intead of the corresponding .gate file. The debugger is not finished but once it is I will start to work on the compiler. For help on how to use Gate Script use
```
Gate.py -h
```

## Examples

```GateScript
var, int:testAlpha
set, testAlpha:15
prnt, testAlpha
```