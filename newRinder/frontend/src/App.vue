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
  mounted() {
    // Acceder al token JWT almacenado en la cookie
    const cookies = document.cookie.split(";").map((cookie) => cookie.trim());
    let accessToken = null;

    for (const cookie of cookies) {
      if (cookie.startsWith("access_token=")) {
        accessToken = cookie.substring("access_token=".length);
        break;
      }
    }

    if (
      !accessToken &&
      !["/login", "/register"].includes(window.location.pathname)
    ) {
      window.location.href = "/login";
    }
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
