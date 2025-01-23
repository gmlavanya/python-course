from notebook.auth import passwd
c = get_config()
c.NotebookApp.password = passwd("sha1:5a52a62c0dc47a322e7d8169c70d1c529c3e8932")
c.NotebookApp.open_browser = False
c.NotebookApp.ip = '0.0.0.0'
c.NotebookApp.port = 8888
