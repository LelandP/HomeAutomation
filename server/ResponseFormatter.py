import urllib
def add_href_to_list(url, in_list, key="id"):
    """
    """
    for item in in_list:
        item.update( {"href": url + "/" + urllib.quote_plus(item[key])})
    return in_list

def filter_dict(indict, exclude=None):
	"""
	"""
	#TO-DO: add include to only include X feilds

	if exclude is not None:
		if type(exclude) is list:
			for key in exclude:
				del indict[key]
		else:
			del indict[exclude]
	return indict
