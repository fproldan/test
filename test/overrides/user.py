import frappe
from frappe.core.doctype.user.user import User


class CustomUser(User):

	def is_system_manager_disabled(self):
		"""
		HASH: c157564281a786fba0835fd58310947074e56772
		REPO: https://github.com/frappe/frappe/
		PATH: frappe/core/doctype/user/user.py
		METHOD: is_system_manager_disabled
		"""		
		print("Custom code")
		return frappe.db.get_value("Role", {"name": "System Manager"}, ["disabled"])
	
	
	def validate_user_image(self):
		"""
		HASH: d00b20a610b9d04ddefb9ab5eb8c406c7fa0e6d3
		REPO: https://github.com/frappe/frappe/
		PATH: frappe/core/doctype/user/user.py
		METHOD: validate_user_image
		"""	
		if self.user_image and len(self.user_image) > 2000:
			frappe.throw(_("Not a valid User Image."))

	def set_full_name(self):
		"""
		HASH: ef2687768991f7677a349cacd967c77ca3935c68
		REPO: https://github.com/frappe/frappe/
		PATH: frappe/core/doctype/user/user.py
		METHOD: set_full_name
		"""	
		self.full_name = " ".join(filter(None, [self.first_name, self.last_name]))

	def ensure_unique_roles(self):
		"""
		HASH: 6e7e641a3a579631dd3f5d30c8784ca9daed30b1
		REPO: https://github.com/frappe/frappe/
		PATH: frappe/core/doctype/user/user.py
		METHOD: ensure_unique_roles
		"""	
		pass
