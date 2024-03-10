Entiendo, aquí tienes el README completo con los bloques de código de una manera que puedas copiar y pegar directamente:

```
# Proyecto de Sistema de Gestión Empresarial con Odoo

Este repositorio contiene un sistema de gestión empresarial desarrollado con Odoo. A continuación se detallan los pasos para configurar y ejecutar el proyecto:

## Configuración del Proyecto

1. **Clonar el Repositorio:** Clona este repositorio en tu máquina local.

```bash
git clone <enlace_del_repositorio>
cd <nombre_del_repositorio>
```

2. **Ejecutar con Docker:**

Asegúrate de cerrar cualquier otro proyecto antes de iniciar este.

```bash
# Ejecutar Docker Compose
docker compose up -d
```

3. **Acceso al Contenedor:**

Para acceder al contenedor, ejecuta el siguiente comando en la terminal:

```bash
docker exec -u root -it <nombre_del_contenedor> /bin/bash
```

4. **Creación de Extensión:**

Dentro del contenedor, dirígete a la carpeta de addons y crea tu extensión:

```bash
cd /mnt/extra-addons
odoo scaffold pruebaexamen/
```

5. **Dar Permisos:**

Otorga permisos de escritura a la extensión:

```bash
chmod -R 777 pruebaexamen/
```

6. **Salir del Contenedor:**

Una vez hecho, puedes salir del contenedor:

```bash
exit
```

7. **Reiniciar Docker:**

Reinicia Docker para aplicar los cambios:

```bash
docker compose restart
```

## Configuración de la Extensión

1. **Crear una Tabla en Models:**

Define la estructura de la tabla en el archivo `models.py`. Por ejemplo:

```python
from odoo import fields, models

class TestModel(models.Model):
    _name = "test_model"
    _description = "Test Model"
   
    name = fields.Char(string="Nombre")
    description = fields.Text(string="Descripcion")
```

2. **Datos Iniciales:**

Crea una carpeta `datos` y dentro un archivo `datos.xml`. Por ejemplo:

```xml
<odoo>
    <data>
        <record model="test_model" id="pruebaExamen.nombres">
            <field name="name">Pepe</field>
            <field name="description">50</field>
        </record>
    </data>
</odoo>
```

3. **Configuración de Seguridad:**

En la carpeta `security`, edita el archivo `ir.model.access.csv` y configura los permisos para la tabla:

```csv
access_pruebaexamen,pruebaexamen.model_test_model,base.group_user,1,1,1,1
```

4. **Configuración de las Vistas:**

En la carpeta `views`, edita el archivo `views.xml` para definir las vistas de la tabla:

```xml
<odoo>
    <!-- Definición de la vista -->
    <record id="view_test_model_form" model="ir.ui.view">
        <field name="name">test.model.form</field>
        <field name="model">test_model</field>
        <field name="arch" type="xml">
            <form string="Test Model">
                <field name="name"/>
                <field name="description"/>
            </form>
        </field>
    </record>
    <!-- Asignación de la vista a un menú -->
    <menuitem id="menu_test_model" name="Test Model" parent="menu_root"/>
    <menuitem id="menu_test_model_form" name="Test Model" parent="menu_test_model" action="action_test_model_form"/>
</odoo>
```

## Ejecución del Proyecto

Una vez completados los pasos de configuración, puedes ejecutar el proyecto accediendo a la URL proporcionada por Odoo en tu navegador.

