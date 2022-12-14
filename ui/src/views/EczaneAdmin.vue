<template>
    <div style='heigth : 100vh'>
      <div style="myCars">
          <h1>
              Profile:
          </h1>
          <p>
              Eczane Ismi : {{eczaneAd}}
          </p>
          <p>
              Adres : {{eczaneAdres}}
          </p>
          <p>
              Eczaci Isim ve Soyisim : {{eczaciAdSoyad}}
          </p>
          <p>
              Eczaci Id  : {{eczaciId}}
          </p>
      </div>

      <div>
        <table border = "1">
            <thead>
            <tr>
                <th>İlaç Adı</th>
                <th>Alış Fiyatı</th>
                <th>Satış Fiyatı</th>
                <th>İlaç Sayısı</th>
            </tr>
            </thead>
            <tbody>
            <tr v-for="item in ilaclar" :key="item.ilac_id">
                <td>{{item.ilac_ad}}</td>
                <td>{{item.alis_fiyat}}</td>
                <td>{{item.satis_fiyat}}</td>
                <td>{{item.envanter}}</td>
                <td><button class='button-black' @click="removeMedicine(item.ilac_id)">
                    İlaç sayısını eksilt
                </button></td>
            </tr>
            </tbody>
        </table>
      </div>
    </div>
  </template>

  <script>
    export default {
        name: 'EczaneAdmin',
        components: {
        },
        data() {
            return{
                eczaneId:null,
                eczaneAd:"",
                eczaneAdresId:null,
                eczaneAdres:"",
                eczaciAdSoyad:"",
                eczaciId:null,
                ilaclar:[]
            }
        },
        created() {
            const pageInfo = this.$router.currentRoute.value;
            console.log(this.$router.currentRoute.value);
            this.eczaneId = pageInfo.params.eczaneID
            
            const url1 = 'http://127.0.0.1:5000' + pageInfo.fullPath;
            fetch(url1)
            .then(async response => {
                const data = await response.json();
                if (!response.ok) {
                    const error = (data && data.message) || response.statusText;
                    return Promise.reject(error);
                }
                this.eczaneAd = data[1].eczane_ad
                this.eczaneAdresId = data[1].adres_id

                const url2 = 'http://127.0.0.1:5000/adres/' + this.eczaneAdresId;
                fetch(url2)
                .then(async response => {
                    const data = await response.json();
                    if (!response.ok) {
                        const error = (data && data.message) || response.statusText;
                        return Promise.reject(error);
                    }
                this.eczaneAdres = data[1].il + " " + data[1].ilce +  " " + data[1].posta_kodu;
                })
                .catch(error => {
                    this.errorMessage = error;
                    console.error("There was an error!", error);
                });

                const url3 = 'http://127.0.0.1:5000/eczaci/' + this.eczaneId;
                fetch(url3)
                .then(async response => {
                    const data = await response.json();
                    if (!response.ok) {
                        const error = (data && data.message) || response.statusText;
                        return Promise.reject(error);
                    }
                    this.eczaciAdSoyad = data[1].eczaci_ad_soyad
                    this.eczaciId = data[1].eczaci_id
                })
                .catch(error => {
                    this.errorMessage = error;
                    console.error("There was an error!", error);
                });
            })
            .catch(error => {
                this.errorMessage = error;
                console.error("There was an error!", error);
            });
            const url4 = 'http://127.0.0.1:5000/ilac/' + this.eczaneId;
            fetch(url4)
                .then(async response => {
                    const data = await response.json();
                    if (!response.ok) {
                        const error = (data && data.message) || response.statusText;
                        return Promise.reject(error);
                    }
                    this.ilaclar = data;
                })
                .catch(error => {
                    this.errorMessage = error;
                    console.error("There was an error!", error);
                });
            
        },
        methods: {
            removeMedicine(ilac_id){
                let data =JSON.stringify({"ilac_id":ilac_id,"eczane_id":this.eczaneId});    
                const url5 = 'http://127.0.0.1:5000/removeMedicine'; 
                fetch(url5, {
                    method: 'post',
                    headers: {
                        'Content-Type' : 'application/json'
                    },
                body: data
                }).then(function(response){
                    console.log(response)
                }).then(function(text){
                    console.log(text);
                }).catch(function (error){
                    console.error(error);
                });
                this.resetPage();
            },
            resetPage() {
                window.location.reload();
            },
        },
    }
</script>