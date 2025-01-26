from .models import (Proveedor, ProveedorCategoriaSubcategoria, Categoria, Subcategoria, CategoriaSubcategoria,
                     ImagenProveedor, Provincia, ProveedorProvincia, EnlaceProveedor)

from .serializers import (ProveedorSerializer, ImageProveedorSerializer, CategoriaSerializer, SubcategoriaSerializer,
                          ProveedorCategoriaSubcategoria, CategoriaSubcategoriaSerializer,
                          ProveedorCategoriaSubcategoriaSerializer, ProvinciaSerializer,ProveedorProvinciaSerializer,ProveedorProvinciaSerializerPOST,
                          EnlaceProveedorSerializer)

from django.http import QueryDict
from django.db.models import Q
from django.core import serializers

import json

# API To Proveedor

def list_Activeproveedor():

    proveedoresInfoCompleta = []

    proveedores = Proveedor.objects.filter(state="Activo").order_by('razon_social')
    serializer = ProveedorSerializer(proveedores, many=True)


    for proveedorObj in proveedores:

        category_proveedor = []
        subcategory_proveedor = []
        pronvincias_proveedor = []

        categorias = ProveedorCategoriaSubcategoria.objects.filter(proveedor=proveedorObj.id_proveedor)
        print("CATEOGIRAS")

        print(categorias)

        enlaces = EnlaceProveedor.objects.filter(proveedor=proveedorObj.id_proveedor)
        enlaceProveedorSerializer = EnlaceProveedorSerializer(enlaces, many=True)

        provincias = ProveedorProvincia.objects.filter(proveedor=proveedorObj.id_proveedor)
        serializerProvincias = ProveedorProvinciaSerializer(provincias, many=True)

        for provinciaObj in provincias:
            pronvincias_proveedor.append(provinciaObj)

        for categoriaObj in categorias:

            nombrecategoria = categoriaObj.categoria_subcategoria.categoria.nombre

            # CONDICIONAL QUE EVALUA EN EL CASO DE QUE SE TRATASE DE LA CATEGORIA DE VARIOS YA QUE ESTA NO TIENE SUBCATEGORIA
            if categoriaObj.categoria_subcategoria.subcategoria:
                nombresubcategoria = categoriaObj.categoria_subcategoria.subcategoria.nombre
            else:
                nombresubcategoria = ""

            print(nombrecategoria + nombresubcategoria)
            if nombrecategoria not in category_proveedor:
                category_proveedor.append(nombrecategoria)

            if (nombresubcategoria not in subcategory_proveedor) and categoriaObj.categoria_subcategoria.subcategoria:
                subcategory_proveedor.append(nombresubcategoria)

        imagen = ImagenProveedor.objects.filter(proveedor=proveedorObj.id_proveedor).first()

        print(pronvincias_proveedor)
        print("Test 2")
        print(serializerProvincias.data)
        print("Test 3")

        print(category_proveedor)
        print(subcategory_proveedor )
        print(pronvincias_proveedor)
        if imagen is None:

            proveedoresInfoCompleta.append({

                "id_proveedor": proveedorObj.id_proveedor,
                "ruc_cedula": proveedorObj.ruc_cedula,
                "razon_social": proveedorObj.razon_social,
                "telefono": proveedorObj.telefono,
                "correo": proveedorObj.correo,
                "provincia": serializerProvincias.data,
                "ciudad": proveedorObj.ciudad,
                "descripcion": proveedorObj.descripcion,
                "state": proveedorObj.state,
                "categoria": category_proveedor,
                "subcategorias": subcategory_proveedor,
                "enlaces": enlaceProveedorSerializer.data

            })

        else:
            proveedoresInfoCompleta.append({

                "id_proveedor": proveedorObj.id_proveedor,
                "ruc_cedula": proveedorObj.ruc_cedula,
                "razon_social": proveedorObj.razon_social,
                "telefono": proveedorObj.telefono,
                "correo": proveedorObj.correo,
                "provincia": serializerProvincias.data,
                "ciudad": proveedorObj.ciudad,
                "descripcion": proveedorObj.descripcion,
                "state": proveedorObj.state,
                "image_path": "/media/" + str(imagen.image_path),
                "categoria": category_proveedor,
                "subcategorias": subcategory_proveedor,
                "enlaces": enlaceProveedorSerializer.data

            })

    return proveedoresInfoCompleta


