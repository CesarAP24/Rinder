<template>
  <div class="container slide-in-top">
    <div class="row">
      <div class="col-12">
        <div id="nueva-clase">
          <h3>Soporte</h3>
          <p>
            Si necesitas ayuda o tienes alguna pregunta, estamos aquí para
            asistirte. Nuestro equipo de soporte está disponible para brindarte
            la asistencia necesaria.
          </p>
          <p>Puedes contactarnos de las siguientes formas:</p>
          <ul>
            <li>
              Envíanos un correo electrónico a
              <a href="mailto:rinder.social@gmail.com?Subject=Soporte"
                >rinder.social@gmail.com</a
              >
            </li>
            <li>Llámanos al número +51 946 669 408</li>
            <li>Completa el formulario de soporte a continuación</li>
          </ul>
        </div>
        <SoporteForm></SoporteForm>
      </div>
    </div>
  </div>
</template>

<script>
import SoporteForm from "../components/SoporteForm.vue";

export default {
  name: "SoporteView",
  components: {
    SoporteForm,
  },
};
</script>

<style scoped>
.texto {
  max-width: 600px;
  margin: 0 auto;
  text-align: center;
  padding: 20px;
  background-color: #f5f5f5;
  border-radius: 8px;
  box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.1);
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

h3 {
  font-size: 24px;
  color: #333;
  margin-bottom: 20px;
}

p {
  font-size: 16px;
  color: #555;
  margin-bottom: 10px;
}

ul {
  list-style: none;
  padding: 0;
  margin-bottom: 20px;
}

li {
  font-size: 16px;
  color: #555;
  margin-bottom: 10px;
}

a {
  color: #4285f4;
  text-decoration: none;
  transition: color 0.3s ease;
}

a:hover {
  color: #1a73e8;
}

p[data-v-57ed91ba] {
  font-size: 16px;
  color: #555;
  margin-bottom: 10px;
  text-align: left;
}

#nueva-clase[data-v-57ed91ba] {
  text-align: left;
  margin-left: 50px;
  margin-top: 37px;
}

h3 {
  font-size: 1.75rem;
  color: #ff007f;
}
</style>
