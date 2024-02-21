# -*- coding: utf-8 -*-
{
    'name': "miembros de la biblioteca",

    'description': """
        Gestionar los prestamos de los miembros de la biblioteca
    """,

    'author': "SrSpooderman",

    # any module necessary for this one to work correctly
    'depends': ['library_app',"mail"],
    
    'application': False,
    
    'data': [
        "secutiry/library_security.xml",
        "security/ir.model.access.csv",
        "views/book_view.xml",
        "views/library_menu.xml",
        "views/member_view.xml",
        "views/book_list_template.xml",
    ],
}
