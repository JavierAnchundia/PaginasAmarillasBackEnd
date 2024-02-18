from .models import Proveedor, ProveedorCategoriaSubcategoria, Categoria, Subcategoria, CategoriaSubcategoria, ImagenProveedor

from .serializers import (ProveedorSerializer, ImageProveedorSerializer, CategoriaSerializer, SubcategoriaSerializer,
                          ProveedorCategoriaSubcategoria, CategoriaSubcategoriaSerializer, ProveedorCategoriaSubcategoriaSerializer)

from django.http import QueryDict

# API To Proveedor

def list_Activeproveedor():
    proveedoresInfoCompleta = []

    proveedores = Proveedor.objects.filter(state="Activo").order_by('razon_social')
    serializer = ProveedorSerializer(proveedores, many=True)


    for proveedorObj in proveedores:

        category_proveedor = []
        subcategory_proveedor = []

        categorias = ProveedorCategoriaSubcategoria.objects.filter(proveedor=proveedorObj.id_proveedor)

        for categoriaObj in categorias:

            nombrecategoria = categoriaObj.categoria_subcategoria.categoria.nombre
            nombresubcategoria = categoriaObj.categoria_subcategoria.subcategoria.nombre

            if nombrecategoria not in category_proveedor:
                category_proveedor.append(nombrecategoria)

            if nombresubcategoria not in subcategory_proveedor:
                subcategory_proveedor.append(nombresubcategoria)

        imagen = ImagenProveedor.objects.filter(proveedor=proveedorObj.id_proveedor).first()
        if imagen is None:

            proveedoresInfoCompleta.append({

                "id_proveedor": proveedorObj.id_proveedor,
                "ruc_cedula": proveedorObj.ruc_cedula,
                "razon_social": proveedorObj.razon_social,
                "telefono": proveedorObj.telefono,
                "correo": proveedorObj.correo,
                "provincia": proveedorObj.provincia,
                "ciudad": proveedorObj.ciudad,
                "descripcion": proveedorObj.descripcion,
                "state": proveedorObj.state,
                "categoria": category_proveedor,
                "subcategorias": subcategory_proveedor
            })

        else:
            proveedoresInfoCompleta.append({

                "id_proveedor": proveedorObj.id_proveedor,
                "ruc_cedula": proveedorObj.ruc_cedula,
                "razon_social": proveedorObj.razon_social,
                "telefono": proveedorObj.telefono,
                "correo": proveedorObj.correo,
                "provincia": proveedorObj.provincia,
                "ciudad": proveedorObj.ciudad,
                "descripcion": proveedorObj.descripcion,
                "state": proveedorObj.state,
                "image_path": "/media/" + str(imagen.image_path),
                "categoria": category_proveedor,
                "subcategorias": subcategory_proveedor

            })

    return proveedoresInfoCompleta


def list_Postulanteproveedor():
    proveedores = Proveedor.objects.filter(state="Pendiente").order_by('razon_social')

    serializer = ProveedorSerializer(proveedores, many=True)
    return serializer.data

def list_filterproveedor(data):

    proveedoresInfoCompleta = []

    if data.get("nombreProveedorFilterOn") == "True":
        proveedores = Proveedor.objects.filter(razon_social__contains = data.get("nombreProveedor"),
                                               state = "Activo").order_by('razon_social')

    else:

        if data.get("categoriaFilterOn") == "True":

            if data.get("nombreSubcategoria") == "VARIOS":

                proveedores = Proveedor.objects.filter(
                proveedorcategoriasubcategoria__categoria_subcategoria__categoria__nombre=data.get("nombreCategoria"),
                state = "Activo").order_by('razon_social')

            else:

                if data.get("subcategoriaFilterOn") == "True":

                    proveedores = Proveedor.objects.filter(
                        proveedorcategoriasubcategoria__categoria_subcategoria__categoria__nombre= data.get("nombreCategoria"),
                        proveedorcategoriasubcategoria__categoria_subcategoria__subcategoria__nombre= data.get("nombreSubcategoria"),
                        state='Activo').order_by('razon_social')

        else:
            proveedores = Proveedor.objects.filter(state="Activo").order_by('razon_social')


    for proveedorObj in proveedores:

        category_proveedor = []
        subcategory_proveedor = []

        categorias = ProveedorCategoriaSubcategoria.objects.filter(proveedor=proveedorObj.id_proveedor)

        for categoriaObj in categorias:

            nombrecategoria = categoriaObj.categoria_subcategoria.categoria.nombre
            nombresubcategoria = categoriaObj.categoria_subcategoria.subcategoria.nombre

            if nombrecategoria not in category_proveedor:
                category_proveedor.append( nombrecategoria)

            if nombresubcategoria not in subcategory_proveedor:
                subcategory_proveedor.append(nombresubcategoria)

        imagen = ImagenProveedor.objects.filter(proveedor=proveedorObj.id_proveedor).first()
        if imagen is None:

            proveedoresInfoCompleta.append({

                "id_proveedor": proveedorObj.id_proveedor,
                "ruc_cedula": proveedorObj.ruc_cedula,
                "razon_social": proveedorObj.razon_social,
                "telefono": proveedorObj.telefono,
                "correo": proveedorObj.correo,
                "provincia": proveedorObj.provincia,
                "ciudad": proveedorObj.ciudad,
                "descripcion": proveedorObj.descripcion,
                "state": proveedorObj.state,
                "categoria": category_proveedor,
                "subcategorias" : subcategory_proveedor
            })

        else:
            proveedoresInfoCompleta.append({

                "id_proveedor": proveedorObj.id_proveedor,
                "ruc_cedula": proveedorObj.ruc_cedula,
                "razon_social": proveedorObj.razon_social,
                "telefono": proveedorObj.telefono,
                "correo": proveedorObj.correo,
                "provincia": proveedorObj.provincia,
                "ciudad": proveedorObj.ciudad,
                "descripcion": proveedorObj.descripcion,
                "state": proveedorObj.state,
                "image_path": "/media/" + str(imagen.image_path),
                "categoria": category_proveedor,
                "subcategorias": subcategory_proveedor

            })

    return proveedoresInfoCompleta

