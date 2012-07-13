import urllib2, base64, json

api_url = 'https://YOURFORMNAME.wufoo.com/api/v3/forms/FORMID/'
password = 'GET-THIS-FROM-WUFOO'

def wufoo_get(url):
	request = urllib2.Request(url)
	username = password
	base64string = base64.encodestring('%s:%s' % (username, password))[:-1]
	request.add_header("Authorization", "Basic %s" % base64string)   
	result = urllib2.urlopen(request)
	return result.readlines()
	
def get_entry_count():
	entries = wufoo_get(api_url + 'entries/count.json')
	entry_count = json.loads(entries[0])['EntryCount']
	return int(entry_count)

def get_entries():
	entry_count = get_entry_count()
	i = 0
	page_size = 100
	entry_list = []
	while i < entry_count:
		entries = wufoo_get(api_url + 'entries.json?pageStart=' + str(i) + '&pageSize=' + str(page_size))
		entry_list.append(json.loads(entries[0])['Entries'])
		i = i + page_size
	return entry_list