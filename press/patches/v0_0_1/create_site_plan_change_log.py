# Copyright (c) 2020, Frappe Technologies Pvt. Ltd. and Contributors
# MIT License. See license.txt

from __future__ import unicode_literals
import frappe


def execute():
	frappe.reload_doc("press", "doctype", "site_plan_change")
	for site in frappe.db.get_all("Site", {"status": "Active"}, ["name"]):
		frappe.get_doc("Site", site.name)._create_initial_site_plan_change()