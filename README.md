# pytorch-image-classification

- 下载 anaconda: https://docs.anaconda.com/anaconda/install/mac-os/
- 创建一个虚拟环境
```
conda info --envs
conda create --name <ENV_NAME>
conda activate <ENV_NAME>
```

- 安装 pytorch
```
conda install pytorch torchvision -c pytorch
```

- 更新anaconda镜像为国内服务器

* https://mirror.tuna.tsinghua.edu.cn/help/anaconda/
* 执行 `conda info` 查看文件 .condarc 的位置

- 安装Jupyter
```
conda install jupyter
``` 

- 检查当前虚拟环境中安装的包的列表
```
conda list -n <ENV_NAME>
```

- 启动jupyter
```
jupyter notebook
```
