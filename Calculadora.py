import sys
sys.path.append("./Funciones")
import Divicion
import Multiplicacion
import Resta
import Suma


mensaje = "Ingrese un numero: "
numero1 = int(input(mensaje))

mensaje = """Ingrese una opcion:
1 -> Sumar
2 -> Restar
3 -> Multiplicar
4 -> Dividir


..."""
operador = int(input(mensaje))

mensaje = "Ingrese otro numero: "
numero2 = int(input(mensaje))


if operador == 1:
    mensaje = f"EL resultado de la suma es {Suma.sumar(numero1, numero2)}"
elif operador == 2:
    mensaje = f"EL resultado de la resta es {Resta.restar(numero1, numero2)}"

elif operador == 3:
    mensaje = f"EL resultado de la multiplicacion es {Multiplicacion.multiplicar(numero1, numero2)}"

elif operador == 4:
    mensaje = f"EL resultado de la divicion es {Divicion.dividir(numero1, numero2)}"

else:
    mensaje = "Deves de ingresar una opcion valida"
print(mensaje)
