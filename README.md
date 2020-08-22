# Arithmetic API

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/7060b44bc97d430699994fec16dfa97d)](https://app.codacy.com/manual/nklubega/mathematical-operations-API?utm_source=github.com&utm_medium=referral&utm_content=nklubega/mathematical-operations-API&utm_campaign=Badge_Grade_Dashboard)

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
