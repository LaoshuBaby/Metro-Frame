## OpenMetro
Maybe the best Metro application in the World

若要使用其他语言的README文件，请点击[这里](./Docs/Readme/zh_CN.md)



## 造轮子，造个P的轮子

https://www.openmetromaps.org/

https://www.openmetromaps.org/

https://www.openmetromaps.org/

https://www.openmetromaps.org/

https://www.openmetromaps.org/

https://www.openmetromaps.org/

https://www.openmetromaps.org/

https://www.openmetromaps.org/

https://www.openmetromaps.org/

https://www.openmetromaps.org/

https://www.openmetromaps.org/

https://www.openmetromaps.org/

https://www.openmetromaps.org/

https://www.openmetromaps.org/

https://www.openmetromaps.org/

https://www.openmetromaps.org/

https://www.openmetromaps.org/

https://www.openmetromaps.org/

https://www.openmetromaps.org/

https://www.openmetromaps.org/

https://www.openmetromaps.org/

https://www.openmetromaps.org/

https://www.openmetromaps.org/

https://www.openmetromaps.org/

https://www.openmetromaps.org/

https://www.openmetromaps.org/

https://www.openmetromaps.org/





## 

该项目由中国各地的地铁迷和程序员进行维护

欢迎您来为这个世界上最大最全的地铁应用添砖加瓦

您用过手机地铁地图软件吗？
惊艳于农家乐审美的UI？
惊喜于几年前的老旧线路图？
惊吓于天马行空不着调的换乘算法？
您想过换用一个更好更全面更专业的平台吗？
……
没错，苦恼于从不更新维护，收录极其有限的国内各路地铁软件，我们脑海中萌发了这样一个创想，想要开发一个框架，留足各类接口，仅提供一个读取文件化了的地图的框架，在框架上加载各种插件。诸如换乘设计，诸如站内客流量，诸如地铁客流分析。
我们希望把这个框架做成一个非盈利的开源项目，面向世界用户，向世界开放。

您，也曾想过吧？


现在，给您这个实现过去期望的机会！
加入Metro Frame开源项目组！
和我们一同绘制世界上最详细最完善的地铁地图，和我们一起开发最精悍的信息框架！

官方QQ群：862894200




主体思想：一切皆文件——Linux
我们希望能抛弃以前的图层叠加的形式来表现地铁线路图，不再和之前的各类应用一样。我们希望纯粹的在每一个城市的数据包中仅保存足够的地铁站信息，足够的线路信息，由即时运算直接生成线路图，做到任何一个更改，只要对数据文件做增减，即可实时刷新显示变动。真正将地铁图轻量化，数据化。这将是一种全新的文件格式来储存。




工作方式：框架与插件通过接口实现数据交换
框架负责读取地图文件，并通过接口向各个插件交付信息。
插件用来实现功能，如实时绘制地铁图，如计算换乘信息等。

插件与框架可分为多个不同的进程，分别交由不同的核心运算。即使一个插件崩溃，也不会影响其他插件的运作。同时实现异步。框架相当于本机服务器。
维护方式：分团队维护与添加插件
核心维护团队不定期发布最新的框架

地图维护团队不定期更新地图。地图格式基本不变动。只做增减和新“标签”的增添。
插件更新团队负责开发各种功能插件。（过于老旧的插件可能无法在新框架上运行）
欢迎世界各地的轨道交通爱好者和我们一起不断维护这个开源项目。




## 感谢（Acknowledge）

为本项目提供产品层次上的指导的威尔先生

BUCT计科系的几位努力敲代码的学长们

肯为本项目开一个接口，作为MF的在线地图引擎之一的先生

百度地图开放的API使我们获取了世界上一百多个城市的地铁信息（当然还是有待完善的）

以及全国各地的积极校对自己城市内地铁信息的地铁迷们。正是因为有了你们，才能够发展完善


## 联系我们

[Metro Frame 官方QQ讨论群](<a target="_blank" href="//shang.qq.com/wpa/qunwpa?idkey=e885023e2c1be1d7029f1df09c4bb914c33e654b159307044f1f86c138665113"><img border="0" src="//pub.idqqimg.com/wpa/images/group.png" alt="Metro Frame Users" title="Metro Frame Users"></a>)

或扫描下方二维码进入

<p align="center">
<a href="https://github.com/LaoshuBaby/Metro-Frame">
    <img src="https://github.com/LaoshuBaby/Metro-Frame/edit/master/Metro_Frame_Users.jpg" alt="">
  </a>