def list_subcategoriasByCategoria(data):

    subcategoriaInfoCompleta = []

    categoria = Categoria.objects.filter(nombre = data.get("categoria")).first()

    categoriaSubcategorias = CategoriaSubcategoria.objects.filter(categoria = categoria.id)

    for categoriaSubcategoria in categoriaSubcategorias:

            subcategoria =  categoriaSubcategoria.subcategoria

            subcategoriaInfoCompleta.append({

                "nombre": subcategoria.nombre,
            })

    return subcategoriaInfoCompleta

def create_proveedorCategoriaSubcategoria(data):
    print("Hello its me")

    print(data)

    for categoriaSubcategoria in data.get("subcategoriasList").split(","):
        categoriaTemp = categoriaSubcategoria.split("-")[0]
        subcategoriaTemp = categoriaSubcategoria.split("-")[1]

        categoria = Categoria.objects.filter(nombre=categoriaTemp).first()
        subcategoria = Subcategoria.objects.filter(nombre=subcategoriaTemp).first()

        if(categoria and subcategoria):
            categoriaSubcategorias = CategoriaSubcategoria.objects.filter(categoria=categoria.id, subcategoria = subcategoria.id).first()

            ordinary_dict = {'proveedor': data.get("proveedor"), 'categoria_subcategoria': categoriaSubcategorias.id }
            query_dict = QueryDict('', mutable=True)
            query_dict.update(ordinary_dict)

            print(query_dict)

            serializer = ProveedorCategoriaSubcategoriaSerializer(data = query_dict)
            if serializer.is_valid():

                serializer.save()
            else:
                    print(serializer.errors)

    #serializer.is_valid()
    #print(serializer.errors)

    return None

def create_proveedor(data):
    print(data)

    serializer = ProveedorSerializer(data=data)

    #serializer.is_valid()
    #print(serializer.errors)
    if serializer.is_valid():
        serializer.save()
        return serializer.data
    return None


# API To Image

def create_image_proveedor(data):

    print(data)

    serializer = ImageProveedorSerializer(data=data, many=False)
    serializer.is_valid()
    print(serializer.errors)
    if serializer.is_valid():
        print("Posi")
        serializer.save()
        return True
    return None


#API To Categoria Subcategoria por Proveedor id
def list_categoria_subcategoria(proveedor_id):
    category_proveedor = []

    categorias = ProveedorCategoriaSubcategoria.objects.filter(proveedor=proveedor_id)

    for categoriaObj in categorias:

        category_proveedor.append({
            "categoria": categoriaObj.categoria_subcategoria.categoria.nombre,
            "image_categoria": str(categoriaObj.categoria_subcategoria.categoria.image_path),
            "subcategoria": categoriaObj.categoria_subcategoria.subcategoria.nombre
        })
    
    return category_proveedor


def getProveedorById(request, proveedor_id):


    proveedor = Proveedor.objects.filter(id_proveedor=proveedor_id).first()
    serializer = ProveedorSerializer(proveedor, many=False)

    return serializer.data

def editProveedor(data, proveedor_id):


    print(proveedor_id)
    print(data)


    proveedor = Proveedor.objects.filter(id_proveedor=proveedor_id).first()
    serializer = ProveedorSerializer(proveedor, data=data, many=False)

    serializer.is_valid()
    print(serializer.errors)

    if serializer.is_valid():
        serializer.save()
        return True
    return None

def getCategorias():
    categorias = Categoria.objects.all()

    serializer = CategoriaSerializer(categorias, many=True)
    return serializer.data


