
dotest:
	py.test

install:
	sudo python setup.py install

sdist:
	python setup.py sdist

clean:
	rm -rf *.egg-info
	rm -rf build
	find . -name \*.pyc | xargs rm -f

realclean:	clean
	rm -rf dist
	find . -name \*~ | xargs rm -f
	find . -name \*.so | xargs rm -f
	find . -name __pycache__ | xargs rm -rf

