from JumpScale import j

j.do.execute("rm -rf %s/ptpython*"%j.do.getPythonLibSystem())

j.do.execute("pip3 install docopt --upgrade")

j.do.execute("python3 setup.py install")


