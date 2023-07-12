<template>
  <div class="container slide-in-top">
    <div class="row">
      <div class="col-12">
        <h3>Soporte</h3>
        <p>
          Si necesitas ayuda o tienes alguna pregunta, estamos aquí para
          asistirte. Nuestro equipo de soporte está disponible para brindarte la
          asistencia necesaria.
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
        <soporte-form></soporte-form>
        <!-- Include the SoporteForm component here -->
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
form {
  display: flex;
  flex-direction: column;
  border-radius: 16px;
  width: 100%;
  overflow: hidden;
  flex-direction: column;
}
</style>
