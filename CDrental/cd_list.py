class CDList(object):
	def __init__(self):
		self.cdlist = {}

	def add_cd(self, cd):
		self.cdlist[cd.cd_id] = cd.cd_status

