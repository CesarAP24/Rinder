<template>
  <div id="main">
    <MatchCard
      :photo="photo"
      :name="name"
      :age="age"
      :description="description"
    />
  </div>
</template>

<script>
import MatchCard from "@/components/MatchCard.vue";

export default {
  name: "RindYourLove",
  components: {
    MatchCard,
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
  height: 100vh;
  width: 100vw;
}
</style>
