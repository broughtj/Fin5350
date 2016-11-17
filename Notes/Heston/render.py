import subprocess

cmd = '''R -e "rmarkdown::render('heston.Rmd', output_format = 'all')"'''
subprocess.call(cmd, shell=True)

