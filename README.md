# :test_tube: OdooAigues
An experimental project to explore how Odoo (Python-based ERP) can be used to structure and visualize public water-related data from Spain's **Instituto Nacional de Estadística (INE)**.

## :triangular_flag_on_post: Datasources
The data used comes from the INE, specifically from:

- [INE - Suministro y saneamiento del agua](https://www.ine.es/dynt3/inebase/index.htm?padre=8709&capsel=8711)
- [INE - Uso del agua en las empresas gestoras](https://www.ine.es/dynt3/inebase/index.htm?padre=8709&capsel=8710)

Clean versions of the CSVs are available in the `data/clean_data/` folder.

# :rocket: Instructions
In order to run this application you must need to do few things.

## 1. Install odoo
In main project folder, where data is run 
```git clone https://github.com/odoo/odoo.git
```
## 2. Set up postgres
Install postgres: https://www.postgresql.org/download/ and follow instructions to install it.
## 3.Download data and run formatter script (Optional)
Check README from data for more information but you have the clean data in `data/clean_data`
## 4. Install requirements
```
pip install -r odoo/requirements.txt
```
## 5. Run odoo
### Create odoo.conf file. It looks like this:
```
[options]
addons_path = odoo/addons, custom_addons

;database
db_host = localhost
db_port = 5432
db_user = user
db_password = pwd
db_name = False

; admin UI password (for creating the first DB)
admin_passwd = admin

; logging
log_level = info
logfile = odoo.log

; development convenience
dev_mode = True
```
In main project folder, where data is run 
```python odoo/odoo-bin -c odoo.conf
```
### Install requiremetns from odoo
```
pip install -r odoo/requirements.txt
# Add excel drivers just in case
pip install xlrd openpyxl
```
### Test
```
python odoo/odoo-bin --version
```
If correct the terminal must print something similar to: **Odoo Server XX.X**

