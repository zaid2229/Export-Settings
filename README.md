## **Frappe Export Settings**

### **Overview**

This app allows you to predefine the fields you want to export from any given doctype in Frappe. The app adds a new "Export Settings" doctype where users can specify which fields should be prechecked when they open the Export Data dialog box.

### **Features**

1. Define prechecked fields for any doctype
1. Simplify the data export process
1. Improve user experience by minimizing manual selections

### **Installation**
  Prerequisites
  Make sure you have Frappe installed.

#### **Steps**

1. Navigate to your Frappe bench folder:

   `cd path/to/your/bench`

1. dd the GitHub repository:

   `bench get-app https://github.com/zaid2229/Export-Settings.git`

1. Install the app onto your site:

   `bench --site your-site-name install-app export_setting`

1. Migrate the database:

   `bench migrate`

1. Finally, restart your Frappe server:

   `bench restart`

### **Usage**

#### - Creating a new Export Setting
  
    1. Go to the 'Export Settings' doctype.
    2. Select the doctype you want to configure.
    3. Check the fields that should be prechecked during export.
    4. Save the document.
       
#### - Exporting Data
  
    1. Navigate to the doctype for which you've set the export settings.
    2. Click on the 'Export' button.
    3. Notice that the fields specified in the 'Export Settings' are prechecked.

### Snapshots



https://github.com/zaid2229/Export-Settings/assets/60132555/db43763b-e0f2-41fc-99c7-0185b927effc







### License

MIT
