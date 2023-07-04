<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png" />
    <HelloWorld msg="Welcome to Your Vue.js App" :lista="lista" />
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from "@/components/HelloWorld.vue";

export default {
  name: "HomeView",
  components: {
    HelloWorld,
  },
  data() {
    return {
      lista: [
        { id: 1, name: "Elemento 1" },
        { id: 2, name: "Elemento 2" },
        { id: 3, name: "Elemento 3" },
        { id: 4, name: "Elemento 4" },
        { id: 5, name: "Elemento 5" },
      ],
    };
  },
};
</script>
