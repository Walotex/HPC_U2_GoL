from setuptools import setup, Extension
from Cython.Build import cythonize
import numpy as np

# Configura las extensiones con los directorios de inclusión de Numpy y la biblioteca de Python
extensions = [
    Extension("cython1_gol", ["cython1_gol.pyx"], 
              include_dirs=[np.get_include()],
              libraries=['python311'], 
              library_dirs=['C:\\Users\\HP OMEN\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\site-packages\\numpy\\core\\include']),
    Extension("cython2_gol", ["cython2_gol.pyx"], 
              include_dirs=[np.get_include()],
              libraries=['python311'], 
              library_dirs=['C:\\Users\\HP OMEN\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\site-packages\\numpy\\core\\include']),
    Extension("cython3_gol", ["cython3_gol.pyx"], 
              include_dirs=[np.get_include()],
              libraries=['python311'], 
              library_dirs=['C:\\Users\\HP OMEN\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\site-packages\\numpy\\core\\include']),
    Extension("cython4_gol", ["cython4_gol.pyx"], 
              include_dirs=[np.get_include()],
              libraries=['python311'], 
              library_dirs=['C:\\Users\\HP OMEN\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\site-packages\\numpy\\core\\include'])
]

# Configura el script de setup para usar Cython y compilar las extensiones
setup(
    ext_modules=cythonize(extensions, language_level=3)
)
