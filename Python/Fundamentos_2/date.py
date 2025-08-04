from datetime import datetime, date, time, timedelta

# Fecha y hora actual
ahora = datetime.now()
print("Ahora:", ahora)

# Sumar 5 días
futuro = ahora + timedelta(days=5)
print("Dentro de 5 días:", futuro)

# Crear fecha específica
fecha = datetime(2024, 12, 25, 8, 30)
print("Fecha creada:", fecha)

# Diferencia entre fechas
diferencia = futuro - fecha
print("Diferencia:", diferencia.days, "días")