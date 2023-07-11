<template>
  <div class="match-card">
    <div class="left-matches">
      <button @click="like">
        <img src="static/images/c_rosado.PNG" alt="Acepta" />
      </button>
    </div>
    <div class="center-matches">
      <div class="profile-photo-matches">
        <img :src="photo" alt="Foto de perfil" />
        <div class="profile-photo-footer">
          <h4>{{ name }}</h4>
          <h4>{{ age }}</h4>
        </div>
      </div>
      <div class="profile-info-matches">
        <p><strong>Descripción:</strong></p>
        <p>{{ description }}</p>
      </div>
    </div>
    <div class="right-matches">
      <button @click="dislike">
        <img src="static/images/equis.PNG" alt="Rechaza" />
      </button>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    photo: {
      type: String,
      required: true,
    },
    name: {
      type: String,
      required: true,
    },
    age: {
      type: Number,
      required: true,
    },
    description: {
      type: String,
      required: true,
    },
  },
  methods: {
    like() {
      // Lógica para manejar el evento de "like"
    },
    dislike() {
      // Lógica para manejar el evento de "dislike"
    },
  },
};
</script>

<style scoped>
.match-card {
  display: flex;
  flex-direction: row;
  align-items: center;
  width: 100%;
  padding: 0;
  height: 100%;
}

.profile-photo-matches {
  width: 425px;
  height: 425px;
  border: 5px solid white;
  min-height: 425px;
  display: flex;
  box-shadow: 0 0 102px rgba(0, 0, 0, 0.2);
  border-radius: 20px;
  overflow: hidden;
  margin-bottom: 30px;
  justify-content: center;
  flex-direction: column;
  align-items: center;
}

.profile-photo-matches img {
  height: 100%;
}

.profile-photo-matches h4 {
  position: relative;
  margin-top: -37px;
  top: -17px;
  color: white;
  font-weight: bolder;
  margin-left: 43px;
  margin-right: 43px;
  text-align: left;
  text-shadow: 1px 1px 1px #000000;
}

.profile-photo-footer {
  display: flex;
  width: 100%;
  justify-content: space-between;
}

.center-matches {
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 525px;
}

.center-matches .profile-info-matches {
  width: 100%;
  padding: 15px;
  border-radius: 10px;
  text-align: left;
  background: #ff007f;
  color: white;
}

.center-matches p {
  margin: 0;
  text-align: justify;
  margin-bottom: 1rem;
}

.match-card button {
  border-radius: 100%;
  overflow: hidden;
  width: 80px;
  height: 80px;
  display: flex;
  justify-content: center;
  align-items: center;
  border: none;
  outline: none;
  transition: all 0.2s ease;
}

.match-card button:hover {
  transform: scale(1.1);
  transition: all 0.2s ease;
}

.match-card button:active {
  transform: scale(0.9);
  transition: all 0.2s ease;
}

.match-card .right-matches button {
  background-color: #ffe5e5;
}

.match-card .left-matches button {
  background-color: #ffe1ec;
}

.match-card .right-matches button:hover {
  background-color: #ffc8c8;
}

.match-card .left-matches button:hover {
  background-color: #f9b9d0;
}

.match-card .right-matches button:active {
  background-color: #fdb9b9;
}

.match-card .left-matches button:active {
  background-color: #f9a3c3;
}

.match-card button img {
  width: 100%;
}

.left-matches,
.right-matches {
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 25%;
}
</style>
