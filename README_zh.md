# log Mod

RQAlpha 日志 Mod，实现日志输出

## 开启或关闭日志 Mod

```bash
# 关闭日志 Mod
$ rqalpha mod disable log

# 启用日志 Mod
$ rqalpha mod enable log
```

## 模块配置项

日志 Mod 的可用配置项如下

```python
{
    # 指定日志输出文件
    "log_path": "./output/reposition_log.txt",
    # python open() 方法读写文件的模式
    "log_mode": "a",
}
```