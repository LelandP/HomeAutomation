from os.path import dirname, basename, isfile
import glob

def get_all_plugins():
	"""
	Get all the name of all the modules in this plugin dir
	"""
	modules = glob.glob(dirname(__file__)+"/*.py")
	return [ basename(f)[:-3] for f in modules if isfile(f) and not f.endswith('__init__.py')]