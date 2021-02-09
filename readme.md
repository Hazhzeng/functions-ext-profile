### How To Use

1. Install this Python package by adding to your **requirements.txt**

```python
azure-functions
git+https://github.com/Hazhzeng/functions-ext-profile@master
```

2. Set `PYTHON_ENABLE_WORKER_EXTENSIONS="true"` and `PYTHON_ISOLATE_WORKER_DEPENDENCIES="true"` in your environment variable

3. Run the function app with `func host start`

### Collect Result from Stdout

Example:
```
HttpTriggerExperiment Stats: [Memory Usage 843776 bytes] [IO Read/Write Count 8/0] [IO Read/Write Bytes 13277/0]
```