def list_Postulanteproveedor():

    proveedoresInfoCompleta = []
    proveedores = Proveedor.objects.filter(state="Pendiente").order_by('razon_social')

    for proveedorObj in proveedores:

        category_proveedor = []
        subcategory_proveedor = []
        pronvincias_proveedor = []

        categorias = ProveedorCategoriaSubcategoria.objects.filter(proveedor=proveedorObj.id_proveedor)

        enlaces = EnlaceProveedor.objects.filter(proveedor=proveedorObj.id_proveedor)
        enlaceProveedorSerializer = EnlaceProveedorSerializer(enlaces, many=True)

        provincias = ProveedorProvincia.objects.filter(proveedor=proveedorObj.id_proveedor)
        serializerProvincias = ProveedorProvinciaSerializer(provincias, many=True)

        for provinciaObj in provincias:
            pronvincias_proveedor.append(provinciaObj)

        for categoriaObj in categorias:

            nombrecategoria = categoriaObj.categoria_subcategoria.categoria.nombre

            # CONDICIONAL QUE EVALUA EN EL CASO DE QUE SE TRATASE DE LA CATEGORIA DE VARIOS YA QUE ESTA NO TIENE SUBCATEGORIA
            if categoriaObj.categoria_subcategoria.subcategoria:
                nombresubcategoria = categoriaObj.categoria_subcategoria.subcategoria.nombre
            else:
                nombresubcategoria = ""

            if nombrecategoria not in category_proveedor:
                category_proveedor.append(nombrecategoria)

            if nombresubcategoria not in subcategory_proveedor:
                subcategory_proveedor.append(nombresubcategoria)

        imagen = ImagenProveedor.objects.filter(proveedor=proveedorObj.id_proveedor).first()

        print(pronvincias_proveedor)
        print(serializerProvincias.data)
        if imagen is None:

            proveedoresInfoCompleta.append({

                "id_proveedor": proveedorObj.id_proveedor,
                "ruc_cedula": proveedorObj.ruc_cedula,
                "razon_social": proveedorObj.razon_social,
                "telefono": proveedorObj.telefono,
                "correo": proveedorObj.correo,
                "provincia": serializerProvincias.data,
                "ciudad": proveedorObj.ciudad,
                "descripcion": proveedorObj.descripcion,
                "state": proveedorObj.state,
                "categoria": category_proveedor,
                "subcategorias": subcategory_proveedor,
                "enlaces": enlaceProveedorSerializer.data

            })

        else:
            proveedoresInfoCompleta.append({

                "id_proveedor": proveedorObj.id_proveedor,
                "ruc_cedula": proveedorObj.ruc_cedula,
                "razon_social": proveedorObj.razon_social,
                "telefono": proveedorObj.telefono,
                "correo": proveedorObj.correo,
                "provincia": serializerProvincias.data,
                "ciudad": proveedorObj.ciudad,
                "descripcion": proveedorObj.descripcion,
                "state": proveedorObj.state,
                "image_path": "/media/" + str(imagen.image_path),
                "categoria": category_proveedor,
                "subcategorias": subcategory_proveedor,
                "enlaces": enlaceProveedorSerializer.data

            })
    return proveedoresInfoCompleta

