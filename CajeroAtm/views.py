class ruta_vista:

    def __init__(self):
        print ""

    def mostrar_ruta(self,tipoTemplate,modulo):
        switcher ={
            1: "<div class='col-lg-12'>"+
               "<ol class='breadcrumb'>"+
               "<li><i class='fa fa-home'></i><a href='/'>Home</a></li>"+
               "<li><i class='fa fa-desktop'></i>Banco</li>"+
               "<li><i class='fa fa-th'></i>"+modulo+"</li>"+
               "</ol>"+
               "</div>",
            2: "<div class='col-lg-12'>"+
               "<ol class='breadcrumb'>"+
               "<li><i class='fa fa-home'></i><a href='/'>Home</a></li>"+
               "<li><i class='fa fa-desktop'></i>Cajero</li>"+
               "<li><i class='fa fa-th'></i>"+modulo+"</li>"+
               "</ol>"+
               "</div>",
            3: "<div class='col-lg-12'>"+
               "<ol class='breadcrumb'>"+
               "<li><i class='fa fa-home'></i><a href='/'>Home</a></li>"+
               "<li><i class='fa fa-desktop'></i>Personal</li>"+
               "<li><i class='fa fa-th'></i>"+modulo+"</li>"+
               "</ol>"+
               "</div>"
        }
        return switcher.get(tipoTemplate,"Tipo de Templete Invalido")