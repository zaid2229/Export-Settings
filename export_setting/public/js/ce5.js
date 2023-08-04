frappe.provide("export_setting.data_import");
frappe.provide("frappe.data_import");

export_setting.data_import.MyDataExporter = class MyDataExporter extends frappe.data_import.DataExporter {
    make_dialog() {
        // Call the original make_dialog method
        super.make_dialog();
        
        // Now add your custom button
        this.dialog.set_primary_action(__("Export Settings"), () => {
          frappe.call({
            method: 'export_setting.export_setting.api.get_export_fields',
            args: {
              doctype: this.doctype,
              docname: this.doctype
            },
            callback: (response) => {
              let selected_fieldnames = response.message.map((field) => field.fieldname);
              this.unselect_all();
              this.dialog.fields_list.forEach((field) => {
                if (field.df.fieldtype === "Check" && selected_fieldnames.includes(field.df.fieldname)) {
                  field.set_value(1);
                }
              });
            }
          });
        });
      }
      
};