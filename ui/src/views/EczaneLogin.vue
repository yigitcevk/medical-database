<template>
  <div class="top-frame">

    <img class="eczaneicon" src="@/assets/iconlarge.png" />

    <div class="container" style="text-align: center; align-items: center">

      <div class='EczaneIdCards' style="border-style: solid;">
        <div>
          <label for="enter-id" style="margin-top: 5px; margin-right: 5px;">Eczane ID</label>
          <input class="id-input" style="border-style: solid; margin-top: 5px;" v-model="eczaneID"
            v-on:keyup.enter="login" placeholder="Eczane Id giriş" />
        </div>

        <a class="button-login" v-on:click="login()">
          Login
        </a>

        <button class="button-login" @click="$router.go(-1)">Geri Dön</button>


      </div>

      <h1>Eczaneni sorgula!</h1>
      <p>Tüm bilgilerin burada.</p>
    </div>



  </div>
</template>

<script>
import { isProxy, toRaw } from 'vue';
export default {
  name: 'EczaneLogin',
  components: {
  },
  data() {
    return {
      eczaneID: ""
    }
  },
  created() {
  },
  methods: {
    login() {
      this.$router.push({
        name: 'EczaneAdmin',
        params: {
          eczaneID: this.eczaneID
        }
      });
    },
  }
}
</script>


<style>
.id-input {
  width: 250px;
  border-radius: 8px;
}

.eczaneicon {
  width: 15%;
  position: absolute;
  left: 0;
  top: 0;
}

.container {
  display: flex;
  position: absolute;
  margin-top: 80px;
}

.form {
  display: flex;
  flex-direction: row;
  background: #ffffff;
  box-shadow: 0px 0px 5px rgba(0, 0, 0, 0.05), 0px 25px 35px rgba(0, 0, 0, 0.03);
  border-radius: 8px;
  max-width: 664px;
  width: 100%;
  height: 56px;
  padding: 2px;
  margin: 8px;
}

.form:hover {
  box-shadow: 0px 0px 20px gray;
  transition: box-shadow 0.2s ease-in-out;
}

.form:focus-within {
  box-shadow: 0px 0px 20px gray;
  transition: box-shadow 0.2s ease-in-out;
}

.addedCars {
  display: flex;
  flex-direction: row;
}

.button-login:hover {
  box-shadow: 0px 0px 20px black;
  transition: box-shadow 0.2s ease-in-out;
}

.button-login {
  cursor: pointer;
  float: right;
  padding: 8px 12px;
  margin-top: 5px;
  margin-bottom: 5px;
  background: #1b449c;
  color: #ffffff;
  width: 50%;
  text-decoration: none;
  font-weight: bold;
  border: 2px solid #1b449c;
  box-sizing: border-box;
  border-radius: 40px;
  box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.2);
}

.button-login>.text {
  font-size: 8px;
  vertical-align: middle;
}

.EczaneIdCards {
  display: flex;
  flex-direction: column;
  text-align: center;
  align-items: center;
  /* This bit draws the box around it */
  background: #ffffff;
  /* Shadow / 1 */
  box-shadow: 0px 0px 5px rgba(0, 0, 0, 0.05), 0px 25px 35px rgba(0, 0, 0, 0.03);
  border-radius: 8px;
  width: 40%;
}
</style>
