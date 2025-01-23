from notebook.auth import passwd
c = get_config()
c.NotebookApp.password = passwd("8$mFbOiDfQVbn3k2AxQIF2fQ$bZ0CkZZIBW4YK+TTehiUBv9qgQc6h7HFxceitKCQshM")
c.NotebookApp.open_browser = False
c.NotebookApp.ip = '0.0.0.0'
c.NotebookApp.port = 8888