def list_filterproveedor(data):

    proveedoresInfoCompleta = []
    print(data)
    #Mira Javier de manana, aqui debes de colocar un filtro que tambien ataque al campo de descripcion, algun tipo de concatenacion de ambas listas o un or en el filtro
    if data.get("nombreProveedorFilterOn") == "True":


        if data.get("provinciasFilterOn") == "true":
            print("Dentro de la provincia primera")
            print(data.get("listaProvinciasId").split(","))

            print(Provincia.objects.filter(id__in =  data.get("listaProvinciasId").split(",")))

            proveedores = Proveedor.objects.filter(Q(razon_social__contains=data.get("nombreProveedor")) | Q(descripcion__contains=data.get("nombreProveedor")),
                                                   Q(proveedorprovincia__provincia__id__in=data.get("listaProvinciasId").split(",")),Q(state=data.get("tipoProveedor"))).order_by('razon_social')

        else:
            proveedores = Proveedor.objects.filter(Q(razon_social__contains=data.get("nombreProveedor")) | Q(
                descripcion__contains=data.get("nombreProveedor")),
                                                   Q(state=data.get("tipoProveedor")))
    else:

        if data.get("categoriaFilterOn") == "True":
            #La categoria VARIOS no tiene subcategorias, por eso se lo coloca aqui primero
            if data.get("nombreCategoria") == "VARIOS":

                if data.get("provinciasFilterOn") == "true":
                    print("Dentro de la provincia Categoria")

                    proveedores = Proveedor.objects.filter(
                        proveedorcategoriasubcategoria__categoria_subcategoria__categoria__nombre=data.get("nombreCategoria"),
                        proveedorprovincia__provincia__id__in=data.get("listaProvinciasId").split(","), state=data.get("tipoProveedor")).order_by(
                        'razon_social')

                else:
                    proveedores = Proveedor.objects.filter(proveedorcategoriasubcategoria__categoria_subcategoria__categoria__nombre=data.get("nombreCategoria"),
                        state=data.get("tipoProveedor")).order_by('razon_social')


            else:

                if data.get("subcategoriaFilterOn") == "True":

                    if data.get("provinciasFilterOn") == "true":
                        print("Dentro de la provincia Subcategoria")



                        proveedores = Proveedor.objects.filter(
                            proveedorcategoriasubcategoria__categoria_subcategoria__categoria__nombre=data.get("nombreCategoria"),
                            proveedorcategoriasubcategoria__categoria_subcategoria__subcategoria__nombre=data.get("nombreSubcategoria"),
                            proveedorprovincia__provincia__id__in=data.get("listaProvinciasId").split(","),
                            state=data.get("tipoProveedor")).order_by('razon_social')

                    else:
                        proveedores = Proveedor.objects.filter(
                            proveedorcategoriasubcategoria__categoria_subcategoria__categoria__nombre=data.get("nombreCategoria"),
                            proveedorcategoriasubcategoria__categoria_subcategoria__subcategoria__nombre=data.get("nombreSubcategoria"),
                            state=data.get("tipoProveedor")).order_by('razon_social')




        else:
            if data.get("provinciasFilterOn") == "true":
                proveedores = Proveedor.objects.filter(Q(proveedorprovincia__provincia__id__in=data.get("listaProvinciasId").split(",")),
                                                       Q(state=data.get("tipoProveedor"))).order_by('razon_social')
            else:
                proveedores = Proveedor.objects.filter(state=data.get("tipoProveedor")).order_by('razon_social')


    for proveedorObj in proveedores:

        category_proveedor = []
        subcategory_proveedor = []
        pronvincias_proveedor = []

        categorias = ProveedorCategoriaSubcategoria.objects.filter(proveedor=proveedorObj.id_proveedor)

        enlaces =  EnlaceProveedor.objects.filter(proveedor=proveedorObj.id_proveedor)
        enlaceProveedorSerializer = EnlaceProveedorSerializer(enlaces, many=True)

        provincias = ProveedorProvincia.objects.filter(proveedor=proveedorObj.id_proveedor)
        serializerProvincias = ProveedorProvinciaSerializer(provincias, many=True)

        for provinciaObj in provincias:
            pronvincias_proveedor.append(provinciaObj)

        for categoriaObj in categorias:

            nombrecategoria = categoriaObj.categoria_subcategoria.categoria.nombre

            # CONDICIONAL QUE EVALUA EN EL CASO DE QUE SE TRATASE DE LA CATEGORIA DE VARIOS YA QUE ESTA NO TIENE SUBCATEGORIA
            if categoriaObj.categoria_subcategoria.subcategoria:
                nombresubcategoria = categoriaObj.categoria_subcategoria.subcategoria.nombre
            else:
                nombresubcategoria = ""

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
                "provincia": serializerProvincias.data,
                "ciudad": proveedorObj.ciudad,
                "descripcion": proveedorObj.descripcion,
                "state": proveedorObj.state,
                "categoria": category_proveedor,
                "subcategorias" : subcategory_proveedor,
                "enlaces": enlaceProveedorSerializer.data
            })

        else:
            proveedoresInfoCompleta.append({

                "id_proveedor": proveedorObj.id_proveedor,
                "ruc_cedula": proveedorObj.ruc_cedula,
                "razon_social": proveedorObj.razon_social,
                "telefono": proveedorObj.telefono,
                "correo": proveedorObj.correo,
                "provincia": serializerProvincias.data ,
                "ciudad": proveedorObj.ciudad,
                "descripcion": proveedorObj.descripcion,
                "state": proveedorObj.state,
                "image_path": "/media/" + str(imagen.image_path),
                "categoria": category_proveedor,
                "subcategorias": subcategory_proveedor,
                "enlaces": enlaceProveedorSerializer.data

            })

    return proveedoresInfoCompleta

