class CD(object):
	def __init__(self, cd_id, cd_status):
		self.cd_id = cd_id
		self.cd_status = cd_status

	def is_rented(self):
		return self.cd_status

	def change_status(self):
		self.cd_status = "Rented"