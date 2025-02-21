# Copyright (c) 2023, zaid and contributors
# For license information, please see license.txt

import frappe
import json
from frappe.model.document import Document

class ExportSettings(Document):
	pass


@frappe.whitelist()
def get_doctype_fields(doctype):
    meta = frappe.get_meta(doctype)
    fields = [
        {
            'fieldname': field.fieldname, 
            'label': field.label
        } 
        for field in meta.fields 
        if field.fieldtype not in ['Section Break', 'Column Break', 'HTML', 'Table', 'Button', 'Image', 'Fold']
    ]
    return fields

@frappe.whitelist()
def get_selected_fields(docname, doctype):
    # Fetch the selected fields for the given parent document and doctype
    selected_fields = frappe.get_all('Selected Field',
                                     filters={'parent': docname,
                                              'reference_doctype': doctype},
                                     fields=['fieldname', 'is_selected'])
    return selected_fields



@frappe.whitelist()
def save_selected_fields(parent, data, doctype):
    # Convert the data from JSON format to Python
    data = json.loads(data)

    # Delete the old selected fields
    frappe.db.sql("""DELETE  FROM `tabSelected Field` WHERE parent = %s""", parent)

    # Save the new selected fields
    for field in data:
        doc = frappe.get_doc({
            'doctype': 'Selected Field',
            'parent': parent,
            'parentfield': 'selected_fields',
            'parenttype': 'Export Settings',
            'fieldname': field['fieldname'],
            'is_selected': field['is_selected'],
            'reference_doctype': doctype,
        })
        doc.insert(ignore_permissions=True)