def list_subcategoriasByCategoria(data):

    subcategoriaInfoCompleta = []

    categoria = Categoria.objects.filter(nombre = data.get("categoria")).first()

    categoriaSubcategorias = CategoriaSubcategoria.objects.filter(categoria = categoria.id)

    for categoriaSubcategoria in categoriaSubcategorias:

            subcategoria =  categoriaSubcategoria.subcategoria

            # CONDICIONAL QUE EVALUA EN EL CASO DE QUE SE TRATASE DE LA CATEGORIA DE VARIOS YA QUE ESTA NO TIENE SUBCATEGORIA
            if subcategoria:
                subcategoriaNombre = subcategoria.nombre
            else:
                subcategoriaNombre = ""
            subcategoriaInfoCompleta.append({

                "nombre": subcategoriaNombre,
            })

    return subcategoriaInfoCompleta

def create_proveedorCategoriaSubcategoria(data):


    for categoriaSubcategoria in data.get("subcategoriasList").split(","):

        caregoriaSubcategoriaSplitList = categoriaSubcategoria.split("-")


        categoriaTemp = caregoriaSubcategoriaSplitList[0]
        categoria = Categoria.objects.filter(nombre=categoriaTemp).first()


        #CONDICIONAL ELABORADO POR LA EXISTENCIA DE LA CATEGORIA VARIOS
        if len(caregoriaSubcategoriaSplitList) == 2:
            subcategoriaTemp = caregoriaSubcategoriaSplitList[1]
            subcategoria = Subcategoria.objects.filter(nombre=subcategoriaTemp).first()

        else:
            subcategoriaTemp = ""

        #RECUERDA QUE AQUI SE APLICARON CONDICIONALES PARA EVALUAR SI ES UNA CATEGORIA QUE NO TIENE SUBCATEGORIAS COMO LA DE VARIOS
        if(categoria and subcategoria):
            categoriaSubcategorias = CategoriaSubcategoria.objects.filter(categoria=categoria.id, subcategoria = subcategoria.id).first()

            print("Existe subcategoria")
        else:
            if categoria and (not subcategoria):
                print("NOOOO Existe subcategoria")

                categoriaSubcategorias = CategoriaSubcategoria.objects.filter(categoria=categoria.id).first()


        if(categoriaSubcategorias):
            ordinary_dict = {'proveedor': data.get("proveedor"), 'categoria_subcategoria': categoriaSubcategorias.id}
            query_dict = QueryDict('', mutable=True)
            query_dict.update(ordinary_dict)

            print(query_dict)

            serializer = ProveedorCategoriaSubcategoriaSerializer(data=query_dict)
            if serializer.is_valid():

                serializer.save()
            else:
                print(serializer.errors)


    #serializer.is_valid()
    #print(serializer.errors)

    return None

def create_proveedorProvincia(data):


    for provincias in data.get("provinciasList").split(","):


        provinciaObj = Provincia.objects.filter(id=provincias).first()

        if(provinciaObj):

            ordinary_dict = {'proveedor': data.get("proveedor"), 'provincia': provinciaObj.id }
            query_dict = QueryDict('', mutable=True)
            query_dict.update(ordinary_dict)

            print(ordinary_dict)
            print(query_dict)

            serializer = ProveedorProvinciaSerializerPOST(data = query_dict)
            print(serializer)
            if serializer.is_valid():

                serializer.save()
            else:
                    print(serializer.errors)

    #serializer.is_valid()
    #print(serializer.errors)

    return None

def create_proveedorEnlaces(data, proveedor_id):
    print("Proveedor Enlace Api")

    print(data)
    print(data.get("enlacesProveedor"))

    for proveedorEnlace in json.loads(data.get("enlacesProveedor")):

        print(proveedorEnlace)

        if(proveedorEnlace):


            ordinary_dict = {'proveedor': proveedor_id, 'enlace': proveedorEnlace.get("enlace"),
                             'linkType': proveedorEnlace.get("linkType") }
            query_dict = QueryDict('', mutable=True)
            query_dict.update(ordinary_dict)

            print(ordinary_dict)
            print(query_dict)

            serializer = EnlaceProveedorSerializer(data = query_dict)
            print(serializer)
            if serializer.is_valid():

                serializer.save()
            else:
                    print(serializer.errors)

    #serializer.is_valid()
    #print(serializer.errors)

def create_proveedor(data):
    print(data)

    serializer = ProveedorSerializer(data=data)

    #serializer.is_valid()
    #print(serializer.errors)
    if serializer.is_valid():
        serializer.save()
        print("Se guardo con exito")
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

        # CONDICIONAL QUE EVALUA EN EL CASO DE QUE SE TRATASE DE LA CATEGORIA DE VARIOS YA QUE ESTA NO TIENE SUBCATEGORIA
        if categoriaObj.categoria_subcategoria.subcategoria:
            nombresubcategoria = categoriaObj.categoria_subcategoria.subcategoria.nombre
        else:
            nombresubcategoria = ""


        category_proveedor.append({
            "categoria": categoriaObj.categoria_subcategoria.categoria.nombre,
            "image_categoria": str(categoriaObj.categoria_subcategoria.categoria.image_path),
            "subcategoria": nombresubcategoria
        })
    
    return category_proveedor


