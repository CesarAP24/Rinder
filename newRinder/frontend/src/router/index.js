import { createRouter, createWebHistory } from "vue-router";
import RindYourLove from "../views/RindYourLove.vue";
import SideBar from "../components/SideBar.vue";

const routes = [
  {
    path: "/",
    name: "RindYourLove",
    components: {
      default: RindYourLove,
      sidebar: SideBar,
    },
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
