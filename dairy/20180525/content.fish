第0(0(145)周
问题: 平台打开慢
定位: 基础模板中加载了大量js\css, js加载本地image.
处理:
基础模板保留jquery/bootstrap这样的所有页面都有的基础模块,
各个页面所需其他模块,
在该页面单独加载,
这需要对各个页面非常熟悉,
少了js将会是功能问题.

定位到js加载image的代码,
发现全是些背景资源,
这个前端框架,
无论是做法还是所实现的东西,
真的很垃圾,
使用的模块:

Highcharts JS v2.3.3 (2012-10-04)
Javascript plotting library for jQuery, v. 0.7.
Released under the MIT license by IOLA, December 2007.

可见一斑...

直接取消了部分image作为背景,
页面清爽多了.