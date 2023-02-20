{
    "name": "Library Members",
    "license": "AGPL-3",
    "description": "Manage members borrowing books.",
    "author": "Daniel Reis",
    "depends": ["library_app", "mail"],
    "application": False,
    "data": [
        "security/ir.model.access.csv",
        "security/library_security.xml",
        "views/book_view.xml",
        "views/member_view.xml",
        "views/library_menu.xml",
    ],
}