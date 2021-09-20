# log Mod

RQAlpha log Mod，supporting logbook output

## Enable/Disable log Mod

```bash
# Disable log Mod
$ rqalpha mod disable log

# Enable log Mod
$ rqalpha mod enable log
```

## Mod Config

Configs of log Mod are as followed.

```python
{
    # Specify the log output file
    "log_file": "./log.txt",
    # Python open() method to read/write file
    "log_mode": "a",
}
```

## Extended Command

With this mod enabled, you can use follow function:


- `rqalpha run` command can use `--log-file file_path` option to export the log to `file_path` location
- `rqalpha run` command can use `--log-mode log_mode` option，which is the 'mode' param in  python built-in `open()` method，to determine how to read/write the output log file