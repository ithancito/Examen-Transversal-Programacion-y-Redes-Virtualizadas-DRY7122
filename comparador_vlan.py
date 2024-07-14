# vlan_check.py

def verificar_vlan(vlan_id):
    if 1 <= vlan_id <= 1005:
        return "VLAN corresponde al rango normal."
    elif 1006 <= vlan_id <= 4094:
        return "VLAN corresponde al rango extendido."
    else:
        return "VLAN fuera del rango válido."

if __name__ == "__main__":
    vlan_id = int(input("Ingrese el número de VLAN: "))
    resultado = verificar_vlan(vlan_id)
    print(resultado)

