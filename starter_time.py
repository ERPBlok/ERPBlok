from time import time 
from anyblok import start


startt = time()
registry = start(
    'default',
    entry_points=('bloks', 'test_bloks'),
    loadwithoutmigration=True,
)
endt = time()
print(f"started time: {(endt - startt)} : {registry}")
print(registry.System.Blok)
Q = registry.System.Blok.query().order_by(registry.System.Blok.order)
print(f'{Q.where(registry.System.Blok.state == 'installed').count()} / {Q.count()} bloks installé')
print(registry.System.Blok)
print("Nombre de model : ", len(registry.loaded_namespaces))
