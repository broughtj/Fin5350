import subprocess

cmd = '''R -e "rmarkdown::render('heston.Rmd')"'''
subprocess.call(cmd, shell=True)

