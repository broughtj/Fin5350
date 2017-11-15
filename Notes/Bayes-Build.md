For some reason on Bayes when you try to build `deacon` with the Makefile as follows:

```
$ make
```

You get the following error message:

```
$ make
python setup.py build_ext -if
Traceback (most recent call last):
  File "setup.py", line 3, in <module>
    from Cython.Build import cythonize
ImportError: No module named Cython.Build
Makefile:2: recipe for target 'all' failed
make: *** [all] Error 1
```

I have no idea why. Sorry. But you can still build it manually by issuing the following command:

```
$ python setup.py build_ext -if
```