def getProveedorById(request, proveedor_id):


    proveedorObj = Proveedor.objects.filter(id_proveedor=proveedor_id).first()

    category_proveedor = []
    subcategory_proveedor = []
    pronvincias_proveedor = []

    categorias = ProveedorCategoriaSubcategoria.objects.filter(proveedor=proveedorObj.id_proveedor)
    provincias = ProveedorProvincia.objects.filter(proveedor=proveedorObj.id_proveedor)
    serializerProvincias = ProveedorProvinciaSerializer(provincias, many=True)

    for provinciaObj in provincias:
        pronvincias_proveedor.append(provinciaObj)

    for categoriaObj in categorias:

        nombrecategoria = categoriaObj.categoria_subcategoria.categoria.nombre

        # CONDICIONAL QUE EVALUA EN EL CASO DE QUE SE TRATASE DE LA CATEGORIA DE VARIOS YA QUE ESTA NO TIENE SUBCATEGORIA
        if categoriaObj.categoria_subcategoria.subcategoria:
            nombresubcategoria = categoriaObj.categoria_subcategoria.subcategoria.nombre
        else:
            nombresubcategoria = ""


        if nombrecategoria not in category_proveedor:
            category_proveedor.append(nombrecategoria)

        if nombresubcategoria not in subcategory_proveedor:
            subcategory_proveedor.append(nombresubcategoria)

    imagen = ImagenProveedor.objects.filter(proveedor=proveedorObj.id_proveedor).first()



    if imagen is None:

       return {

            "id_proveedor": proveedorObj.id_proveedor,
            "ruc_cedula": proveedorObj.ruc_cedula,
            "razon_social": proveedorObj.razon_social,
            "telefono": proveedorObj.telefono,
            "correo": proveedorObj.correo,
            "provincia": serializerProvincias.data,
            "ciudad": proveedorObj.ciudad,
            "descripcion": proveedorObj.descripcion,
            "state": proveedorObj.state,
            "categoria": category_proveedor,
            "subcategorias": subcategory_proveedor
        }

    else:
        return{

            "id_proveedor": proveedorObj.id_proveedor,
            "ruc_cedula": proveedorObj.ruc_cedula,
            "razon_social": proveedorObj.razon_social,
            "telefono": proveedorObj.telefono,
            "correo": proveedorObj.correo,
            "provincia": serializerProvincias.data,
            "ciudad": proveedorObj.ciudad,
            "descripcion": proveedorObj.descripcion,
            "state": proveedorObj.state,
            "image_path": "/media/" + str(imagen.image_path),
            "categoria": category_proveedor,
            "subcategorias": subcategory_proveedor

        }



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

def deleteProveedorProvincia(data, proveedor_id):

    proveedor = Proveedor.objects.filter(id_proveedor=proveedor_id).first()
    provinciasIdsList = data.get("provinciasIdsList").split(",")

    try:
        records = ProveedorProvincia.objects.filter(provincia__in= provinciasIdsList, proveedor = proveedor.id_proveedor)
        # Delete the record
        deleted_count, _ = records.delete()
        print(f"{deleted_count} records deleted")

        return deleted_count
    except records.DoesNotExist:
        print("Record not found")

#MODIFICA EL METODO DE AQUI ABAJO PARA TERMINAR  LA ELIMINACION DE LOS ENLACE
def deleteProveedorEnlaces(data, proveedor_id):

    proveedor = Proveedor.objects.filter(id_proveedor=proveedor_id).first()
    enlacesIdsList = data.get("enlacesIdsList").split(",")


    try:
        records = EnlaceProveedor.objects.filter(id__in=enlacesIdsList, proveedor=proveedor.id_proveedor)

        print(records)
        # Delete the record
        deleted_count, _ = records.delete()
        print(f"{deleted_count} records deleted")

        return deleted_count
    except records.DoesNotExist:
        print("Record not found")
def getCategorias():
    categorias = Categoria.objects.all()

    serializer = CategoriaSerializer(categorias, many=True)
    return serializer.data

def getProvincias():
    provincias = Provincia.objects.all()

    serializer = ProvinciaSerializer(provincias, many=True)
    return serializer.data

def getAllEnlaces():
    enlaces = EnlaceProveedor.objects.all()

    serializer = EnlaceProveedorSerializer(enlaces, many=True)
    return serializer.data