# -*- coding: utf-8 -*-
"""
            SEMANA 06 - Lun 06 / 05 /2024 - 14:37pm

Los Módulos te permitirán crear librerías de funcionalidades que puedas utilizar o 
reutilizar en cualquier momento en tu proyecto
"""

igv = 0.18

def obtenerIGVconSubtotal(subtotal):    
    return subtotal*igv

def obtenerTotalconSubtotal(subtotal):
    # subtotal + igv*subtotal
    # subtotal * (1 + 0.18)
    return subtotal*(1+igv)

# Porque si hago cambios, solo necesitariamos cambiar 
# y porque no poner 1.18???la linea 23

def obtenerSubtotalconTotal(total):
    return total/(1+igv)

def obtenerIGVconTotal(total):
    return total-obtenerSubtotalconTotal(total)
 