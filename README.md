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
    "log_path": "./output/reposition_log.txt",
    # Python open() method to read/write file
    "log_mode": "a",
}
```