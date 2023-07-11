<template>
  <div id="main">
    <SideBar />
    <div id="content"></div>
    <router-view />
  </div>
</template>

<script>
import SideBar from "@/components/SideBar.vue";
export default {
  name: "App",
  components: {
    SideBar,
  },
  data() {
    return {
      photo: "https://via.placeholder.com/525x425",
      name: "Cesar Perales",
      age: 17,
      description:
        "Guapo por naturaleza, con propietaria pero sin dueña :Stars:. Tuyo no por siempre puesto que cesitar es libre, cesitar es amor.",
    };
  },
};
</script>

<style>
#main {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  height: 100vh;
  width: 100vw;
}

#content {
  flex-grow: 1;
}
</style>
