class CD(object):
	def __init__(self, cd_id, cd_status):
		self.cd_id = cd_id
		self.cd_status = cd_status

	def is_rented(self, cd1):
		return cd1.cd_status