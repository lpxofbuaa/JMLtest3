# BUAA-OO-JML-HOMEWORK3-AutoTest

## How to use

- （本脚本为作业互测对拍工具，纯属娱乐
- 前提准备：
    - `windows`系统，`python3`环境，装有`subprocess`,`OS`,`random`,`time`,`shutil`,`sys`等包。
    - 为所有对拍成员在`.\classes\`目录下创建对应`name`文件夹，将`java`源文件按包结构放入，例如`.\classes\name1\helloworld.java`
    - 编译非必要工作，`init`有编译功能。

- 第一次使用：
    - `cmd`或`powershell`：

            python init.py

    - 根据提示创建对拍名单，并设置数据生成器模式
- 非第一次使用：
    - 方式一：通过使用`init`接口创建对拍名单重新使用，若对拍名单不需更改，则如下启动，其中`<total>`为测试总数，0代表无限，`<mode>`为数据生成模式，详见`init.py`手册

            python init.py -r <total> <mode>
    
    - 方式二：在`cmd`或`powershell`下使用：（格式同一）

            main <total> <mode>
- single_run模式（namelist已经创建完毕）：
    - 若仅想单独测试一个数据，可以将数据命名为`data<name>.txt`形式，`<name>`为任意字符串，然后在cmd或powershell中：

            python single_feeder.py <name> 
- 更多事项
    - 手动更改`namelist.txt`能更改对拍名单
    - init支持编译等其他接口，详见`init`手册
    - `efficient`文件夹数据为各成员运行效率，需要定期清理



