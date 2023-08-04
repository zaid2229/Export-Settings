

import frappe
from frappe import _

@frappe.whitelist()
def get_export_fields(doctype, docname):
    # Check if the 'Export Settings' document exists
    if frappe.db.exists('Export Settings', docname):
        # Fetch the selected fields for the given doctype with 'is_selected' set to 1
        selected_fields = frappe.get_all('Selected Field',
                                         filters={'parent': docname,
                                                  'reference_doctype': doctype,
                                                  'is_selected': 1},
                                         fields=['fieldname', 'is_selected'])
    else:
        # Fetch the standard fields for the doctype
        meta = frappe.get_meta(doctype)
        selected_fields = [{'fieldname': field.fieldname, 'is_selected': 1} for field in meta.fields]

    return selected_fields


# import frappe
# from frappe.utils import cstr
# from frappe.utils.csvutils import build_csv_response
# import pandas as pd
# import openpyxl

# @frappe.whitelist()
# def download_data_as_csv(doctype, fields):
#     # Fetch the data
#     data = frappe.get_all(doctype, fields=fields)

#     # Convert the data to a list of lists and prepend the fieldnames
#     data = [[cstr(value) for value in row.values()] for row in data]
#     data.insert(0, fields)

#     # Create the CSV response
#     return build_csv_response(data, doctype)

# @frappe.whitelist()
# def download_data_as_excel(doctype, fields):
#     # Fetch the data
#     data = frappe.get_all(doctype, fields=fields)

#     # Convert the data to a DataFrame
#     df = pd.DataFrame(data)

#     # Create the Excel file
#     filename = frappe.generate_hash(doctype) + ".xlsx"
#     filepath = frappe.get_site_path('private', 'files', filename)
#     df.to_excel(filepath, index=False)

#     # Create the File doc
#     file_doc = frappe.get_doc({
#         'doctype': 'File',
#         'file_name': filename,
#         'file_url': '/private/files/' + filename,
#         'is_private': 1
#     })
#     file_doc.save()

#     # Return the download URL
#     return file_doc.file_url

