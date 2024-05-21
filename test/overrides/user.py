import frappe
from frappe.core.doctype.user.user import User


class CustomUser(User):

	def is_system_manager_disabled(self):
		"""
		HASH: 171e1d0159cda3b8d9415527590c9c3ca0c827be
		REPO: https://github.com/frappe/frappe/
		PATH: frappe/core/doctype/user/user.py
		METHOD: is_system_manager_disabled
		"""		
		print("Custom code")
		return frappe.db.get_value("Role", {"name": "System Manager"}, ["disabled"])


	def validate_user_image(self):
		"""
		HASH: 0dee65cbe96beed05ba234e6614d9e91a3ed1894
		REPO: https://github.com/frappe/frappe/
		PATH: frappe/core/doctype/user/user.py
		METHOD: validate_user_image
		"""	
		print("Custom code")
		if self.user_image and len(self.user_image) > 2000:
			frappe.throw(_("Not a valid User Image."))

	def set_full_name(self):
		"""
		HASH: 0dee65cbe96beed05ba234e6614d9e91a3ed1894
		REPO: https://github.com/frappe/frappe/
		PATH: frappe/core/doctype/user/user.py
		METHOD: set_full_name
		"""	
		self.full_name = " ".join(filter(None, [self.first_name, self.last_name]))


	