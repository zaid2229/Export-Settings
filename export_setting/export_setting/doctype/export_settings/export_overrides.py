# from frappe.core.doctype.data_export.exporter import export_data 
import frappe

# def export_data(doctype, all_doctypes, filters=None):
#     # Fetch the Export Settings for this Doctype
#     export_settings = frappe.get_all(
#         "Export Settings",
#         filters={"reference_doctype": doctype},
#     )

#     if export_settings:
#         # If there are Export Settings, fetch the selected fields
#         selected_fields = frappe.get_all(
#             "Selected Field",
#             filters={"parent": export_settings[0].name},
#             fields=["fieldname"],
#         )

#         # Extract the fieldnames from the selected_fields records
#         selected_fieldnames = [field["fieldname"] for field in selected_fields]

#         # Modify all_doctypes to only include the selected fields
#         all_doctypes = {
#             doctype: [field for field in doctype_fields if field.fieldname in selected_fieldnames]
#             for doctype, doctype_fields in all_doctypes.items()
#         }

#     # Call the original export_data function
#     return original_export_data(doctype, all_doctypes, filters)


# from frappe.core.doctype.data_export.data_export import DataExport

# def get_columns_for_data_export(self):
#     # Fetch the Export Settings for this Doctype
#     export_settings = frappe.get_all(
#         "Export Settings",
#         filters={"reference_doctype": self.ref_doctype},
#         fields=["*"],
#     )

#     if not export_settings:
#         # No export settings, revert to default behavior
#         return super(DataExport, self).get_columns_for_data_export()

#     # Fetch selected fields
#     selected_fields = frappe.call(
#         method='export_setting.export_setting.doctype.export_settings.export_settings.get_selected_fields',
#         args={
#             'docname': export_settings[0].name,
#             'doctype': self.ref_doctype
#         }
#     )

#     if selected_fields:
#         selected_fields = [d.fieldname for d in selected_fields]

#     columns = []
#     # Only include selected fields
#     for df in frappe.get_meta(self.ref_doctype).fields:
#         if df.fieldname in selected_fields:
#             columns.append(df)

#     return columns

# # Override the original method
# DataExport.get_columns_for_data_export = get_columns_for_data_export


# import frappe
# from frappe.core.doctype.data_export.exporter import export_data as original_export_data

# def export_data(doctype, all_doctypes, filters=None):
#     # Fetch the Export Settings for this Doctype
#     export_settings = frappe.get_all(
#         "Export Settings",
#         filters={"reference_doctype": doctype},
#         fields=["selected_fields"],
#     )

#     if export_settings:
#         selected_fields = export_settings[0].get('selected_fields', [])
#         all_doctypes = {
#             doctype: [field for field in doctype_fields if field.fieldname in selected_fields]
#             for doctype, doctype_fields in all_doctypes.items()
#         }

#     # Call the original export_data function
#     return original_export_data(doctype, all_doctypes, filters)

# # Override the original export_data function
# frappe.core.doctype.data_export.exporter.export_data = export_data


# @frappe.whitelist()
# def get_doctype_fields(doctype):
#     meta = frappe.get_meta(doctype)
#     fields = [
#         {
#             'fieldname': field.fieldname, 
#             'label': field.label,
#             'checked': check_if_field_is_selected(doctype, field.fieldname)
#         } 
#         for field in meta.fields 
#         if field.fieldtype not in ['Section Break', 'Column Break', 'HTML', 'Table', 'Button', 'Image', 'Fold']
#     ]
#     return fields

# def check_if_field_is_selected(doctype, fieldname):
#     # This is a helper function that checks if a field is selected in your settings doctype
#     # You need to replace 'Export Settings' and 'your_field' with the actual names in your implementation
#     settings = frappe.get_all('Export Settings', filters={'reference_doctype': doctype}, fields=['your_field'])
#     if not settings:
#         return False
#     selected_fields = settings[0].get('your_field')
#     if not selected_fields:
#         return False
#     return fieldname in selected_fields
