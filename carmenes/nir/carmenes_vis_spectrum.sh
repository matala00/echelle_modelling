#/bin/bash
python main2.py
sed -i -e 's/(//g' echelle_orders_main.txt
sed -i -e 's/)//g' echelle_orders_main.txt
sed -i -e 's/,//g' echelle_orders_main.txt
python plot_echelle.py


