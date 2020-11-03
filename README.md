Miasm
========

This is a IDA plugin that integrates several modules of miasm

Installation
========

Before installing this plugin,you should install the miasm module.
And then copying file `MiasmPlugin.py` and directory `miasm_modules` into IDA's `plugins` directory

USAGE
=======

For example:

*********************************
**IDA 7.0 versoin**
********************************

symbol execution


**1.First step**


Select an area


![image](GIF/2.png)


**2.Second step**


1) Click the "Python Miasm Plugin" in the plugin

2) Click the symbol_exec


![image](GIF/1.png)

**3.result**

![image](GIF/3.png)

********************************
**Greater than IDA 7.0 versoin**
********************************

![image](GIF/4.png)

All the options are here


Origin
=======

These code come from the modification of miasm module


https://github.com/cea-sec/miasm/tree/master/example/ida
