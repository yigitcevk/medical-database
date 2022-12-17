<template>
  <div class='home-frame' style=''>
    <img
      src="@/assets/iconlarge.png"
    />
    <div>

      <a class="button-add" v-on:click="navigateEczane()">
          Eczane girişi
      </a>
      <a class="button-add" v-on:click="navigateMusteri()">
          Musteri girişi
      </a>
      <img class="tobb-etu-png" src="@/assets/tobbetu.png"/>   

    
    </div>  

  </div>
</template>

<script>

export default {
  name: 'Home',
  components: {
    
  },
  methods: {
    navigateEczane() {
      this.$router.push({
          name: 'EczanePage',
          params: {
          }
      });     
    },
    navigateMusteri() {
      this.$router.push({
          name: 'MusteriPage',
          params: {
          }
      });     
    },

  }
}

</script>

<style>

.lower-page-div {
  position: absolute;
  bottom: 0;
  text-align: center;
  padding-left: 38%;
}
.tobb-etu-png {
  position: absolute;
  bottom: 0;
  width: 5%;
  right: 0;
}

</style>
