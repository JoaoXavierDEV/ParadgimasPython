<%-- 
    Document   : Resultado
    Created on : 16/11/2020, 20:40:07
    Author     : denis
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>JSP Page</title>
    </head>
    <body>
        <% Integer soma = (Integer) request.getAttribute("soma"); %>
        <h1>Soma: <%=soma%></h1>
    </body>
</html>
