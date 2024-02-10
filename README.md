# odoo_custom
Customized file used during Oddo training with personal additions

At Ubuntu 23 10, oddo 16 was installed. The developper folder for new odoo mudules is :
user/FORMATION/custom

#Configure instance 
./odoo-bin - formation -i base
python3 odoo-bin -addons-path=addons -d formation

#Test postgresql
psql
exit

cd odoo/
python3 odoo-bin --addons-path=addons -d formation
sudo apt-get -y install wkhtmltopdf
cd ..

#TO run instance :
cd FORMATION/
# Activation de l'environnement
source venv/bin/activate

# Start instance with new modules
./odoo/odoo-bin -d formation -c odoo.conf -u immeuble,infrastructure

See also _history_bash to configure git
