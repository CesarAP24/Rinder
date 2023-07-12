<template>
  <div id="main">
    <SideBar />
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
};
</script>

<style>
#main {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  height: 100vh;
  width: 100vw;
}

#content {
  flex-grow: 1;
}
</style>
