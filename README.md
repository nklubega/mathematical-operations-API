# Arithmetic API
 A simple Restful API for for addition, subtraction, multiplication and division operations

METHOD CHART:
Resource   Method  Path              Use                 Parameters        Status_Code
+          POST    /add              Addition            x:int, y:int      200 OK
                                                                           301 Missing Parameter
-          POST    /subtract        Subtraction          x:int, y:int      200 OK
                                                                           301 Missing Parameter
*          POST    /mutiply        Multiplication        x:nt, y:int       200 OK
                                                                           301 Missing Parameter
/          POST    /divide         Division              x:nt, y:int       200 OK
                                                                           301 Missing Parameter
                                                                           302 y is zero
