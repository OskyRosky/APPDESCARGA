import asyncio
import importlib.util
import os

# Cargar DESCARGA.py dinámicamente
ruta_descarga_py = os.path.join(os.path.dirname(__file__), '..', 'DESCARGA.py')
spec = importlib.util.spec_from_file_location("descarga", ruta_descarga_py)
descarga = importlib.util.module_from_spec(spec)
spec.loader.exec_module(descarga)

def ejecutar_descarga(url, ruta_salida):
    async def run():
        await descarga.descargar_documentos(url, ruta_salida)
    asyncio.run(run())