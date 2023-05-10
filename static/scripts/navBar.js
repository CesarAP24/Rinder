/*cambiar el active si se presiona los links con animacion*/
    $(document).ready(function(){
        $('.sidebar a').click(function(){
        $('.sidebar a').removeClass("active");
        $(this).addClass("active");
        });
    });
    
  /*ocultar las secciones*/
    $(document).ready(function(){
        $('.container').hide();
        $('.content').hide();
    });


    /*mostrar la sección maches*/
    $(document).ready(function(){
        const contents = $('.container');
        $('#Matches').click(function(){
            for (var i = 0; i < contents.length; i++) {
                //a todos los que no sean el actual
                if (contents[i].id != "Matches-Content") {
                    //les agrega la clase slide-out-bottom
                    contents[i].classList.add("slide-out-bottom");
                    //y les quita la clase slide-in-top
                    contents[i].classList.remove("slide-in-top");
                } else {
                    //al que sea el actual
                    contents[i].classList.add("slide-in-top");
                    contents[i].classList.remove("slide-out-bottom");

                }
            }
            setTimeout(function(){
                contents.hide();
                $('#Matches-Content').show();
                console.log("Matches");

            }, 300);
        });
        $('#Mensajes').click(function(){
            for (var i = 0; i < contents.length; i++) {
                if (contents[i].id != "Mensajes-Content") {
                    contents[i].classList.add("slide-out-bottom");
                    contents[i].classList.remove("slide-in-top");
                } else{
                    contents[i].classList.add("slide-in-top");
                    contents[i].classList.remove("slide-out-bottom");

                }
            }
            setTimeout(function(){
                contents.hide();
                $('#Mensajes-Content').show();
                console.log("Mensajes");

            }, 300);

        });
        $('#Perfil').click(function(){
            for (var i = 0; i < contents.length; i++) {
                if (contents[i].id != "Perfil-Content") {
                    contents[i].classList.add("slide-out-bottom");
                    contents[i].classList.remove("slide-in-top");
                } else{
                    contents[i].classList.add("slide-in-top");
                    contents[i].classList.remove("slide-out-bottom");

                }
            }
            setTimeout(function(){
                contents.hide();
                $('#Perfil-Content').show();
                console.log("Perfil");

            }, 300);

        });
        $('#Soporte').click(function(){
            for (var i = 0; i < contents.length; i++) {
                if (contents[i].id != "Soporte-Content") {
                    contents[i].classList.add("slide-out-bottom");
                    contents[i].classList.remove("slide-in-top");
                } else{
                    contents[i].classList.add("slide-in-top");
                    contents[i].classList.remove("slide-out-bottom");

                }
            }
            setTimeout(function(){
                contents.hide();
                $('#Soporte-Content').show();
                console.log("Soporte");

            }, 300);

        });
        $('#Posts').click(function(){
            for (var i = 0; i < contents.length; i++) {
                if (contents[i].id != "Posts-Content") {
                    contents[i].classList.add("slide-out-bottom");
                    contents[i].classList.remove("slide-in-top");
                } else{
                    contents[i].classList.add("slide-in-top");
                    contents[i].classList.remove("slide-out-bottom");

                }
            }
            setTimeout(function(){
                contents.hide();
                $('#Posts-Content').show();
                console.log("Posts");

            }, 300);

        });
        $('#Planes').click(function(){
            for (var i = 0; i < contents.length; i++) {
                if (contents[i].id != "Planes-Content") {
                    contents[i].classList.add("slide-out-bottom");
                    contents[i].classList.remove("slide-in-top");
                } else{
                    contents[i].classList.add("slide-in-top");
                    contents[i].classList.remove("slide-out-bottom");

                }
            }
            setTimeout(function(){
                contents.hide();
                $('#Planes-Content').show();
                console.log("Planes");

            }, 300);

        }
    );


    });