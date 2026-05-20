lote1 = {"nombre":"Don Remigio", "cultivo": "maiz","ph": 6.2, "humedad": 14, "temperatura": 12,}
lote2 = {"nombre": "La Posta", "cultivo": "soja", "ph": 6.5, "humedad": 18, "temperatura": 11,}
lote3 = {"nombre": "El Ceibo", "cultivo": "centeno", "ph": 6.7, "humedad": 22, "temperatura": 13,}
campo = [lote1, lote2, lote3]

for lote in campo:
  print ("---lote:", lote["nombre"], "---")
  print ("cultivo:", lote["cultivo"])
  print ("ph:", lote["ph"])
  print ("humedad:", lote["humedad"])
  print ("temperatura:", lote["temperatura"])
  
  if lote["humedad"] < 20:
    print ("Riego necesaro")
  else:
    print("Humedad correcta")  
  if lote["ph"] < 6:
    print ("Suelo ácido")
  if lote["temperatura"] < 4:
    print ("Riesgo de helada") 
