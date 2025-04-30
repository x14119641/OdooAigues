import pandas as pd
import sys
from pathlib import Path
ODOO_PATH = Path(__file__).resolve().parents[3] / "odoo"
sys.path.append(str(ODOO_PATH))

import odoo
import odoo
from odoo import tools

odoo.tools.config.parse_config(['-c', 'odoo.conf'])

registry = odoo.modules.registry.Registry.new('aigues')


def import_water_regions(env):
    df = pd.read_csv('data/clean_data/region_codes.csv', sep=';', encoding='latin1')
    print(df)
    for _,row in df.iterrows():
        code = str(row['code']).strip()
        name = str(row['region']).strip()
        
        # Avoid Duplicates
        existing = env['water.region'].search([('code', '=', code)])
        
        if not existing:
            env['water.region'].create({
                'code':code,
                'name':name
            })
    
    print('Water dataset imported.')
    
if __name__ == '__main__':
    with registry.cursor()as cr:
        env = odoo.api.Environment(cr, odoo.SUPERUSER_ID, {})
        import_water_regions(env)
        cr.commit()
        